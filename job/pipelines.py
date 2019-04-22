# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings


# 处理爬出以后的数据
class JobPipelineMongodb(object):
    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        db = settings['MONGODB_DBNAME']
        self.client = pymongo.MongoClient(host=host, port=port)
        tdb = self.client[db]
        self.post = tdb[settings['MONGODB_DOCNAME']]

    def process_item(self, item, spider):
        info = dict(item)
        self.post.insert(info)
        return item

    def close_spider(self, spider):
        self.client.close()
