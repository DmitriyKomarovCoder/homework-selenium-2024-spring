import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.navbar_page import NavbarPage
# from ui.pages.settings_page import SettingsPage
from dotenv import load_dotenv
import os


@pytest.fixture()
def driver(config):
    browser = config['browser']
    url = config['url']
    selenoid = config['selenoid']
    vnc = config['vnc']
    options = Options()
    # options = webdriver.ChromeOptions()
    # options.add_argument("--window-size=1920,1080")
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
        driver = webdriver.Chrome()
        
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()

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
def main_page(driver):
    return MainPage(driver=driver)

@pytest.fixture
def navbar_page(driver):
    driver.get(NavbarPage.url)
    return NavbarPage(driver=driver)

