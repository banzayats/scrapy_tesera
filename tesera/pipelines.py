# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TeseraGamePipeline(object):
    def process_item(self, item, spider):
        if item['year']:
            item['year'] = item['year'].replace(u'\xa0', '')
            item['year'] = item['year'][-4:]
        return item
