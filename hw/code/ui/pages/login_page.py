import pytest
import os
from ui.locators.login_page_locators import LoginPageLocators
from ui.pages.base_page import BasePage
import time
from selenium.webdriver.common.keys import Keys

class LoginPage(BasePage):
    locators = LoginPageLocators()
    url = 'https://ads.vk.com/'
    
    def login(self, user, password):
        self.click(self.locators.HREF_LOGIN_PAGE, 5)
        self.click(self.locators.HREF_MAIL_LOGIN_PAGE, 5)
        login_input = self.find(self.locators.LOGIN_INPUT)
        # login_input.clear()
        login_input.send_keys(user)
        login_input.send_keys(Keys.ENTER)
        #self.click(self.locators.NEXT_BUTTON, 5)
        time.sleep(4)
        password_input = self.find(self.locators.PASSWORD_INPUT)
        # password_input.clear()
        password_input.send_keys(password)
        time.sleep(4)

        password_input.send_keys(Keys.ENTER)
        self.click(self.locators.SUBMIT_BUTTON, 5)        
