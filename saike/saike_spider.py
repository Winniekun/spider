'''
@author：KongWeiKun
@file: saike_spider.py
@time: 17-10-10 下午12:04
@contact: 836242657@qq.com
'''
import re
import requests

def get_page(url):
    try:
        response = requests.get(url)
        if response.status_code==200:
            return response.text
        return None
    except:
        return None

def get_content(html):
    pattern = re.compile('<span class="title-desc">(.*?)</span>', re.S)
    pattern1 = re.compile('<h3 class="title">.*?浏览量.*?<span class="title-desc">(.*?)</span>' +
                          '.*?<h3 class="title">.*?类型.*?<span class="title-desc">(.*?)</span>' +
                          '.*?<h3 class="title">.*?报名费.*?<span class="title-desc">(\d+)元</span>' +
                          '.*?<h3 class="title">.*?级别.*?<span class="title-desc">\n*(.*?)</span>' +
                          '.*?<h3 class="title">.*?参赛对象.*?<span class="title-desc">\n*(.*?)\n*</span>' +
                          '.*?<li class="new-event4-1-info-item clearfix">.*?class="info-content">(.*?)</div>.*?info-content">(.*?)</div>.*?info-content">(.*?)</div>.*?info-content">(.*?)</div>.*?</li>' +
                          '.*?<span class="fl item-prize">(.*?)</span>.*?<span class="fl item-prize">(.*?)</span>.*?<span class="fl item-prize">(.*?)</span>.*?<span class="fl item-prize">(.*?)</span>.*?<span class="fl item-prize">(.*?)</span>.*?<span class="fl item-prize">(.*?)</span>',
                          re.S)
    pattern2 = re.compile('<span class="fl item-prize">(.*?)</span>', re.S)
    content = re.findall(pattern1, html)
    print(content)
    # for item in content:
    #     browse = int(item[0].strip())
    #     category = item[1]
    #     price = item[2]
    #     leval = item[3].strip()
    #     target = item[4].strip()
    #     sponser = item[5] + ' , ' + item[6]
    #     register = item[7].strip().split('&nbsp;至&nbsp;')
    #     over = item[8].strip().split('&nbsp;至&nbsp;')
    #     begin = register[0] + '-' + register[1]
    #     finish = over[0] + '-' + over[1]
    #     prize = item[9] + item[10] + item[11] + item[12] + item[13]
    #     contest_category = item[14]
    #     # print(contest_category)

def main():
    url='https://www.saikr.com/apmcm/2017'
    html=get_page(url)
    # print(html)
    get_content(html)

if __name__ == '__main__':
    main()

