"""
@time : 2019/12/8下午7:39
@Author: kongwiki
@File: new.py
@Email: kongwiki@163.com
"""
import requests
from lxml import etree
response = requests.get("https://www.imdb.com/title/tt0092046/")
tree = etree.HTML(response.text)
patterns = '//div[@class="poster"]/a/img/@src'
url = tree.xpath(patterns)
print(url)