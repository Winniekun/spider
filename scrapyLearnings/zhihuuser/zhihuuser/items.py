# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field

class UserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    answer_count = Field()
    articles_count = Field()
    avatar_url = Field()
    badge = Field()
    employments = Field()
    follower_count = Field()
    gender = Field()
    headline = Field()
    id = Field()
    name = Field()
    type = Field()
    url = Field()
    url_token = Field()
    user_type = Field()
