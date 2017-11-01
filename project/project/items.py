# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy.item import Item, Field


class ProjectItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class LagouItem(Item):
    url = Field()
    company = Field()
    position = Field()
    salary = Field()
    # salary_max = Field()
    location = Field()
    work_years = Field()
    degree = Field()
    position_type = Field()
    tags = Field()
    pub_date = Field()
    position_desc = Field()
    work_address = Field()
    # crawled = Field()
    # spider = Field()
