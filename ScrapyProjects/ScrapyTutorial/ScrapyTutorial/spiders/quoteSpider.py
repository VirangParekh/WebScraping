import scrapy


class QuotespiderSpider(scrapy.Spider):
    name = 'quoteSpider'
    allowed_domains = ['https://parade.com/937586/parade/life-quotes/']
    start_urls = ['http://https://parade.com/937586/parade/life-quotes//']

    def parse(self, response):
        pass
