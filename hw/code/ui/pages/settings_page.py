import time

from hw.code.ui.pages.base_page import BasePage
from hw.code.ui.locators.ads_locators import SettingsPageLocators


class SettingsPage(BasePage):
    locators = SettingsPageLocators()
    url = 'https://ads.vk.com/hq/settings'

    def click_settings_button(self):
        self.click(self.locators.settings_button(), 5)
