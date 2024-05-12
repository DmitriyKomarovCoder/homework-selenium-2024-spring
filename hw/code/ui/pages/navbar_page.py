from ui.pages.base_page import BasePage
from ui.locators.navbar_locators import NavbarPageLocators

class NavbarPage(BasePage):
    locators = NavbarPageLocators()
    url = 'https://ads.vk.com/'

    def click_navbar_item(self, item_text):
        self.click(self.locators.NAVBAR_HREF(item_text))