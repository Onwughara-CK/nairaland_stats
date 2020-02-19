# -*- coding: utf-8 -*-
import scrapy
import re


class OnlyLikedSpider(scrapy.Spider):
    name = 'only_liked'

    def start_requests(self):
        url = input('Enter link of thread:')
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        for even in response.css('table[summary=\'posts\'] tr td[class=\'l w pd\']'):
            shares_str = even.css('p.s b[id ^=\'shb\']::text')
            likes_str = even.css('p.s b[id ^=\'lpt\']::text')

            even_str = even.css('td[class="l w pd"] .narrow').get()
            text = re.sub('<[^<>]+>', '--', even_str)
            likes = 0
            shares = 0
            texts = None

            if shares_str:
                shares = re.sub('\D+', '', shares_str.get())

            if likes_str:
                likes = re.sub('\D+', '', likes_str.get())

            if text:
                texts = text

            yield {
                'likes': likes or 0,
                'shares': shares or 0,
                'comment': texts
            }

        next_url = re.search('\d+', response.url).group()
        next_pages = response.css(
            f'div.nocopy > p:first-of-type > a[href ^=\'/{next_url}\']::attr(href)').getall()
        for next_page in next_pages:
            yield response.follow(url=next_page, callback=self.parse)

# -------------- to-do--------------------------
# ---work on text
# blockquote to remain for quoted comments
# Author should be included too

# --scrape all post of a moniker
