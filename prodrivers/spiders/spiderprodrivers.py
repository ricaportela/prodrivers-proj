from pyparsing import srange
import scrapy
from w3lib.html import remove_tags
from prodrivers.items import ProdriversItem


class SpiderprodriversSpider(scrapy.Spider):
    name = "spiderprodrivers"
    city = "Washington"
    start_urls = ["https://www.prodrivers.com/jobs/?City=&State=Washington"]
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
        city = "Washington"
        url = "https://www.prodrivers.com/jobs/?City=&State=Washington"
        yield scrapy.Request(url)

    def parse(self, response):
        item = ProdriversItem()
        for selector in response.css(".accordionItem"):
            item["title"] = selector.css(".accordionHead h2 ::text").get()
            item["city"] = str(selector.css(".accordionHead h3 ::text").get()).strip()
            item["basepay"] = selector.css(".accordionHead .basePay ::text").get()
            item["shortDescription"] = selector.css(".accordionHead .shortDescription ::text").get()
            item["jobDescription"] =  [li.xpath('string(.)').extract()[0] for li in response.xpath('/html/body/section[2]/div[2]/div/div[1]/div[2]/div/ul[1]/li')]
            item["jobRequirements"] =  [li.xpath('string(.)').extract()[0] for li in response.xpath('/html/body/section[2]/div[2]/div/div[1]/div[2]/div/ul[2]/li')]
            item["jobBenefits"] =  [li.xpath('string(.)').extract()[0] for li in response.xpath('/html/body/section[2]/div[2]/div/div[1]/div[2]/div/ul[3]/li')]

        yield item
