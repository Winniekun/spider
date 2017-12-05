'''
@author：KongWeiKun
@file: douban.py
@time: 17-9-28 下午1:35
@contact: 836242657@qq.com
'''
import json
import re

import requests
from requests import RequestException
from fake_useragent import UserAgent


def get_page(url):
    UA = UserAgent()
    headers = {'User-Agent': UA.random}
    try:
        response=requests.get(url,headers)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        return None

def write_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)  + '\n')#写入文件,并且确定为汉字
        f.close()

def get_content(html):
    pattern = re.compile(
        '<dd>.*?href="(.*?)".*?blank">(.*?)</a>.*?"desc">(.*?)</div>.*?rating_nums">(.*?)</span>.*?</dd>', re.S)
    content = re.findall(pattern, html)
    # print(content)
    for item in conthoent:
        yield {
            'name' : item[1],
            'category' : item[2].strip(),
            'star' : item[3],
            'detail_url' : item[0]

        }

def main(num):
    url = 'https://www.douban.com/tag/%E5%9B%BD%E6%BC%AB/movie?start=' + str(num)
    # print(url)
    html=get_page(url)
    for item in get_content(html):
        print(item)
        write_file(item)



if __name__ == '__main__':
    for i in range(0, 210, 15):
        main(i)