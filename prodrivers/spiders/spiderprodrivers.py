import scrapy
from w3lib.html import remove_tags
from prodrivers.items import ProdriversItem


class SpiderprodriversSpider(scrapy.Spider):
    name = "spiderprodrivers"
    start_urls = ["https://www.prodrivers.com/jobs/?City=&State=Florida"]
    custom_settings = {
        "FEED_EXPORT_FIELDS": [
            "title",
            "city",
            "basepay",
            "shortDescription",
            "jobDescription",
        ],
    }
    def start_requests(self):
        url = 'https://www.prodrivers.com/jobs/?City=&State=Florida'

        yield scrapy.Request(url)

    def parse(self, response):
        item = ProdriversItem()
        for selector in response.css(".accordionHead"):
            item["title"] = selector.xpath(".//h2/text()").get(),
            item["city"] = selector.xpath(".//h3/text()").get(),
            item["basepay"] = selector.css(".basePay ::text").get(),
            item["shortDescription"] = selector.xpath(".//p[2]/text()").get(),
            for li in selector.xpath("/html/body/section[2]/div[2]/div/div[1]/div[2]/div/ul[1]"):
                item['jobDescription'] = li.xpath('.//li//text()').getall(),

            yield item
