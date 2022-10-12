from pyparsing import srange
import scrapy
from w3lib.html import remove_tags
from prodrivers.items import ProdriversItem


class SpiderprodriversSpider(scrapy.Spider):
    name = "spiderprodrivers"
    start_urls = ["https://www.prodrivers.com/jobs/?City=&State=Alabama"]
    custom_settings = {
        "FEED_EXPORT_FIELDS": [
            "title",
            "city",
            "basepay",
            # "shortDescription",
            "jobDescription",
        ],
    }
    def start_requests(self):
        url = 'https://www.prodrivers.com/jobs/?City=&State=Alabama'

        yield scrapy.Request(url)

    def parse(self, response):
        item = ProdriversItem()
        for selector in response.css(".accordionHead"):
            item["title"] = selector.css("h2 ::text").get(),
            item["city"] = str(selector.css("h3 ::text").get()).strip(),
            item["basepay"] = selector.css(".basePay ::text").get(),
            # item["shortDescription"] = selector.css(".shortDescription ::text").get(),
            listajobdescription = []
            for li_selector in response.xpath("/html/body/section[2]/div[2]/div/div[1]/div[2]/div/ul[1]/li").getall():
                clear_selector = remove_tags(li_selector).replace('\xa0',' ')
                listajobdescription.append(clear_selector)
            
            item['jobDescription'] = listajobdescription

            yield item