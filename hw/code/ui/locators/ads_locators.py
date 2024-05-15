from selenium.webdriver.common.by import By


class NewsPageLocators():
    @staticmethod
    def nav_bar_news():
        return By.XPATH, f"//*[contains(@class, 'NavigationVKAdsItem_link__') and text()='Новости']"

    @staticmethod
    def article_time():
        return By.XPATH, f'//time[@itemprop="datePublished"]'

    @staticmethod
    def get_article():
        return By.XPATH, f'(//div[contains(@class, "pages_gridRow__")])'

    @staticmethod
    def lk_button():
        return By.XPATH,  f"//a[contains(@class, 'vkuiButton')]"

class LoginPageLocators:
    HREF_LOGIN_PAGE = (By.XPATH, "//a[contains(@class, 'ButtonCabinet_primary__')]")
    HREF_MAIL_LOGIN_PAGE = (By.XPATH, '//button[@data-test-id="oAuthService_mail_ru"]')
    LOGIN_INPUT = (By.XPATH, '//input[@name="username"]')
    NEXT_BUTTON = (By.XPATH, '//button[@data-test-id="next-button"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="password"]')
    SUBMIT_BUTTON = (By.XPATH, '//button[@data-test-id="submit-button"]')

class SettingsPageLocators():
    @staticmethod
    def settings_button():
        return By.XPATH, f'//a[@data-entityid="settings"]'
    
    @staticmethod
    def settings_href(item_text):
        return By.XPATH, f'//div[contains(@id, "tab-settings")]//span[text()="{item_text}"]'
    
    @staticmethod
    def phone_field():
        return By.XPATH, f'//input[@data-testid="general-phone"]'
    
    @staticmethod
    def input_error():
        return By.XPATH, f'//span[@role="alert"]'
    
    @staticmethod
    def api_about_link():
        return By.XPATH, f'//a[contains(@class, "vkuiLink")]'
    
    @staticmethod
    def lang_changer():
        return By.XPATH, f'//div[contains(@class, "vkuiCustomSelect")]'
    
    @staticmethod
    def subbmit_button():
        return By.XPATH, f'//button[@data-testid="settings-save"]'
    
    @staticmethod
    def add_email():
        return By.XPATH, f'//*[contains(@class, "vkuiSimpleCell")]//*[text()="Добавить email"]'
    
    @staticmethod
    def email_input():
        return By.XPATH, f'//*[@data-testid="email-0"]'
    
    @staticmethod
    def my_taget_button():
        return By.XPATH, f'//*[contains(@class, "vkuiSimpleCell")]//*[text()="Привязать кабинет myTarget"]'
    
    @staticmethod
    def button_import_countinue():
        return By.XPATH, f'//button[@data-testid="import-continue"]'
