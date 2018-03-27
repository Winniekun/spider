'''
@author：KongWeiKun
@file: crawler_year_tags.py
@time: 18-3-27 下午3:10
@contact: 836242657@qq.com
'''
import csv
import json
import random
import re

import requests
import time
from requests import RequestException

headers = {
    'Cookie':'gsScrollPos-417=; gsScrollPos-757=424; _nu=1521005565.935; _abby=XCbZuh1bd9DtgWo; _abby_thin_ted_line=b; _abby_acme=a; _tcn=1; __gads=ID=8624370ac7978e12:T=1521957481:S=ALNI_MYN0HE9D7yjaLWqfDceS9To6KTE1A; _ga=GA1.2.76788920.1521005569; _gid=GA1.2.1250258044.1521957476',
    'Connection':'keep-alive',
    'Cache-Control':'max-age=0',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36Name'
}


def save(txtname,views,year,tags,name):
    print("视频{}发布于{}年 标签为{} 浏览量为{}".format(name,year, tags, views))
    with open('txt/{}.txt'.format(txtname),"a",encoding='utf-8') as f:
        f.write((year+" "+views+" "+tags)  + '\n')
        f.close()

def video_tags_year(video_name):
    base_url = 'https://www.ted.com/talks/'
    try:
        response = requests.get(base_url+video_name,headers=headers)
        content = response.text
        viewed_pattern = re.compile('"viewed_count":(\d+),')
        viewed = viewed_pattern.findall(content)[0]
        tags_pattern = re.compile('<script>.*?"maiTargeting":(.*?),"stream"', re.S)
        tags = tags_pattern.findall(content)
        target = json.loads("".join(tags))
        # print(target)
        video_year = target.get('year')
        video_tags = target.get('tag')
        return video_tags,viewed,video_year
    except RequestException:
        return None

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

def main():
    for i in range(64,77):
        page_names = names_crawler(i)
        print("{}共有{}视频还有{}页".format(i,len(page_names),76-i))
        for name in list(page_names):
            video_tags, viewed, video_year = video_tags_year(name)
            save('year_tags_views_2',viewed,video_year,video_tags,name)
        time.sleep(random.random()*6)
    # names = [
    #     'catherine_mohr_surgery_s_past_present_and_robotic_future',
    #     'ex_moonie_diane_benscoter_how_cults_think',
    #     'clay_shirky_how_cellphones_twitter_facebook_can_make_history',
    #     'jane_poynter_life_in_biosphere_2',
    #     'richard_st_john_success_is_a_continuous_journey',
    #     'robert_full_learning_from_the_gecko_s_tail',
    #     'nancy_etcoff_on_happiness_and_why_we_want_it',
    #     'john_la_grou_plugs_smart_power_outlets_1',
    #     'kevin_surace_fixing_drywall_to_heal_the_planet',
    #     'pete_alcorn_s_vision_of_a_better_world',
    #     ]
    # for name in names:
    #     video_tags, viewed, video_year = video_tags_year(name)
    #     save('year_tags_views_2',viewed,video_year,video_tags,name)
    #     time.sleep(random.random()*5)

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print("结束共用{}".format(end-start))