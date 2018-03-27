'''
@author：KongWeiKun
@file: crawler.py
@time: 18-3-26 下午4:56
@contact: 836242657@qq.com
'''
import json
import random

import requests
import re
from multiprocessing import Pool,cpu_count,Lock,Manager
import time

headers = {
    'Cookie':'gsScrollPos-417=; gsScrollPos-757=424; _nu=1521005565.935; _abby=XCbZuh1bd9DtgWo; _abby_thin_ted_line=b; _abby_acme=a; _tcn=1; __gads=ID=8624370ac7978e12:T=1521957481:S=ALNI_MYN0HE9D7yjaLWqfDceS9To6KTE1A; _ga=GA1.2.76788920.1521005569; _gid=GA1.2.1250258044.1521957476',
    'Connection':'keep-alive',
    'Cache-Control':'max-age=0',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36Name'
}

#名字
from requests import RequestException


def names_crawler(i):
    base_url = 'https://www.ted.com'
    url = 'https://www.ted.com/talks?page={}'.format(i)
    #匹配出视频的名字
    pattern = re.compile(
        "<div class='media__image media__image--thumb talk-link__image'>.*?"
        "<a.*?data-ga-context='talks' href='/talks/(.*?)'>",
        re.S)
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            # 每一页视频的所有名称
            video_urls = pattern.findall(response.text)
            return video_urls
        return None
    except:
        return None
#字幕
def get_subtitles(video_id):
    subtitles_url = 'https://ted2srt.org/api/talks/{}/transcripts/txt?lang=en'.format(video_id)
    if  requests.get(subtitles_url).status_code == 200:
        return requests.get(subtitles_url).text
    return '出现问题'

def video_tags_id(video_name):
    base_url = 'https://www.ted.com/talks/'
    try:
        response = requests.get(base_url+video_name,headers=headers)
        content = response.text
        tags_pattern = re.compile('<script>.*?"maiTargeting":(.*?),"stream"', re.S)
        tags = tags_pattern.findall(content)
        target = json.loads("".join(tags))
        print(target)
        video_id = target.get('id')
        video_tags = target.get('tag')
        return video_id,video_tags
    except RequestException:
        return None

def save(txtname,content,tags):
    with open('txt/{}.txt'.format(txtname),"w+") as f:
        f.write(tags+'\n')
        f.write(content)
        f.close()
        print('{}保存成功'.format(txtname))

def main():
    for i in range(7,12):
        page_names = names_crawler(i)
        print("{}共有{}视频还有{}页".format(i,len(page_names),76-i))
        for name in list(page_names):
            video_id,video_tags = video_tags_id(name)
            txt = get_subtitles(video_id)
            save(name,txt,video_tags)
        time.sleep(random.random()*5)
    # video_tags_id('rei_my_mama_black_banana')
    # print(video_tags)
    # print(video_id)
    # txt = get_subtitles(video_id)
    # print(txt)
    # save('rei_my_mama_black_banana',txt,video_tags)

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print("结束共用{}".format(end-start))