'''
@author  : kongweikun
@file    : bdocCrawler.py
@time    : 18-6-15 下午7:14
@contact : kongwiki@163.com
'''

import os
import re
import json
import requests
from lxml import etree
import sys


# import tkinter

# 创建文库基类
class BaiduWK(object):
    def __init__(self, url):
        self.title = None
        self.url = url
        self.docType = None
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'}
        self.get_response_content(self.url)
        self.get_doc_type_and_title()

    def get_response_content(self, url):
        try:
            response = requests.get(url, headers=self.headers)
            return response.content
        except Exception as e:
            print(e)
            pass

    def get_doc_type_and_title(self):
        # 获取源码
        source_html = self.get_response_content(self.url)
        # 解析源码
        content = source_html.decode('gbk')
        # 获取文档类型
        self.docType = re.findall(r"docType.*?\:.*?\'(.*?)\'\,", content)[0]
        # 获取文档标题
        self.title = re.findall(r"title.*?\:.*?\'(.*?)\'\,", content)[0]


# 创建获取txt的类
class BDWKTXT(BaiduWK):
    def __init__(self, url):
        super().__init__(url)
        self.docId = None
        pass

    def get_txt(self, url):
        # 获取源码
        source_html = self.get_response_content(url)
        content = source_html.decode("gbk")
        # 获取docId
        self.docId = re.findall(r"docId.*?(\w{24}?)\'\,", content)[0]
        # 拼接请求url
        token_url = "https://wenku.baidu.com/api/doc/getdocinfo?callback=cb&doc_id=" + self.docId
        # 再次请求
        first_json = self.get_response_content(token_url).decode()
        str_first_json = re.match(r'.*?\((\{.*?\})\).*', first_json).group(1)
        # print(str_first_json)
        the_first_json = json.loads(str_first_json)
        md5sum = the_first_json["md5sum"]
        rn = the_first_json["docInfo"]["totalPageNum"]
        rsign = the_first_json["rsign"]
        # print(md5sum,"-->",rn)
        # 请求目标url
        target_url = "https://wkretype.bdimg.com/retype/text/" + self.docId + "?" + md5sum + "&callback=cb" + "&pn=1&rn=" + rn + "&type=txt" + "&rsign=" + rsign

        # https://wkretype.bdimg.com/retype/text/de53bafaf705cc1755270982?md5sum=b89f055e765e6f73db57525bcfc3c2d2&sign=7b385f9cf7&callback=cb&pn=1&rn=12&type=txt

        sec_json = self.get_response_content(target_url).decode()
        # print(type(sec_json),"-->")
        str_sec_json = re.match(r'.*?\(\[(.*)\]\)$', sec_json).group(1)
        str_sec_json += ","
        str_json_list = str_sec_json.split('},')
        result_txt = ""
        # 截取尾部空格
        str_json_list = str_json_list[:-1]
        for str_json in str_json_list:
            str_json += "}"
            pure_dic = json.loads(str_json)
            pure_txt = pure_dic["parags"][0]["c"].strip()
            result_txt += pure_txt

        # 创建文件目录
        try:
            path = "." + os.sep + self.docType
            # print(type(path),"path-->",path)

            os.makedirs(path)
        except Exception as e:
            # print("文件夹%s已存在"%(path))
            pass
        # 创建文件,保存信息
        try:
            file_name = "." + os.sep + self.docType + os.sep + self.title + ".txt"
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(result_txt)
                print("已经保存为:", self.title + '.txt')
        except Exception as e:
            # print(e)
            pass


