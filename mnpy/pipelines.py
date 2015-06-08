# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from model import *

class MnpyPipeline(object):
    def process_item(self, item, spider):
        mp = ManongPython(page=item['page'], title=item['title'], url=item['url'])
        flush(mp)
        return item
