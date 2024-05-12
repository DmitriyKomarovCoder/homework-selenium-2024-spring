from base_case import BaseCase
from ui.fixtures import main_page
import pytest

class TestMainPage(BaseCase):
    authorize = True
    # @pytest.mark.skip
    def test_slide_click(self, main_page):
        initial_title = main_page.get_slide_title()
        main_page.change_slide()
        assert initial_title != main_page.get_slide_title()
    
    @pytest.mark.skip
    def test_case_company_get_all(self, main_page):
        main_page.click_get_all()
        assert self.is_opened("https://ads.vk.com/cases")

    @pytest.mark.skip
    def test_case_company(self, main_page):
        case_title = main_page.get_title_text()
        main_page.click_case_href()
        case_summary = main_page.get_title_case_summary()
        assert case_title == case_summary
    
    @pytest.mark.skip
    def test_webinar(self, main_page):
        main_page.click_more_info()
        assert self.is_opened("https://ads.vk.com/events")