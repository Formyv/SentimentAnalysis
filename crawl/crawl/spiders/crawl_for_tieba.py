# -*- coding: utf-8 -*-
import scrapy


class CrawlForTiebaSpider(scrapy.Spider):
    name = "crawl_for_tieba"
    allowed_domains = ["tieba.baidu.com/"]
    start_urls = ['http://tieba.baidu.com//']

    def parse(self, response):
        pass
