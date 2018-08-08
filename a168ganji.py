# -*- coding: utf-8 -*-
import scrapy
from ..items import OurfirstscraperItem


class A168ganjiSpider(scrapy.Spider):
    name = '168ganji'
    allowed_domains = ['168ganji.com']
    start_urls = ['http://www.168ganji.com/cis/Recruitment/Index/rrm']

    def parse(self, response):
        # get the link of every page, which contains the restaurant's detailed info
        line = response.css('tr:not(:first-child)')
        for l in line:
            url = l.css('.t::attr("href")').extract_first()
            item = OurfirstscraperItem()

            r = scrapy.Request(url=response.urljoin(url), callback=self.parseurl)
            r.meta['item'] = item
            item['url'] = response.urljoin(url)
            yield r
            # flip web page
        nextPageLinkSelector = response.css('.next-page a::attr("href")').extract_first()
        if nextPageLinkSelector:
                nextPageLink = 'http://www.168ganji.com'+nextPageLinkSelector
                yield scrapy.Request(url=nextPageLink)

    def parseurl(self, response):
        item = response.meta['item']
        products = response.css('.span12')
        global x
        x = 1
        # this piece of code will extract an empty line for every odd number row (ex 1st row, 3rd row)
        # So I only print every even-number line and I could also use index number later
        for p in products:
            if x%2 ==0:
                # use strip() to delete the empty space before the text, but it has to be
                # a single piece of string
                name = str(p.css('.bgnone::text').extract_first()).strip()
                item['name'] = name
                location = str(p.css('.span7 div:nth-child(2)::text').extract_first()).strip()
                # only wants the second string in the list
                date = p.css('.span7 div:nth-child(5)::text').extract()[1].strip()
                contact = str(p.css('.span7 div:nth-child(7)::text').extract_first()).strip()
                item['location'] = location
                item['date'] = date
                item['contact'] = contact
                yield item
            x+=1
