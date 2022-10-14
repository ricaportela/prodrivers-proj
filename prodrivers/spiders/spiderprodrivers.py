from pyparsing import srange
import scrapy
from w3lib.html import remove_tags
from prodrivers.items import ProdriversItem


class SpiderprodriversSpider(scrapy.Spider):
    name = "spiderprodrivers"
    city = "California"
    start_urls = ["https://www.prodrivers.com/jobs/?City=&State=California"]
    custom_settings = {
        "FEED_EXPORT_FIELDS": [
            "title",
            "city",
            "basepay",
            "shortDescription",
            "jobDescription",
            "jobRequirements",
            "jobBenefits",
        ],
    }

    def start_requests(self):
        city = "California"
        url = "https://www.prodrivers.com/jobs/?City=&State=California"
        yield scrapy.Request(url)

    def parse(self, response):
        item = ProdriversItem()
        for selector in response.css(".accordionHead"):
            item["title"] = selector.css("h2 ::text").get()
            item["city"] = str(selector.css("h3 ::text").get()).strip()
            item["basepay"] = selector.css(".basePay ::text").get()
            item["shortDescription"] = response.xpath("/html/body/section[2]/div[2]/div/div[1]/div[1]/p[2]/text()")
            item["jobDescription"] = response.xpath("/html/body/section[2]/div[2]/div/div[1]/div[2]/div/ul[1]/li/text()").extract()
            item["jobRequirements"] = response.xpath("/html/body/section[2]/div[2]/div/div[1]/div[2]/div/ul[2]/li/text()").extract()
            item["jobBenefits"] = response.xpath("/html/body/section[2]/div[2]/div/div[1]/div[2]/div/ul[3]/li/text()").extract()

            yield item
