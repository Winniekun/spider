'''
@author：KongWeiKun
@file: spidet.py
@time: 18-2-27 下午2:40
@contact: 836242657@qq.com
'''
"""
真正视频解析地址
"""
from urllib import request,parse
import re
import requests
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
}
api = ' http://api.baiyug.cn/vip/index.php?url='
url = ' http://vip.baiyug.cn/baiyug.php?url='
target = 'http://www.iqiyi.com/v_19rre31w14.html?src=focustext_1_20130410_1'
target_url =url+target
response = requests.get(api+target).text
print(parse.quote_plus(target))
print(response)