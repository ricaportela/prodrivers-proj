# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join, TakeFirst
from w3lib.html import remove_tags


def remove_blank_space(valor):
    return valor.strip()


class ProdriversItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field(
        input_processor=MapCompose(
            str.strip,
        ),
    )
    city = scrapy.Field(
        input_processor=MapCompose(
            str.strip,
        ),
    )
    basepay = scrapy.Field(
        input_processor=MapCompose(
            str.strip,
        ),
    )
    shortDescription = scrapy.Field()
    jobDescription = scrapy.Field()
    jobRequirements = scrapy.Field()
    jobBenefits = scrapy.Field()