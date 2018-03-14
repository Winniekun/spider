'''
@author：KongWeiKun
@file: xpath_0x01.py
@time: 18-3-14 上午9:56
@contact: 836242657@qq.com
'''
from lxml import etree


html = etree.parse('hello.html')
#获取所有的li标签
result = html.xpath('//li')
print(result)
#获取li标签的所有class
result = html.xpath('//li/@class')
print(result)
#获取li中href为link1.html的<a>标签
result = html.xpath('//li/a[@href="link1.html"]')
print(result)
#获取li标签下href所有<span>标签
result = html.xpath('//li//span')
print(result)

#获取li标签下的所有class 不包括li
result = html.xpath('//li/a//@class')
print(result)

#获取最后一个<li>的<a>的href
result = html.xpath('//li[last()]/a/@href')
print(result)

#获取倒数第二个元素的内容
result = html.xpath('//li[last()-1]/a')
print(result[0].text)

#获取class为bold的标签名
result = html.xpath('//*[@class="bold"]')
print(result[0].text)
print(result[0].tag)
