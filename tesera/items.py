# -*- coding: utf-8 -*-

from scrapy.item import Item, Field


class GameItem(Item):
    title_main = Field()
    year = Field()
    player_number = Field()
    player_recomended = Field()
    time_learn = Field()
    time_game = Field()
    rating_summ = Field()
    rating_users = Field()
    rating_users_count = Field()
    num_comments = Field()
    num_news = Field()
    num_users_own = Field()
    num_users_sell = Field()
    num_users_buy = Field()
    num_users_play = Field()
    num_users_want = Field()
    num_users_fans = Field()
    num_users_diaries = Field()

    # Housekeeping fields
    url = Field()
    date = Field()
