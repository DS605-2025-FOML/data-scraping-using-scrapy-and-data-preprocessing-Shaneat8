import scrapy
from ..items import QuotesScraper202518021Item
class QuoteSpider(scrapy.Spider):
    name = "quotes" 
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self , response) :
        all_div_quotes  = response.css('div.quote')

        for quote_div in all_div_quotes :
            items = QuotesScraper202518021Item()
            text  = quote_div.css('span.text::text').extract_first()
            authors  = quote_div.css('.author::text').extract_first()
            tags = quote_div.css('.tag::text').extract()

            items['text'] = text
            items['author'] = authors
            items['tags'] = tags

            yield items
        next_page = response.css('li.next a::attr(href)').get()

        if next_page is not None :
            yield response.follow(next_page,callback=self.parse)