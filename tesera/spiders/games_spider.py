# -*- coding: utf-8 -*-
import scrapy


class GamesSpider(scrapy.Spider):
    name = "games"

    start_urls = ['http://tesera.ru/games/all/%s/' % page for page in xrange(0,10)]

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
	    'player_number':  extract_with_xpath('//ul[@class="classnav"]/li[1]/text()'),
            'player_recomended':  extract_with_xpath('//ul[@class="classnav"]/li[2]/text()'),
            'time_learn':  extract_with_xpath('//ul[@class="classnav"]/li[4]/text()'),
            'time_game':  extract_with_xpath('//ul[@class="classnav"]/li[5]/text()'),
	    'rating_summ': extract_with_xpath('//div[@class="colright"]/div/h3/span/span/text()'),
	    'num_comments': extract_with_xpath('//div[@class="block comment"]//div[@class="numb"]/text()'),
            'num_news': extract_with_xpath('//div[@class="block news"]//div[@class="numb"]/text()'),
            'num_similar': extract_with_xpath('//div[@class="block similar"]//div[@class="numb"]/text()'),
	    'num_users_own': extract_with_xpath('//div[@class="smalltab-green smt"]//a[contains(text(), "владеют")]/../following-sibling::span/text()'),

	}


