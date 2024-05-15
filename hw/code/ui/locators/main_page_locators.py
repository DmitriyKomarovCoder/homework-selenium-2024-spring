from selenium.webdriver.common.by import By

class MainPageLocators:
    SLIDER_TITLE = (By.XPATH, "//*[contains(@class, 'MainSlider_active__')]//p")
    NONACTIVE_CIRCLE = (By.XPATH, "//*[contains(@class, 'Bullets_box__')]")
    HREF_GET_ALL_COMPANY = (By.XPATH, "//a[contains(@class, 'styles_all')]")
    DIV_ALL_COMPANY = (By.XPATH, "//div[contains(@class, 'Case_content__')]")
    CASE_TITLE = (By.XPATH, "//div[contains(@class, 'Case_title__')]")
    CASE_HREF = (By.XPATH, "//a[contains(@class, 'Case_link__')]")
    CASE_SUMMARY_TITLE = (By.XPATH, "//h1[contains(@class, 'Summary_title__')]")
    BUTTON_MORE_DETAILS = (By.XPATH, "//*[contains(@class, 'GetStarted_button__')]")