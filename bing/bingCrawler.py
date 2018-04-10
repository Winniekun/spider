'''
@author：KongWeiKun
@file: bingCrawler.py
@time: 18-4-10 下午9:07
@contact: kongwiki@163.com
'''
'''
抓取bing图片并设置为桌面
'''
import requests
from bs4 import BeautifulSoup
import os
import datetime

dt = datetime.datetime.now()
cd = str(dt.year)+'0'+str(dt.month)+str(dt.day)
os.makedirs('Bing',exist_ok=True)
url = 'http://bingwallpaper.com/'
sc = requests.get(url)
soup = BeautifulSoup(sc.text,'lxml')
image = soup.select('.cursor_zoom img')
image_url = image[0].get('src')
res = requests.get(image_url)
with open(os.path.join('Bing',cd+'.jpg'),'wb') as file:
   file.write(res.content)
os.system('gsettings set org.gnome.desktop.background picture-uri http://file:///home/kongweikun/PycharmProjects/spider/bing/Bing/'+cd+'.jpg')
