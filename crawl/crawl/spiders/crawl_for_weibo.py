# -*- coding: utf-8 -*-
import scrapy


class CrawlForWeiboSpider(scrapy.Spider):
    name = "crawl_for_weibo"
    allowed_domains = ["weibo.com/"]
    start_urls = ['http://weibo.com//']

    def parse(self, response):
        pass
