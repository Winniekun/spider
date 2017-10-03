'''
@author：KongWeiKun
@file: ip.py
@time: 17-9-20 下午8:13
@contact: 836242657@qq.com
'''
import requests
import re
p='<td data-title="IP">121.232.144.158</td>'
url='http://www.kuaidaili.com/free/'
iplist=[]
html=requests.get(url).text
pattern=re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
content=re.findall(pattern,url)
# print(content)
for ip in content:
    i=re.sub('\n','',ip)
    iplist.append(i.strip())
    print(i.strip())
