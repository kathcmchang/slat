# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class sustainItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
	
	url = scrapy.Field()
	link_text = scrapy.Field()
	company = scrapy.Field()
	content = scrapy.Field()
	keywords = scrapy.Field()
