# -*- coding: utf-8 -*-

import scrapy
from ctf_scraper.items import earl
from scrapy.linkextractors import LinkExtractor

from scrapy.spiders import CrawlSpider, Rule

from ctf_scraper.items import CtfPage

target = "jupiter.challenges.picoctf.org"
targetSub = "/problem/56830"
seeds = ["", "/robots.txt", "/admin"]

class testSpider(CrawlSpider):
    name = 'testSpider'
    allowed_domains = [target]
    start_urls = []
    for seed in seeds:
        start_urls.append("https://"+target+targetSub+seed)
    rules = [
        Rule(LinkExtractor(),
            callback='parse_item', follow=True),
    ]
    def parse_item(self, response):
        item = CtfPage()

        item['page_url'] = response.url
        item['content'] = response.xpath("//html").get()
        item['title'] = response.xpath("//title/text()").get()
        return item