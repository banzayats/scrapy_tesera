import scrapy


class GamesSpider(scrapy.Spider):
    name = "games"

    start_urls = ['http://tesera.ru/games/all/%s/' % page for page in xrange(0,100)]

    def parse(self, response):
        for game in response.css('div.game'):
	    yield {
		'title_rus': game.xpath('div[@class="game-left"]/h3/a/b/text()').extract_first(),
		'link': game.xpath('div[@class="game-left"]/h3/a/@href').extract_first(),
	    }

