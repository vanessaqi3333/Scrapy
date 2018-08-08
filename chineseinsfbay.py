# -*- coding: utf-8 -*-
import scrapy
from ..items import OurfirstscraperItem

# Use for loop to change the url for every page
class ChineseinsfbaySpider(scrapy.Spider):
    name = 'chineseinsfbay'
    allowed_domains = ['chineseinsfbay.com']
    start_urls = ['http://www.chineseinsfbay.com/f/page_viewforum/f_29/items_18B27BAA/start_'+str(i) for i in range(0, 1500, 15)]

    def parse(self, response):
        row = response.css('.havenopage')
        for R in row:
            url = R.css('a::attr("href")').extract_first()
            name = R.css('.title::text').extract_first()
            item = OurfirstscraperItem()
            item['url'] = response.urljoin(url)
            item['name'] = name
            # extract info from the linked page
            r = scrapy.Request(url=response.urljoin(url), callback=self.parseurl)
            r.meta['item'] = item
            yield r

    def parseurl(self, response):
        item = response.meta['item']
        # this website does not have phone number at a specific place, I extract the
        # note left from the owner
        contact = response.css('.real-content::text').extract()


        item['contact'] = contact
        yield item
