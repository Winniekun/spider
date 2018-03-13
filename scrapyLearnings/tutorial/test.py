'''
@author：KongWeiKun
@file: test.py
@time: 18-3-13 下午9:35
@contact: 836242657@qq.com
'''
from scrapy import Selector
sel = Selector(
    text='<div class="hero shout">'
         '  <time datetime="2014-07-23 19:00">Special date</time>'
         '</div>')
print(sel.css('.shout').xpath('./time/@datetime').extract())

