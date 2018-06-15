'''
@author  : kongweikun
@file    : test.py
@time    : 18-6-15 下午7:39
@contact : kongwiki@163.com
'''
import requests
import re

html = requests.get('https://wenku.baidu.com/view/37338aebdd36a32d72758152.html?from=search').content
content = html.decode('gbk')
# 获取文档类型
docType = re.findall(r"docType.*?\:.*?\'(.*?)\'\,", content)[0]
# 获取文档标题
title = re.findall(r"title.*?\:.*?\'(.*?)\'\,", content)[0]
# print(docType,title)

