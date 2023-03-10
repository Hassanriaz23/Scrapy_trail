import scrapy

class QuoteSpider(scrapy.Spider):
    name = "book"
    start_urls = ["https://www.amazon.com/gp/new-releases/books/?ie=UTF8&ref_=sv_b_2"]

    custom_settings = {
        'FEEDS': {'data.csv': {'format': 'csv', 'encoding': 'utf-8-sig', 'overwrite': True}}
    }
    def parse(self, response):
        clan_tag = self.settings.get('clan_tag')
        book = response.css('.a-link-normal span div::text').get()
        price = response.css('._cDEzb_p13n-sc-price_3mJ9Z::text').get()
        print(f'clan tag: {self.clan_tag}')
        print(f'Book name: {book}')
        print(f'Price: {price}')
        yield {
            'clan_tag': self.clan_tag,
            'Book name': book,
            'Price': price
        }
        yield scrapy.Request('https://www.amazon.com/gp/new-releases/books/ref=zg_bsnr_pg_2?ie=UTF8&pg=2',callback= self.second_page)

    def second_page(self, response):
        book = response.css('.a-link-normal span div::text').get()
        price = response.css('._cDEzb_p13n-sc-price_3mJ9Z::text').get()
        print(f'Book name: {book}')
        print(f'Price: {price}')
        yield {
            'clan_tag': self.clan_tag,
            'Book name': book,
            'Price': price
        }

