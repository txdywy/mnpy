from scrapy import Spider
from mnpy.items import MnpyItem
from mnpy.model import *
from sqlalchemy.sql import func

class MnpySpider(Spider):
    try:
        start = db_session.query(func.max(ManongPython.page)).first()[0] + 1
        end = start + 5
    except Exception, e:
        start = 1
        end = 10
    name, start_urls = 'mnpy', ['http://weekly.manong.io/issues/%s' % i for i in range(start, end)]

    def parse(self, response):
        tags = response.selector.xpath('//a')
        items = []
        for i in tags:
    	    item = MnpyItem()
            item['page'] = response.url.split('/')[-1]
            item['title'] = i.xpath('text()').extract()
            item['url'] = i.xpath('@href').extract()
            if item['title'] and 'python' in item['title'][0].lower() and u'\u5de5\u7a0b\u5e08' not in item['title'][0]:
                item['title'] = item['title'][0]
                item['url'] = item['url'][0]
                items.append(item)
        for item in items:
            print item['title'].encode('utf8') if item['title'] else None
        print '============',len(items)
        return items

