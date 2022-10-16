from csv import DictReader
from pyparsing import srange
import scrapy
from w3lib.html import remove_tags
from prodrivers.items import ProdriversItem


class SpiderprodriversSpider(scrapy.Spider):
    name = "spiderprodrivers"
    city = "California"
    start_urls = [f"https://www.prodrivers.com/jobs/?City=&State={city}"]
    def start_requests(self):
        with open ('cities.csv') as rows:
            for row in DictReader(rows):
                city=row['city']
                link = str(f"https://www.prodrivers.com/jobs/?City=&State={city}")

                yield scrapy.Request(url=link ,
                callback=self.parse)
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