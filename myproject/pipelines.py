# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MyprojectPipeline(object):
    def process_item(self, item, spider):
        return item
from scrapy import log
#from scrapy.core.exceptions import DropItem
from twisted.enterprise import adbapi
from scrapy.http import Request
from scrapy.exceptions import DropItem
from scrapy.contrib.pipeline.images import ImagesPipeline
import time
import MySQLdb
import MySQLdb.cursors


class MySQLStorePipeline(object):

    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
                db = 'test',
                #user = 'user',
                user = 'root',
                #passwd = '******',
                passwd = 'root',
                cursorclass = MySQLdb.cursors.DictCursor,
                charset = 'utf8',
                use_unicode = False
        )

    def process_item(self, item, spider):
        
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        
        query.addErrback(self.handle_error)
        return item
  
    def _conditional_insert(self, tx, item):
        if item.get('name'):
            tx.execute(                "insert into book (name, publisher, publish_date, price )                  values (%s, %s, %s, %s)",
                (item['name'],  item['publisher'], item['publish_date'], 
                item['price'])
            )
  
  
  
