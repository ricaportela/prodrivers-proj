from pyparsing import srange
import scrapy
from w3lib.html import remove_tags
from prodrivers.items import ProdriversItem


class SpiderprodriversSpider(scrapy.Spider):
    name = "spiderprodrivers"
    city = "Arizona"
    start_urls = ["https://www.prodrivers.com/jobs/?City=&State=Arizona"]

    def parse(self, response):
        for item in response.xpath("/html/body/section[2]/div[2]/div/div"):
            yield {
                "number": item.xpath('.//input[@id="number"]/@value').get(),
                "title": item.xpath('.//input[@id="title"]/@value').get(),
                "city": item.xpath('.//input[@id="location"]/@value').get(),
                "basepay": item.xpath('.//input[@id="pay"]/@value').get(),
                "jobDescription": [li.xpath('.//li/text()').extract() for li in item.xpath('.//ul[1]')],
                "jobRequirements": [li.xpath('.//li/text()').extract() for li in item.xpath('.//ul[2]')],
                "jobBenefits": [li.xpath('.//li/text()').extract() for li in item.xpath('.//ul[3]')]
            }