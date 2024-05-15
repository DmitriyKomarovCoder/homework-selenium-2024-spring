import time

from base_case import BaseCase

from hw.code.ui.fixtures import news_page

import pytest


class TestNewsPage(BaseCase):
    authorize = False

    def test_redirect_on_news(self, news_page):
        news_page.click_navbar_news()
        time.sleep(3)
        assert self.is_opened('https://ads.vk.com/news')

    def test_first_article_latest(self, news_page):
        news_page.click_navbar_news()
        article_time = news_page.get_article_time()
        news_page.open_article()
        assert article_time == news_page.get_article_time()

    def test_articles_time_range_asc(self, news_page):
        news_page.click_navbar_news()
        published = news_page.get_time_slice()

        assert all(published[i] <= published[i+1] for i in range(len(published) - 1))

    def test_article_redirect_to_lk(self, news_page):
        news_page.click_navbar_news()
        news_page.open_article()

        news_page.open_lk()
        news_page.go_to_new_tab()

        assert self.is_opened('https://id.vk.com/auth?')
