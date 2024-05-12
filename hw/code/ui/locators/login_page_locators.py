from selenium.webdriver.common.by import By

class LoginPageLocators:
    HREF_LOGIN_PAGE = (By.XPATH, "//a[contains(@class, 'ButtonCabinet_primary__')]")
    HREF_MAIL_LOGIN_PAGE = (By.XPATH, '//button[@data-test-id="oAuthService_mail_ru"]')
    LOGIN_INPUT = (By.XPATH, '//input[@name="username"]')
    NEXT_BUTTON = (By.XPATH, '//button[@data-test-id="next-button"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="password"]')
    SUBMIT_BUTTON = (By.XPATH, '//button[@data-test-id="submit-button"]')