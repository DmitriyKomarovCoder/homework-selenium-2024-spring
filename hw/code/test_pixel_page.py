from base_case import BaseCase
from ui.fixtures import pixel_page
from selenium.webdriver.common.keys import Keys
import pytest

class TestPixelPage(BaseCase):
    authorize = True
    
    NOT_CORRECT_DATA = "NOT CORRECT"
    CORRECT_DOMAIN = "https://example.com"
    DELETE_DOMAIN_TEST = "https://delete_test.com"
    FIND_TEXT = "Нашли пиксели, привязанные к сайту"
    CREATE_PIXEL_ID = "Создан ID пикселя"

    @pytest.mark.skip
    def test_open_pixel_form(self, pixel_page):
        pixel_page.click_add_pixel()
        text_add_pixel = pixel_page.find_add_pixel_text()
        assert text_add_pixel != None
    
    @pytest.mark.skip
    def test_not_correct_data(self, pixel_page):
        pixel_page.click_add_pixel()

        input_domen_syte = pixel_page.get_input_domain_site()
        input_domen_syte.clear()
        input_domen_syte.send_keys(self.NOT_CORRECT_DATA)
        
        pixel_page.click_button_frame()

        error_text = pixel_page.get_message_error()
        assert error_text == 'Введите корректный адрес сайта (вида: example.ru)'
    
    @pytest.mark.skip
    def test_correct_data(self, pixel_page):
        pixel_page.click_add_pixel()
        
        input_domen_syte = pixel_page.get_input_domain_site()
        input_domen_syte.clear()
        input_domen_syte.send_keys(self.CORRECT_DOMAIN)
        
        pixel_page.click_button_frame()

        find_text = pixel_page.find_pixel_find_text()

        assert find_text == self.FIND_TEXT

    @pytest.mark.skip
    def test_id_pixel(self, pixel_page):
        pixel_page.click_add_pixel()

        button = pixel_page.find_input_pixelID()

        button.send_keys(Keys.RIGHT)
        assert pixel_page.find_input_email() != None
        assert pixel_page.find_input_pixel_id() != None

    
    def test_correct_data(self, pixel_page):
        pixel_page.click_add_pixel()
        
        input_domen_syte = pixel_page.get_input_domain_site()
        input_domen_syte.clear()
        input_domen_syte.send_keys(self.CORRECT_DOMAIN)
        
        pixel_page.click_button_frame()
        pixel_page.click_button_create_pixel()
        assert pixel_page.find_text_create_ID_pixel().startswith(self.CREATE_PIXEL_ID)
        pixel_page.click_close_pixel()
        pixel_page.delete_pixel()
    
    @pytest.mark.skip
    def test_delete_pixel(self, pixel_page):
        pixel_page.create_pixel(self.DELETE_DOMAIN_TEST)
        pixel_page.open_delete_frame()
        pixel_page.click_delete()
        assert pixel_page.find_domain(self.DELETE_DOMAIN_TEST) == None