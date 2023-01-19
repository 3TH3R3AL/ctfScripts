import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import sys
from ctf_scraper.items import CtfPage

target = "13d39bf5a2b5ecd485f046297c5fbdf0.ctf.hacker101.com"
targetSub = "/problem/56830"
seeds = ["/", "/robots.txt", "/admin"]


class CTFSpider(CrawlSpider):
    name = 'ctf_spider'
    allowed_domains = [target]
    start_urls = []
    for seed in seeds:
        start_urls.append("https://"+target+seed)

    rules = [
        Rule(LinkExtractor(allow="problem/"),
             callback='parse_item', follow=True),
    ]

    def parse_item(self, response):
        item = CtfPage()

        item['page_url'] = response.url
        item['content'] = response.xpath("//html").get()
        item['title'] = response.xpath("//title/text()").get()
        return item
