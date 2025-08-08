import scrapy
from ..items import BooksScraperItem

class BookSpider(scrapy.Spider):
    name = "books" 
    start_urls = [
        'https://books.toscrape.com/catalogue/category/books_1/index.html'
    ]

    def parse (self , response ):
        all_book_info=response.css('article.product_pod')

        # print(all_book_info)
        for book_div in all_book_info:
            items = BooksScraperItem()
            image=book_div.css('img ::attr(src)').extract()
            image=image[0].replace('../../..','https://books.toscrape.com')
            rating=book_div.css('p.star-rating::attr(class)').extract()
            rating[0]=rating[0].replace("star-rating ","")
            # removing the star rating to save space
            title=book_div.css('h3 a::attr(title)').extract()
            price=book_div.css('.price_color::text').extract()
            status=book_div.css('.instock.availability ::text').extract()
            items['book_imagecover_link']=image
            items['book_title']=title
            items['book_rating']=rating
            items['book_price']=price
            status=status[1].strip()
            items['book_stock_status']= 1 if status == "In stock" else 0
            # items['book_stock_status']= status

            yield items
        next_page = response.css('li.next a::attr(href)').get()

        if next_page is not None :
            yield response.follow(next_page , callback=self.parse)
