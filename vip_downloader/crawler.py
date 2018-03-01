'''
@author：KongWeiKun
@file: spidet.py
@time: 18-2-27 下午2:40
@contact: 836242657@qq.com
'''
import time

"""
真正视频解析地址
"""
from urllib import request,parse
import re
import requests
import urllib
import http.cookiejar
# headers = {
#     'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
#     'X-Requested-With':'XMLHttpRequest',
#     'Connection':'keep-alive',
#     'Cookie':'k1=0c32e9dd62bdda4fbc78fa87c027d7a0; k2=1018216933; k3=2581c32a2ef03711d54c094362f09e88; k4=1519725085; k5=0b023664286961bedfaf7764a6504453',
#     'Host':'vip.baiyug.cn'
# }
# session = requests.Session()
api = ' http://api.baiyug.cn/vip/index.php?url='
url = ' http://vip.baiyug.cn/baiyug.php?url='
servers = 'http://vip.baiyug.cn/baiyug.php'
target = 'http://www.iqiyi.com/v_19rre31w14.html?src=focustext_1_20130410_1'
base_file_url = 'http://vip.baiyug.cn/baiyug.php?file='
target_url =url+target
response = requests.get('http://vip.baiyug.cn/baiyug.php?url=http://www.iqiyi.com/v_19rre31w14.html?src=focustext_1_20130410_1&type=iqiyi').text
print(response)
# key_pattern = re.compile('<input id="k1".*?value="(.*?)".*?k2.*?value="(.*?)"'
#                          +'.*?k3.*?value="(.*?)".*?k4.*?value="(.*?)".*?k5.*?value="(.*?)"',re.S)
# print(key)
enc_pattern = re.compile("{.*?enc.*?:'(.*?)'",re.S)
enc = "".join(re.findall(enc_pattern,response))
urlm_pattern = re.compile(",.*?urlm.*?:.*?php\?file.*?=(.*?)\.file'",re.S)
data_urlm = re.findall(urlm_pattern,response)[0]
# print(enc)
urlm = "".join(data_urlm)
# print(urlm)
data_post = {'enc':enc}
session = requests.Session()
res = requests.post('http://vip.baiyug.cn/baiyug.php',data_post)
urls =urlm+'.file'
# print(urls)
# file = {'file':urls}
# print(file)
uuu = 'http://vip.baiyug.cn/baiyug.php?file='+urls
print(uuu)
w = 'http://vip.baiyug.cn/baiyug.php?file=744676627a7052536259544e31746655634d426b6a324c633271396a6e71584b323539677964584f6a6d65766d4a61656f714b596c5a625a6c4a686b7a4b6d676e365457717068796d7444467136586179396d6d6c3271596c35566859324f576c704c436c5669515635716e33744f64563239573139656f6e6f69536735797272616a5179703553625a65576d592b47707357756e4a65486e567169704a624b7a70745534773d3d.file'
# print(w)
headers = {
    'Cookie':'k1bdd5e5fe936564c762517928789f2be6; k2=1018216933; k3=2581c32a2ef03711d54c094362f09e88; k4=1519741352; k5=783fc0f7376f53802a21cc798e11cd75',
    'Host':'vip.baiyug.cn',
}
# print(headers)
# print(header)
video_url = requests.get(w,headers=headers)
print(video_url.text)
# print(video_url)

# print(video_url)
# """
#   函数说明:回调函数，打印下载进度
#   Parameters:
#       a b c - 返回信息
#   Returns:
#       无
#   Modify:
#       2017-09-18
#   """
#
# import sys
# def Schedule(a, b, c):
#     per = 100.0 * a * b / c
#     if  100:
#         per = 1
#     sys.stdout.write("  " + "%.2f%% 已经下载的大小:%ld 文件大小:%ld" % (per, a * b, c) + '\r')
#     sys.stdout.flush()
# def video_download(url,filename):
#     request.urlretrieve(url=url,filename=filename,reporthook=Schedule)
# print(parse.quote_plus(target))
# print(response)
# filename = 'fa'
# print('%s 下载开始'%filename)
# vd = video_download(response,filename+'.mp4')
