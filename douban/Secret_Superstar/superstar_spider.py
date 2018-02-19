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


headers={
'Connection':'keep-alive',
'Cookie':'ll="118318"; bid=y1ihsym9qH0; gr_user_id=4681365f-f15f-4de6-8fd5-6f4910e57b71; viewed="1048173_26696099_26411275"; dbcl2="173335813:cwPOWLE92xc"; ps=y; ck=MhE4; ap=1; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1518443405%2C%22https%3A%2F%2Fwww.douban.com%2Fsearch%3Fsource%3Dsuggest%26q%3D%25E7%25A5%259E%25E7%25A7%2598%25E5%25B7%25A8%25E6%2598%259F%22%5D; _vwo_uuid_v2=028B901A0FDF1EF8CCC82C6AFAEFDABD|bc5fb92ae25910505d1610260a021edc; _pk_id.100001.4cf6=aedf48c1a81e778d.1512477212.4.1518443416.1518410444.; _pk_ses.100001.4cf6=*; __utma=30149280.327903288.1512477214.1518410444.1518443406.14; __utmb=30149280.0.10.1518443406; __utmc=30149280; __utmz=30149280.1518443406.14.12.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; __utmv=30149280.17333; __utma=223695111.1053806044.1512477214.1518410444.1518443406.5; __utmb=223695111.0.10.1518443406; __utmc=223695111; __utmz=223695111.1518443406.5.4.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; push_noty_num=0; push_doumail_num=0',
'Host':'movie.douban.com',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
}

def get_page(url,data,timeOutRetry=5):
    try:
        response = requests.get(url,params=data,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except Exception as e:
        if timeOutRetry > 0:
            get_page(url=url,params=data,timeOutRetry=(timeOutRetry - 1))
        print("失败")

def parse_on_page(html):
    pattern = re.compile('<div class="comment-item".*?data-cid="(\d+)">.*?' #id
                         +'<span class="votes">(\d+)</span>.*?' #觉得有用人数
                         +'<span class="comment-info">.*?<a.*?>(.*?)</a>.*?' #用户名
                         +'<span class="allstar(\d+).*?rating".*?></span>.*?' #推荐星级
                         +'<span class="comment-time " title="(.*?)">.*?</span>.*?' #发布时间
                         +'<p.*?>(.*?)</p>',re.S)  #内容
    items = re.findall(pattern,str(html))
    if items:
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
            'status' : 'F',
            'percent_type' : ''
        }
        html = get_page(url=baseUrl,data=data)
        informations = parse_on_page(html)
        time.sleep(random.random() * 5)
        print("开始爬取第{}页还有{}页".format(i,308-i))
        if informations == None:
            break
        writeCSV('superstar-F',informations)

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

