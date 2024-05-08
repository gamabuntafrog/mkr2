import scrapy


class OlxSpider(scrapy.Spider):
    name = "olx"
    allowed_domains = ["olx.ua"]
    start_urls = ["https://olx.ua"]

    def parse(self, response):
        pass
