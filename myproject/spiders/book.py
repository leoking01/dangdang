# -*- coding:utf-8 -*-
# -*- coding:gbk2312 -*-
import sys
from urlparse import urljoin

from scrapy.http import Request
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

from myproject.items import BookItem

class BookSpider(CrawlSpider):
    name = 'dangdang'
    allowed_domains = ['www.dangdang.com']
    start_urls = [
        "http://www.dangdang.com"
    ]

    rules = (
        Rule(SgmlLinkExtractor(allow=(r'http://www.dangdang.com'))),
        Rule(SgmlLinkExtractor(allow=(r'http://www.dangdang.com')), callback="parse_item"),
    )
        
    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        item = BookItem()
        item['name'] = hxs.select('//div[@class]/h1/text()').extract()[0]
        item['author'] = hxs.select('//div[@class]/p[1]/a/text()').extract()
        publisher = hxs.select('//div[@class]/p[2]/a/text()').extract()
        item['publisher'] = publisher and publisher[0] or ''
        publish_date = hxs.select('//div[@class]/p[3]/text()').re(u"[\u2e80-\u9fffh]+\uff1a([\d-]+)")
        item['publish_date'] = publish_date and publish_date[0] or ''
        prices = hxs.select('//p[@class]/text()').re("(\d*\.*\d*)")
        item['price'] = prices and prices[0] or ''

        #for i in item['name']:
        #       print i.encode('utf-8')
        print item 

        return item



