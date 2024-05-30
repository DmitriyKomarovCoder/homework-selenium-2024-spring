from ui.pages.base_page import BasePage
from ui.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    locators = MainPageLocators()
    url = 'https://ads.vk.com/'

    def get_slide_title(self):
        return self.find(self.locators.SLIDER_TITLE)
    
    def change_slide(self):
        self.scroll_and_click(self.locators.NONACTIVE_CIRCLE)

    def click_get_all(self):
        self.scroll_and_click(self.locators.HREF_GET_ALL_COMPANY)
    
    def get_all_company(self):
        return self.find(self.locators.DIV_ALL_COMPANY)
    
    def get_title_text(self):
        return self.find(self.locators.CASE_TITLE).text
    
    def click_case_href(self):
        self.scroll_and_click(self.locators.CASE_HREF)

    def get_title_case_summary(self):
        return self.find(self.locators.CASE_SUMMARY_TITLE).text
   
    def click_more_info(self):
        self.scroll_and_click(self.locators.BUTTON_MORE_DETAILS)

    def find_text_offerContent(self):
        return self.find(self.locators.OFFER_CONTENT).text
    
    def find_text_summary_title(self):
        return self.find(self.locators.SUMMARY_TEXT).text