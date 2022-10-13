from pyparsing import srange
import scrapy
from w3lib.html import remove_tags
from prodrivers.items import ProdriversItem


class SpiderprodriversSpider(scrapy.Spider):
    name = "spiderprodrivers"
    city = 'Georgia'
    start_urls = [f"https://www.prodrivers.com/jobs/?City=&State={city}"]
    custom_settings = {
        "FEED_EXPORT_FIELDS": [
            "title",
            "city",
            "basepay",
            # "shortDescription",
            "jobDescription",
            "jobRequirements",
            "jobBenefits",

        ],
    }
    def start_requests(self):
        city = 'Georgia'
        url = f"https://www.prodrivers.com/jobs/?City=&State={city}"
        yield scrapy.Request(url)

    def parse(self, response):
        item = ProdriversItem()
        for selector in response.css(".accordionHead"):
            title = selector.css("h2 ::text").get(),
            city = str(selector.css("h3 ::text").get()).strip(),
            basepay = selector.css(".basePay ::text").get(),
            # item["shortDescription"] = selector.css(".shortDescription ::text").get(),
            listajobdescription = []
            for li_selector1 in response.xpath("/html/body/section[2]/div[2]/div/div/div[2]/div/ul[1]/li/text()").getall():
                clear_selector1 = remove_tags(li_selector1).replace('\xa0',' ')
                listajobdescription.append(clear_selector1)
            
            jobDescription = listajobdescription

            listarequirements = []
            for li_selector2 in response.xpath("/html/body/section[2]/div[2]/div/div/div[2]/div/ul[2]/li/text()").getall():
                clear_selector2 = remove_tags(li_selector2).replace('\xa0',' ')
                listarequirements.append(clear_selector2)
            
            jobRequirements = listarequirements

            listaBenefits = []
            for li_selector3 in response.xpath("/html/body/section[2]/div[2]/div/div/div[2]/div/ul[3]/li/text()").getall():
                clear_selector3 = remove_tags(li_selector3).replace('\xa0',' ')
                listaBenefits.append(clear_selector3)
            
            jobBenefits = listaBenefits

            yield {
                'title': title,
                'city': city,
                'basepay': basepay,
                'jobDescription': jobDescription,
                'jobRequirements': jobRequirements,
                'jobBenefits': jobBenefits,
            }