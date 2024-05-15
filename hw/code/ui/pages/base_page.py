import time

import allure

from ui.locators import basic_locators

from selenium.webdriver.remote.webelement import WebElement

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# from ui.locators.base_page_locators import BasePageLocators

class PageNotOpenedException(Exception):
    pass

class BasePage(object):
    url = 'https://ads.vk.com/'

    def is_opened(self, timeout=15):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
                return True
        raise PageNotOpenedException(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def finds(self, locator, timeout=None):
        return self.wait(timeout).until(EC.visibility_of_all_elements_located(locator))

    @allure.step('Search')
    def search(self, query):
        elem = self.find(self.locators.QUERY_LOCATOR_ID)
        elem.send_keys(query)
        go_button = self.find(self.locators.GO_BUTTON_LOCATOR)
        go_button.click()
        self.my_assert()

    @allure.step("Step 1")
    def my_assert(self):
        assert 1 == 1


    @allure.step('Click')
    def click(self, locator, timeout=None) -> WebElement:
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()


    def scroll(self):
        actions = ActionChains(self.driver, duration=500)
        actions.send_keys(Keys.END).perform()

    def go_to_new_tab(self):
        handles = self.driver.window_handles
        assert len(handles) > 1
        self.driver.switch_to.window(handles[1])
       
    def scroll_and_click(self, locator, timeout=None) -> WebElement:
        elem = self.wait(timeout).until(EC.presence_of_element_located(locator))
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()
    
    # def hover_elem(self, locator):
    #     elem = self.find(locator)
    #     ActionChains(self.driver).move_to_element(elem).perform()
    
    # def hover_elem_center(self, locator):
    #     elem = self.find(locator)
    #     size = elem.size
    #     width, height = size['width'], size['height']
    #     ActionChains(self.driver).move_to_element_with_offset(elem, width / 2, height / 2).perform()
