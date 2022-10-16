import scrapy


class CenterlinedriversSpider(scrapy.Spider):
    name = 'centerlinedrivers'
    allowed_domains = ['centerlinedrivers.com']
    start_urls = ['http://centerlinedrivers.com/']

    def parse(self, response):
        pass
