import pytest
from _pytest.fixtures import FixtureRequest
from ui.pages.base_page import PageNotOpenedExeption
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from ui.pages.login_page import LoginPage
from dotenv import load_dotenv
import os

class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)
        if self.authorize:
            user, password = request.getfixturevalue('credentials')
            self.login_page.login(user, password)

    def is_opened(self, url, timeout=None):
        if timeout is None:
            timeout = 5

        try:
            WebDriverWait(self.driver, timeout).until(EC.url_matches(url))
            return True
        except:
            raise PageNotOpenedException(
                f'{url} did not open in {timeout} sec, current url {self.driver.current_url}')