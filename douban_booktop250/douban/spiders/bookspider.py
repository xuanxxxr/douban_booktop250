# -*- coding:utf-8 -*-
import scrapy
from douban.items import DoubanItem 
class BookSpider(scrapy.Spider):
	name = 'douban'
	allowed_domains = ['douban.com']
	start_urls = []
	for i in range(0,250,25):
		start_urls.append('https://book.douban.com/top250?start='+str(i))

	def parse(self,response):

		yield scrapy.Request(response.url, callback=self.parse_next)


	def parse_next(self, response):
		for item in response.xpath('//*[@id="content"]/div/div[1]'):
			book = DoubanItem()
			book['name'] = item.xpath('td[2]/div[1]/a/@title').extract()[0]
			book['price'] = item.xpath('td[2]/p/text()').extract()[0]
			book['ratings'] = item.xpath('td[2]/div[2]/span[2]/text()').extract()[0]
			yield book

