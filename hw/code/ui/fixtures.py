import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.navbar_page import NavbarPage
from ui.pages.pixel_page import PixelPage
from ui.pages.news_page import NewsPage
from ui.pages.settings_page import SettingsPage

from dotenv import load_dotenv
import os

@pytest.fixture()
def driver(config):
    browser = config['browser']
    url = config['url']
    selenoid = config['selenoid']
    vnc = config['vnc']
    options = Options()
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    if selenoid:
        capabilities = {
            'browserName': 'chrome',
            'version': '118.0',
        }
        if vnc:
            capabilities['enableVNC'] = True
        driver = webdriver.Remote(
            'http://127.0.0.1:4444/wd/hub',
            options=options,
            desired_capabilities=capabilities
        )
    elif browser == 'chrome':
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()

def get_driver(browser_name):
    if browser_name == 'chrome':
        browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser_name == 'firefox':
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise RuntimeError(f'Unsupported browser: "{browser_name}"')
    browser.maximize_window()
    return browser


@pytest.fixture(scope='session', params=['chrome', 'firefox'])
def all_drivers(config, request):
    url = config['url']
    browser = get_driver(request.param)
    browser.get(url)
    yield browser
    browser.quit()

@pytest.fixture(scope='session')
def credentials():
    load_dotenv()
    user = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    return user, password

@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def news_page(driver):
    return NewsPage(driver=driver)

@pytest.fixture
def settings_page(driver):
    return SettingsPage(driver=driver)

@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)

@pytest.fixture
def navbar_page(driver):
    driver.get(NavbarPage.url)
    return NavbarPage(driver=driver)

@pytest.fixture
def pixel_page(driver):
    driver.get(PixelPage.url)
    return PixelPage(driver=driver)

