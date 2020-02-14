# -*- coding: utf-8 -*-
import scrapy
import re


class NairalandSpider(scrapy.Spider):
    name = 'nairaland'
    allowed_domains = ['www.nairaland.com']
    start_urls = ['https://nairaland.com/']

    def parse(self, response):

        fp_links = response.css('.featured.w a')

        for count, fp_link in enumerate(fp_links, 1):

            text = re.sub('<[^<>]+>', '', fp_link.get())
            href = fp_link.xpath('.//@href').get()

            yield print('--------------------------------------\n',
                        f'Rank : {count}\n',
                        '--------------------------------------\n',
                        f'text : {text}\n',
                        '--------------------------------------\n',
                        f'link : {href}\n')
