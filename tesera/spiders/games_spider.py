# -*- coding: utf-8 -*-
import scrapy
import datetime
from tesera.items import GameItem

class GamesSpider(scrapy.Spider):
    name = "games"

    start_urls = ['http://tesera.ru/games/all/%s/' % page for page in xrange(0,1836)]

    def parse(self, response):
        # follow links to game pages
	hrefs = response.xpath('//div[@class="game-left"]/h3/a/@href').extract()
	for href in hrefs:
	    yield scrapy.Request(response.urljoin(href),
                                 callback=self.parse_game)

    def parse_game(self, response):

	def extract_with_xpath(query):
	    return response.xpath(query).extract_first()

        yield {
	    'title_main': extract_with_xpath('//*[@id="game_title"]/span/text()'),
            'year': extract_with_xpath('//div[@class="leftcol"]/h3/text()'),
	    'player_number':  extract_with_xpath('//ul[@class="classnav"]/li[1]/text()'),
            'player_recomended':  extract_with_xpath('//ul[@class="classnav"]/li[2]/text()'),
            'time_learn':  extract_with_xpath('//ul[@class="classnav"]/li[4]/text()'),
            'time_game':  extract_with_xpath('//ul[@class="classnav"]/li[5]/text()'),
	    'rating_summ': extract_with_xpath('//div[@class="colright"]/div/h3/span/span/text()'),
            'rating_users': extract_with_xpath('//div[@class="colright"]/div/table/tr[2]/td[3]/span/text()'),
            'rating_users_count': extract_with_xpath('//div[@class="colright"]//sub/text()'),
	    'num_comments': extract_with_xpath('//div[@class="block comment"]//div[@class="numb"]/text()'),
            'num_news': extract_with_xpath('//div[@class="block news"]//div[@class="numb"]/text()'),
	    'num_users_own': extract_with_xpath('//div[@class="smalltab-green smt"]//a[contains(@href, "owners")]/../following-sibling::span/text()'),
            'num_users_sell': extract_with_xpath('//div[@class="smalltab-green smt"]//a[contains(@href, "sellers")]/../following-sibling::span/text()'),
            'num_users_buy': extract_with_xpath('//div[@class="smalltab-green smt"]//a[contains(@href, "buyers")]/../following-sibling::span/text()'),
            'num_users_play': extract_with_xpath('//div[@class="smalltab-green smt"]//a[contains(@href, "players")]/../following-sibling::span/text()'),
            'num_users_want': extract_with_xpath('//div[@class="smalltab-green smt"]//a[contains(@href, "wanters")]/../following-sibling::span/text()'),
            'num_users_fans': extract_with_xpath('//div[@class="smalltab-orange smt"]//a[contains(@href, "fans")]/../following-sibling::span/text()'),
            'num_users_diaries': extract_with_xpath('//div[@class="smalltab-orange smt"]//a[contains(@href, "diaries")]/../following-sibling::span/text()'),
            'url': response.url,
            'date': datetime.datetime.now()
	}


