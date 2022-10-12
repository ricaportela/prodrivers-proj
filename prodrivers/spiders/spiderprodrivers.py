from pyparsing import srange
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
            item["title"] = selector.css("h2 ::text").get(),
            item["city"] = selector.css("h3 ::text").get(),
            item["basepay"] = selector.css(".basePay ::text").get(),
            item["shortDescription"] = selector.css(".shortDescription ::text").get(),
            lista = []
            for li_selector in response.xpath("/html/body/section[2]/div[2]/div/div[1]/div[2]/div/ul[1]"):
                lista.append("".join(li_selector.xpath('.//li//text()').getall()))
            
            item['jobDescription'] = lista

            yield item

#/html/body/section[2]/div[2]/div/div[1]/div[2]/div/ul[1]