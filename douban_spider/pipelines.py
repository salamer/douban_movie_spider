# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import sys

reload(sys)
sys.setdefaultencoding('utf8')



class DoubanSpiderPipeline(object):
    def  __init__(self):
        self.file=codecs.open('douban_movie.json',mode='wb',encoding='utf-8')
    def process_item(self, item, spider):

#        block={"":""}
#        line=json.dumps(block)
        line='the list:'+'\n'
        for i in range(len(item['quote'])):
        	movie_name={"movie_name":str(item['movie_name'][2*i])+str([2*i+1])}
        	star={"start":item['star'][i]}
        	quote={"quote":item['quote'][i]}
        	line=line+json.dumps(movie_name,ensure_ascii=False)
        	line=line+json.dumps(star,ensure_ascii=False)
        	line=line+json.dumps(quote,ensure_ascii=False)+"\n"



        self.file.write(line)
        
    def close_spider(self,spider):
        self.file.close()
