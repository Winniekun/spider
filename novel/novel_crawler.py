'''
@author：KongWeiKun
@file: novel_crawler.py
@time: 18-2-19 上午11:03
@contact: 836242657@qq.com
'''
"""
爬取小说
"""
import requests
import re
url = 'http://www.99lib.net/book/1185/index.htm'

def chapter_number(index_url):
    pattern = re.compile('<dd><a href="/book/\d+/(\d+)\.htm">.*?</a>.*?</dd>', re.S)
    html = requests.get(index_url).text
    chapter = re.findall(pattern, html)
    return chapter

def chapter_content(chapter):
    pattern = re.compile('<div id="content">(.*?)</div>',re.S)
    content = re.findall(pattern,chapter)
    return content

def main():
    url = 'http://www.99lib.net/book/1185/index.htm'
    chapter = chapter_number()

if __name__ == '__main__':
    print(chapter_number(url))