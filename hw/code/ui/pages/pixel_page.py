from ui.pages.base_page import BasePage
from ui.locators.pixel_page_locators import PixelPageLocators

class PixelPage(BasePage):
    locators = PixelPageLocators()
    url = 'https://ads.vk.com/hq/pixels'
    
    def click_add_pixel(self):
        self.click(self.locators.ADD_PIXEL_BUTTON)
    
    def find_add_pixel_text(self):
        return self.find(self.locators.ADD_PIXEL_TEXT).text

    def get_input_domain_site(self):
        return self.find(self.locators.INPUT_DOMAIN_SYTE)
    
    def get_message_error(self): 
        return self.find(self.locators.ERROR_PIXEL_MESSAGE).text
    
    def click_button_frame(self):
        self.click(self.locators.BUTTON_IFRAME_PIXEL, 5)
    
    def find_pixel_find_text(self):
        return self.find(self.locators.FIND_PIXEL_MESSAGE).text
    
    def find_input_pixelID(self):
        return self.find(self.locators.INPUT_PIXEL_ID)

    def find_input_email(self):
        return self.find(self.locators.INPUT_EMAIL, 3)

    def find_input_pixel_id(self):
        return self.find(self.locators.INPUT_ID_PIXEL)
    
    def click_button_create_pixel(self):
        self.click(self.locators.BUTTON_CREATE_PIXEL)
    
    def find_text_create_ID_pixel(self):
        return self.find(self.locators.CREATE_ID_PIXEL_TEXT).text
    
    def click_close_pixel(self):
        self.click(self.locators.CLOSE_FRAME)

    def click_more(self):
        self.click(self.locators.BUTTON_MORE)

    def open_delete_frame(self):
        self.scroll_and_click(self.locators.BUTTON_MORE)
        self.click(self.locators.BUTTON_DELETE_DROPDOWN)

    def click_delete(self):
        self.click(self.locators.BUTTON_DELETE)

    def create_pixel(self, domain_name):
        self.click_add_pixel()
        
        input_domen_syte = self.get_input_domain_site()
        input_domen_syte.clear()
        input_domen_syte.send_keys(domain_name)
        
        self.click_button_frame()
        self.click_button_create_pixel()
        self.click_close_pixel()

    def delete_pixel(self):
        self.open_delete_frame()
        self.click_delete()

    def find_domain(self, domain_name):
        return self.locators.find_element(domain_name)