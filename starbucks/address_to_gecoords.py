'''
@author：KongWeiKun
@file: address_to_gecoords.py
@time: 18-1-2 下午5:55
@contact: 836242657@qq.com
'''
import csv
import json
import random
import re

import requests
import time

'''
地址转经纬度
'''
from urllib.request import quote #URL编码

def getLngLat(url,timeOutRetry=5):
    try:
        response = requests.get(url)
        return response.text
    except Exception as e:
        if timeOutRetry>0:
            getLngLat(url,timeOutRetry=(timeOutRetry-1))
        print("真的失败了")

def write_to_file(content):
    with open('./resources/starbucks_result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')  # 写入文件,并且确定为汉字
        f.close()

def pack_url(address):
    ak='LVsGVvCzooeqcHGM1lnNzvTTSba7gtvU'
    aks = 'fV9ODCmTALCdTtlbkRsheFUacvA9sL7A'
    base_url = 'http://api.map.baidu.com/geocoder/v2/?address='
    output = 'json'
    callback = 'showLocation'
    url = base_url+quote(address)+"&output="+output+"&ak="+ak+"&callback"+callback
    return url

def readCsv(filename):
    reader = csv.reader(open(filename))
    return reader

def main():
    starbucks = './resources/starbucks.csv'
    reader = readCsv(starbucks)
    # address = '天安门'
    # url = pack_url(address)
    # gecoord = getLngLat(url)
    # print(gecoord)
    # pattern = re.compile('"lng":(.*?),"lat":(.*?)}')
    # lngLat = re.findall(pattern, gecoord)
    # if lngLat:
    #     for ll in lngLat:
    #         print(ll[0])
    #         print('写入文件%s%s' % ll)
    #         print(','.join(ll))
    for row in reader:
        address = row[0]
        url=pack_url(address)
        gecoord=getLngLat(url)
        print(gecoord)
        pattern = re.compile('"lng":(.*?),"lat":(.*?)}')
        lngLat=re.findall(pattern, gecoord)
        if lngLat:
            for ll in lngLat:
                print(ll[0])
                print('写入文件%s%s'%ll)
                write_to_file(','.join(ll))
        time.sleep(random.random()*5)


if __name__ == '__main__':
    # main()
    #利用localtime()
    #函数将时间戳转化成localtime的格式
    #利用strftime()
    #函数重新格式化时间
    start = time.time()
    main()
    end = time.time()
    print("转换完成,共消耗%s"%(end-start))