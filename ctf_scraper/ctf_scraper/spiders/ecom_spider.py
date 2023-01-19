# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import sys
from ctf_scraper.items import Product

from ctf_scraper.items import Product
target = "clever-lichterman-044f16.netlify.app"
targetSub = "/products"
seeds = ["/", "/robots.txt", "/admin"]

class EcomSpider(CrawlSpider):
    name = 'ecom_spider'
    allowed_domains = [target]
    start_urls = ['https://clever-lichterman-044f16.netlify.app/products/taba-cream.1/']
    for seed in seeds:
        start_urls.append("https://"+target+targetSub+seed)
    rules = [
        Rule(LinkExtractor(allow=r"products/"),
             callback='parse_item', follow=True),
    ]
    def parse_item(self, response):
        item = Product()
        item['product_url'] = response.url
        item['price'] = response.xpath("//div[@class='my-4']/span/text()").get()
        item['title'] = response.xpath('//section[1]//h2/text()').get()
        item['img_url'] = response.xpath("//div[@class='product-slider']//img/@src").get(0)
        return item