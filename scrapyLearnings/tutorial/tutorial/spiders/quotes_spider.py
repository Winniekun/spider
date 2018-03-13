'''
@author：KongWeiKun
@file: quotes_spider.py
@time: 18-3-13 下午5:07
@contact: 836242657@qq.com
'''
import scrapy
from tutorial.items import  TutorialItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
       quotes = response.css('.quote ')
       for quote in quotes:
           item = TutorialItem()
           text = quote.css('.text::text').extract_first()
           author = quote.css('.author::text').extract_first()
           tags = quote.css('.tags .tag::text').extract()
           item['text'] = text
           item['author'] = author
           item['tags'] = tags
           yield item

       next_page = response.css('.pager .next a::attr(href)').extract_first()
       if next_page is not None:
           next_page = response.urljoin(next_page)#绝对的URL
           yield scrapy.Request(next_page,callback=self.parse)




