'''
@author：KongWeiKun
@file: test.py
@time: 17-9-20 下午7:53
@contact: 836242657@qq.com
'''
import re

p='<td data-title="IP">121.232.144.158</td>'
pattern=re.compile(r'"IP">(.*?)</td>')
content=re.findall(pattern,p)
print(content)