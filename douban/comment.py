'''
@author：KongWeiKun
@file: comment.py
@time: 17-10-1 下午7:42
@contact: 836242657@qq.com
'''
import random
import time
import requests
import re
import json
from fake_useragent import UserAgent


def get_page(url):
    UA=UserAgent()
    headers={'User-Agent':UA.random}
    try:
        response=requests.get(url,headers)
        if response.status_code==200:
            return response.text
        return None
    except:
        return None

def get_comment(html):
    shtml=str(html)
    pattern = re.compile('<div.*?class="comment-item".*?>.*?<p.*?class="">(.*?)\n', re.S)
    pattern2 = re.compile('<p class="">(.*?)\n', re.S)

    comment=re.findall(pattern,shtml)
    return comment

def write_file(content):
    with open('comment.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)  + '\n')#写入文件,并且确定为汉字
        f.close()

def main():
    file='/home/kongweikun/PycharmProjects/spider/douban/result.txt'
    content=open(file)
    for row in content:
        pattern = re.compile('[a-zA-z]+://[^\s,"]*')
        url = re.findall(pattern, row)
        for l in url:
            html=get_page(l)
            comment=get_comment(html)
            print('爬取短评成功,开始写入')
            write_file(comment)
            print('写入成功')
            time.sleep(1 + float(random.randint(1, 20)) / 20)
    print('爬取结束')

if __name__ == '__main__':
    main()
