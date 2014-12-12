# -*- coding:utf-8 -*-
# -*- coding:gbk2312 -*-
import sys
from urlparse import urljoin

from scrapy.http import Request
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

from myproject.items import BookItem
add = 0
sys.stdout=open('output.txt','w')
class BookSpider(CrawlSpider):
    name = 'dangdang'
    allowed_domains = [ 'e.dangdang.com']
    start_urls = [
#        "http://book.dangdang.com"
        'http://e.dangdang.com/list_98.01.03.45.htm'
        #'http://e.dangdang.com'
    ]

    rules = (
        #Rule(SgmlLinkExtractor(allow=(r'http://book.dangdang.com'))),
        #Rule(SgmlLinkExtractor(allow=(r'http://product.dangdang.com/1900011000\.html')), callback="parse_item"),
        Rule(SgmlLinkExtractor(allow=(r'http://e.dangdang.com/.*\.htm')), callback="parse_item"),
    )



    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        item = BookItem()
        global add
        add+=1
        item['id']=add
        #names = hxs.select('/html/body/div/div/h1/span[@class]/text()').extract()
        #xiaowangzi = hxs.select('/html/body/div/div/div/div/div/div/div/div/ul/li[@class]/a/@title').extract()
        shehuidangdang = hxs.select('/html/body/div/div/div/div[@class=\'e_Cbdr\']/a/@title').extract()
        item['name']=shehuidangdang and shehuidangdang[0] or ''
#        author=hxs.select('//div[@class]//a/text()').extract()
#        item['author']=author and author[0] or ''
#        publisher = hxs.select('//div[@class]/p[2]//a/text()').extract()
#        item['publisher'] = publisher and publisher[0] or ''
#        publish_date = hxs.select('//div[@class]//text()').re(u"[\u2e80-\u9fffh]+\uff1a([\d-]+)")
#        item['publish_date'] = publish_date and publish_date[0] or ''
#        prices = hxs.select('//p[@class]//text()').re("(\d*\.*\d*)")
#        item['price'] = prices and prices[0] or ''

        #for i in item['name']:
        #       print i.encode('utf-8')
        print item 

        return item



