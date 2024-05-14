from ui.pages.base_page import BasePage
from ui.locators.ads_locators import NewsPageLocators

class NewsPage(BasePage):
    locators = NewsPageLocators()
    url = 'https://ads.vk.com/'

    def click_navbar_news(self):
        self.click(self.locators.NAVBAR_HREF())
    
    def click_article(self):
        self.click(self.locators)