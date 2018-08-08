# -*- coding: utf-8 -*-
import scrapy
from ..items import OurfirstscraperItem

# because the next page button is at different place for every page, I use a for
# loop to change the ending part of url
class CgjssSpider(scrapy.Spider):
    name = 'cgjss'
    allowed_domains = ['cgjss.com']
    start_urls = ['http://www.cgjss.com/ssql.php?1=1&page='+str(i) for i in range(1, 780)]

    def parse(self, response):
        line = response.css('#searchjie_s_right tr')
        # this web doesn't have blank space printed out before text, therefore, no strip()
        for l in line[:10]:
            name = l.css('.z1::text').extract_first()
            location = l.css('.n div:nth-child(5)::text').extract_first()
            contact = l.css('.n div:nth-child(7)::text').extract_first()
            date = l.css('.n div:nth-child(8)::text').extract_first()
            item = OurfirstscraperItem()
            item['name'] = name
            item['location'] = location
            item['date'] = date
            item['contact'] = contact
            yield item
