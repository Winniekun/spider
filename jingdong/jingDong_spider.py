'''
@author：KongWeiKun
@file: jingDong_spider.py
@time: 18-1-20 下午7:37
@contact: 836242657@qq.com
'''
from random import random
from time import sleep

'''
爬取京东数据
'''
import re
import json
import requests


class JingSpider:

    def __init__(self):
        self.baseurl = 'https://sclub.jd.com/comment/productPageComments.action?'
        self.headers = {
            'Cookie': 'appver=1.5.0.75771;',
            'Referer': 'https://item.jd.com/',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
        }


    def getpage(self,url,params):
        try:
            response = requests.get(url,headers=self.headers,params=params)
            return response.text
        except:
            print('error')

    def getcomments(self,data):
        pattern = re.compile('"content":"(.*?)",', re.S)
        result = re.findall(pattern, data)
        # commentCount = re.compile('"commentCount":(\d+),',re.S)
        # total = re.findall(commentCount,data)
        return result

    def write_to_file(self):
        pass


    def main(self):
        for i in range(800):
            params = {
                'callback': 'fetchJSON_comment98vv48169',
                'productId': '5089225',
                'score': '0',
                'sortType': '5',
                'page': i,
                'pageSize': '10',
                'isShadowSku': '0',
                'rid': '0',
                'fold': '1'
            }
            jsonData = self.getpage(self.baseurl,params)
            result,total = self.getcomments(jsonData)
            sleep(random*5)
            return result


if __name__ == '__main__':
    s = JingSpider()
    s.main()
    print(s.main())
    # url = 'https://sclub.jd.com/comment/productPageComments.action?'
    # params = {
    #     'callback':'fetchJSON_comment98vv48169',
    #     'productId':'5089225',
    #     'score':'0',
    #     'sortType':'5',
    #     'page':'1',
    #     'pageSize':'10',
    #     'isShadowSku':'0',
    #     'rid':'0',
    #     'fold':'1'
    # }
    # headers = {
    #     'Cookie': 'appver=1.5.0.75771;',
    #     'Referer': 'https://item.jd.com/',
    #     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
    # }
    # response = requests.get(url,headers=headers,params=params)
    # print(response.text)
    # response = response.text
    # commentCount = re.compile('"commentCount":(\d+),', re.S)
    # total = re.findall(commentCount, response)
    # print(total)