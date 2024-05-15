from base_case import BaseCase
from ui.fixtures import pixel_page
from selenium.webdriver.common.keys import Keys
import pytest

class TestPixelPage(BaseCase):
    authorize = True
    
    NOT_CORRECT_DATA = "NOT CORRECT"
    CORRECT_DOMAIN = "https://example.com"
    UPDATE_DOMAIN = "Update"
    DELETE_DOMAIN_TEST = "https://delete_test.com"
    FIND_TEXT = "Нашли пиксели, привязанные к сайту"
    CREATE_PIXEL_ID = "Создан ID пикселя"
    NOTHING_PIXEL_TEXT = "Нет привязанных пикселей трекинга"
    SEARCH_TEXT = "Example Domain"
    NOTHING_FIND_TEXT = "Ничего не найдено"
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

    @pytest.mark.skip
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

        assert pixel_page.find_nothind_pixel_text() == self.NOTHING_PIXEL_TEXT
    
    @pytest.mark.skip
    def test_update_pixel_name(self, pixel_page):
        pixel_page.create_pixel(self.CORRECT_DOMAIN) 
        pixel_page.open_update_frame()

        input_update = pixel_page.input_update_name()
        input_update.clear()
        input_update.send_keys(self.UPDATE_DOMAIN)
        pixel_page.click_update()

        assert pixel_page.find_update_text() == self.UPDATE_DOMAIN
        pixel_page.click_close_pixel()
        pixel_page.delete_pixel()

    @pytest.mark.skip
    def test_search_nothing(self, pixel_page):
        pixel_page.create_pixel(self.CORRECT_DOMAIN)
        input_search = pixel_page.find_search_input()
        input_search.clear()
        input_search.send_keys(self.NOT_CORRECT_DATA)

        assert pixel_page.find_nothing_text() == self.NOTHING_FIND_TEXT
        pixel_page.delete_pixel()

    @pytest.mark.skip
    def test_search_correct(self, pixel_page):
        pixel_page.create_pixel(self.CORRECT_DOMAIN)
        input_search = pixel_page.find_search_input()
        input_search.clear()
        input_search.send_keys(self.SEARCH_TEXT)

        assert pixel_page.find_correct_text() == self.SEARCH_TEXT
        pixel_page.delete_pixel()