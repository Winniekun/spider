'''
@author：KongWeiKun
@file: superstar_spider.py
@time: 18-2-12 上午10:31
@contact: 836242657@qq.com
'''
import codecs
import csv

import requests
import random
import re

import time


def get_page(url,data,timeOutRetry=5):
    try:
        response = requests.get(url,data=data)
        if response.status_code == 200:
            return response.text
        return None
    except Exception as e:
        if timeOutRetry > 0:
            get_page(url=url, timeOutRetry=(timeOutRetry - 1))
        print("失败")

def parse_on_page(html):
    pattern = re.compile('<div class="comment-item".*?data-cid="(\d+)">.*?' #id
                         +'<span class="votes">(\d+)</span>.*?' #觉得有用人数
                         +'<span class="comment-info">.*?<a.*?>(.*?)</a>.*?' #用户名
                         +'<span class="allstar(\d+).*?rating".*?></span>.*?' #推荐星级
                         +'<span class="comment-time " title="(.*?)">.*?</span>.*?' #发布时间
                         +'<p.*?>(.*?)</p>',re.S)  #内容
    items = re.findall(pattern,html)
    for item in items:
        yield {
            'comment_id' : item[0],
            'votes' : item[1],
            'username' : item[2],
            'star' : item[3],
            'time' : item[4],
            'comment' : re.sub('\n+','',item[5].strip())

        }

def main():
    baseUrl = 'https://movie.douban.com/subject/26942674/comments?'
    for i in range(308):
        data = {
            'start' : i*20,
            'limit' : '20',
            'sort' : 'new_score',
            'status' : 'P',
            'percent_type' : ''
        }
        html = get_page(url=baseUrl,data=data)
        informations = parse_on_page(html)
        time.sleep(random.random() * 5)
        print("开始爬取第{}页还有{}页".format(i,308-i))
        if informations == None:
            break
        writeCSV('superstar',informations)

def writeCSV(filename,informations):
    csv_file = codecs.open(filename+'.csv','ab','utf-8','ignore')
    csv_writer=csv.writer(csv_file)
    for row  in informations:
        print("写入{}用户的评价".format(row['username']))
        csv_writer.writerow([row['comment_id'],row['votes'] ,row['username'] ,row['star'],row['time'],
                             row['comment']])


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print("爬完了共用了{}".format(end-start))

