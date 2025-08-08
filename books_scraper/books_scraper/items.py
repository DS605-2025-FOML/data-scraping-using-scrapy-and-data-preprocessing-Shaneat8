# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksScraperItem(scrapy.Item):
   book_imagecover_link=scrapy.Field()
   book_title=scrapy.Field()
   book_rating=scrapy.Field()
   book_price=scrapy.Field()
   book_stock_status=scrapy.Field()