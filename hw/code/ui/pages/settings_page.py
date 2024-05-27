import time

from selenium.webdriver.common.keys import Keys

from ui.pages.base_page import BasePage
from ui.locators.ads_locators import SettingsPageLocators


class SettingsPage(BasePage):
    locators = SettingsPageLocators()
    url = 'https://ads.vk.com/hq/settings'

    def click_settings_button(self):
        self.click(self.locators.settings_button(), 5)
        
    def click_settings_item(self, item_text):
        self.click(self.locators.settings_href(item_text))
    
    def set_number(self, phone):
        input = self.find(self.locators.phone_field())
        
        input.send_keys(phone)
        input.send_keys(Keys.ENTER)
    
    def is_input_error(self):
        return self.find(self.locators.input_error())
    
    def click_api_about(self):
        self.click(self.locators.api_about_link())
    
    def change_languegue(self):
        lang_changer_el = self.find(self.locators.lang_changer())
        
        lang_changer_el.send_keys(Keys.ENTER)
        lang_changer_el.send_keys(Keys.ARROW_DOWN)
        lang_changer_el.send_keys(Keys.ARROW_DOWN)
        lang_changer_el.send_keys(Keys.ENTER)
    
    def click_save(self):
        self.click(self.locators.subbmit_button())
    
    def click_my_target(self):
        self.click(self.locators.my_taget_button())
    
    def is_popup_displayed(self):
        return self.find(self.locators.button_import_countinue())
    
    def click_telegram(self):
        self.click(self.locators.telegram_button())