# 创建获取word的类
class BDWKDOC(BaiduWK):
    def __init__(self, url):
        super().__init__(url)
        # 保存数据来源url
        self.pure_addr_list = list()

    # 获取数据来源url
    def get_pure_addr_list(self):
        # 获取页面源码
        source_html = self.get_response_content(self.url).decode('gbk')
        # 从源码中批量提取数据url
        all_addr = re.findall(r'wkbos\.bdimg\.com.*?json.*?expire.*?\}', source_html)
        pure_addr_list = list()
        # 获取文档标题
        self.title = etree.HTML(source_html).xpath("//title/text()")[0].strip()
        # 净化数据来源url列表
        for addr in all_addr:
            addr = "https://" + addr.replace("\\\\\\/", "/")
            addr = addr[:-5]
            pure_addr_list.append(addr)
        # 将处理好的url列表保存为全局属性
        self.pure_addr_list = pure_addr_list

        return pure_addr_list

    # 从数据来源的url列表中提取数据
    def get_json_content(self, url_list):
        content = ''
        result = ''
        sum = len(url_list)
        i = 1
        for pure_addr in url_list:
            print("正在下载第%d条数据, 剩余%d条" % (i, sum - i))
            i += 1
            try:
                # 获取json数据
                content = self.get_response_content(pure_addr).decode()
                # 处理json数据
                content = re.match(r'.*?\((.*)\)$', content).group(1)

                # 将json数据中需要的内容提取出来
                all_body_info = json.loads(content)["body"]
                # 遍历获取所有信息,并将信息拼接到一起
                for body_info in all_body_info:
                    try:
                        result = result + body_info["c"].strip()
                    # print(">>",result)
                    except Exception as e:
                        print(e)
                        pass

            except Exception as e:
                print(e)
                pass
        # 创建文件目录
        try:
            path = "." + os.sep + self.docType
            # print(type(path),"path-->",path)

            os.makedirs(path)
        except Exception as e:
            # print("文件夹%s已存在"%(path))
            pass
        # 创建文件,保存信息
        try:
            file_name = "." + os.sep + self.docType + os.sep + self.title + ".txt"
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(result)
                print("已经保存为:", self.title + '.txt')
        except Exception as e:
            print(e)


# 创建获取ppt的类
class BDWKPPT(BaiduWK):
    def __init__(self, url):
        self.all_img_url = list()
        super().__init__(url)

    # 获取json数据保存文件
    def get_ppt_json_info(self):
        # 获取源文件
        ppt_source_html = self.get_response_content(self.url)
        # 解析源文件
        content = ppt_source_html.decode('gbk')
        # print("-->",len(content))
        # 测试
        with open("test.html", "w") as f:
            f.write(content)

        # 获取文档Id
        self.docId = re.findall(r"docId.*?(\w{24}?)\'\,", content)[0]
        # 拼接请求json的接口
        source_json_url = 'https://wenku.baidu.com/browse/getbcsurl?doc_id=%s&type=ppt&callback=zhaozhao' % self.docId
        # 获取字符串类型的json数据
        str_source_json = self.get_response_content(source_json_url).decode()
        # 处理字符串类型的json数据,使其成为标准格式
        pure_str_source_json = re.match(r'.*?\((.*?)\)', str_source_json).group(1)
        # 将字符串json转为可处理的正式json
        source_json = json.loads(pure_str_source_json)

        # 遍历字典中的数据类型list
        for j in source_json['list']:
            # 创建临时列表
            temp_num_url = list()
            # 将url和page拼接到列表中
            temp_num_url.append(j["zoom"])
            temp_num_url.append(j["page"])
            # 将列表信息添加到全局变量中
            self.all_img_url.append(temp_num_url)

        # 建立文件夹
        try:
            os.makedirs("./ppt/%s" % (self.title))
        except Exception as e:
            # print("---->>",e)
            pass

        for img_url in self.all_img_url:
            # print(img_url)
            print("正在获取第%d页资源(剩余%d页)" % (img_url[1], len(self.all_img_url) - img_url[1]))
            data = self.get_response_content(img_url[0])
            path = "./ppt/%s/%s" % (self.title, str(img_url[1]) + '.jpg')
            with open(path, 'wb') as f:
                f.write(data)

        print("写入完毕")


# 运行主程序
def main():
    try:
        url = input("请输入资源所在的网址:")
        docType = BaiduWK(url).docType
    except:
        print("您输入的url,有误请重新输入!")
        os.exit()
    print("类型为", "-->", docType)

    if docType == "ppt":

        ppt = BDWKPPT(url)
        print("您将要获取的演示文稿(ppt)名称为:", ppt.title)
        ppt.get_ppt_json_info()

    elif docType == "doc":
        word = BDWKDOC(url)
        print("您将要获取的文档(word)名称为", word.title)
        pure_addr_list = word.get_pure_addr_list()
        word.get_json_content(pure_addr_list)

    elif docType == "pdf":
        pdf = BDWKDOC(url)
        print("您将要获取的PDF名称为:", pdf.title)
        pure_addr_list = pdf.get_pure_addr_list()
        pdf.get_json_content(pure_addr_list)

    elif docType == "txt":

        txt = BDWKTXT(url)
        print("您将要下载的文本文档(txt)名称为:", txt.title)
        txt.get_txt(url)

    else:
        other = BDWKPPT(url)
        print("暂不支持下载%s类型" % (other.docType))
        pass


if __name__ == '__main__':
    main()