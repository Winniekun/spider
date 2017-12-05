'''
@author：KongWeiKun
@file: coco_spider.py
@time: 17-12-5 下午8:56
@contact: 836242657@qq.com
'''
import json
import random
import re
import requests
import time
from fake_useragent import UserAgent

'''

https://movie.douban.com/subject/20495023/comments?sort=new_score&status=P
https://movie.douban.com/subject/20495023/comments?start=40&limit=20&sort=new_score&status=P&percent_type=
https://movie.douban.com/subject/20495023/comments?start=60&limit=20&sort=new_score&status=P&percent_type=
'''



def get_page(url):
    try:
        response=requests.get(url)
        if response.status_code==200:
            return response.text
        return None

    except:
        get_page(url)


def parse_page(html):
    # s=str(html)
    # print(s)
    pattern = re.compile('<div class="comment-item".*?>.*?<div class="comment">.*?<p class="">(.*?)</p>', re.S)
    comment = re.findall(pattern,html)
    # print(comment)

    return comment

def write_file(content):
    with open('coco_comments.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)  + '\n')#写入文件,并且确定为汉字
        f.close()

def main():
    base_url='https://movie.douban.com/subject/20495023/comments?'
    sort = 'new_score'
    status = 'P'
    limit = 20
    for i in range(0,10):
        start=i*20
        url=base_url+'start='+str(start)+'&limit='+str(limit)+'&sort='+sort+'&status='+status+'&percent_type='
        print(url)
        html=get_page(url)
        comments=parse_page(html)
        print('爬取第{}页短评成功,开始写入'.format(i))
        for comment in comments:
            write_file(comment)
        time.sleep(1 + float(random.randint(1, 20)) / 20)






if __name__ == '__main__':
    main()
