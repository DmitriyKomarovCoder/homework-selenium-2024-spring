import time

from ui.pages.base_page import BasePage
from ui.locators.ads_locators import NewsPageLocators


class NewsPage(BasePage):
    locators = NewsPageLocators()
    url = 'https://ads.vk.com/'

    def click_navbar_news(self):
        self.click(self.locators.nav_bar_news())

    def get_article_time(self):
        time_el = self.find(self.locators.article_time())
        return time_el.get_attribute("datetime")

    def open_article(self):
        self.click(self.locators.get_article())

    def get_time_slice(self):
        return self.finds(self.locators.article_time())

    def get_articles(self):
        return self.finds(self.locators.get_article())

    def open_lk(self):
        self.scroll()
        self.click(self.locators.lk_button())
        time.sleep(4)
