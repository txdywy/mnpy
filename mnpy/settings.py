# -*- coding: utf-8 -*-

# Scrapy settings for mnpy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'mnpy'

SPIDER_MODULES = ['mnpy.spiders']
NEWSPIDER_MODULE = 'mnpy.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36'

ITEM_PIPELINES = {
    'mnpy.pipelines.MnpyPipeline': 300,
}
