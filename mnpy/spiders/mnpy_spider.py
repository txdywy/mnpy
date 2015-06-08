from scrapy import Spider
from mnpy.items import MnpyItem

class MnpySpider(Spider):
    name, start_urls = 'mnpy', ['http://weekly.manong.io/issues/%s' % i for i in range(1,70)]

    def parse(self, response):
        tags = response.selector.xpath('//a')
        items = []
        for i in tags:
    	    item = MnpyItem()
            item['title'] = i.xpath('text()').extract()
            item['url'] = i.xpath('@href').extract()
            if item['title'] and 'python' in item['title'][0].lower():
                items.append(item)
        for item in items:
            print item['title'][0].encode('utf8') if item['title'] else None
        print '============',len(items)
        return items

