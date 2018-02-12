'''
@author：KongWeiKun
@file: spider.py
@time: 17-8-10 上午10:01
@contact: 836242657@qq.com
'''
'''
抓取猫眼电影前１００电影
'''
import json
import re
import requests
from requests.exceptions import  RequestException

#抓取整个网页的源代码
def get_one_page(url):
    try:
        response=requests.get(url)#将url通过requests传过来
        if  response.status_code==200:#判断状态,若是成功则返回response text,即返回网页内容
            return response.text
        return None
    except RequestException:
        return None
#对抓取的网页进行解析
def parse_one_page(html):
    pattern=re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                       +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                       +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)#通过正则表达式生成对象
                                                                                #re.S匹配任意的字符,换行也可以
    items=re.findall(pattern,html)
    # print(items)
    for item in items:
        yield {
            'index':item[0],
            'image':item[1],
            'title':item[2],
            'actor':item[3].strip()[3:],#去掉主演：
            'time':item[4].strip()[5:],
            'score':item[5]+item[6]
        }

def write_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)  + '\n')#写入文件,并且确定为汉字
        f.close()

def main(offset):
    url = 'http://maoyan.com/board/4?offset'+str(offset)
    html = get_one_page(url)
    # print(html)
    for item in parse_one_page(html):
        print(item)
        write_file(item)

if __name__ == '__main__':
    for i in range(10):
        main(i*10)

