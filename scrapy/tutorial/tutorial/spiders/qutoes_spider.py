'''
@author：KongWeiKun
@file: qutoes_spider.py
@time: 18-3-13 上午11:19
@contact: 836242657@qq.com
'''
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "qutoes" #spider 名字 唯一性

    def start_requests(self):#返回迭代请求
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response): #解析响应
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html'%page
        with open(filename,'wb') as f:
            f.write(response.body)
        self.log("Save file %s"%filename)
