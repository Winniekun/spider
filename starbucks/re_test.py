'''
@author：KongWeiKun
@file: re_test.py
@time: 18-1-2 下午6:21
@contact: 836242657@qq.com
'''
import re
from urllib.request import quote #URL编码

def pack_url(address):
    ak='LVsGVvCzooeqcHGM1lnNzvTTSba7gtvU'
    aks = 'fV9ODCmTALCdTtlbkRsheFUacvA9sL7A'
    base_url = 'http://api.map.baidu.com/geocoder/v2/?'
    output = 'json'
    callback = 'renderReverse'
    url = base_url+'callback='+callback+'&location='+address+'&output=json&pois=1&ak='+ak
    return url

if __name__ == '__main__':
    address = '116.51241734944347,40.04116547929337'
    print(pack_url(address))