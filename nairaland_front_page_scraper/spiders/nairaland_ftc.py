# -*- coding: utf-8 -*-
import scrapy
import re


class NairalandFtcSpider(scrapy.Spider):
    name = 'nairaland_ftc'
    allowed_domains = ['www.nairaland.com']
    start_urls = ['https://nairaland.com/']

    def parse(self, response):
        fp_links = response.css('.featured.w a')

        for fp_link in fp_links:
            topic = re.sub('<[^<>]+>', '', fp_link.get())
            link = fp_link.xpath('.//@href').get()
            yield response.follow(url=link, callback=self.parse_ftc)

    def parse_ftc(self, response):

        topic = response.xpath(
            '//table[@summary=\'posts\']/tr/td/a[4]/text()').get()
        rows = response.xpath(
            '//table[@summary=\'posts\']/tr/td/a[@class="user"]')[0:2]
        op = rows.xpath('.//text()')[0].get()
        ftc = rows.xpath('.//text()')[1].get()
        print(
            '---------------------\n',
            f'Topic : {topic}\n',
            f'OP : {op}\n',
            f'First to comment : {ftc}\n',
            f'URL : {response.url}\n',
            '---------------------\n')
