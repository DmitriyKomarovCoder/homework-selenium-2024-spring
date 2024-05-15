from base_case import BaseCase
from ui.fixtures import navbar_page
import pytest

class TestNavbarPage(BaseCase):
    authorize = False
    @pytest.mark.parametrize(
    'text, href',
        [
            ("Новости", "https://ads.vk.com/news"),
            ("Кейсы", "https://ads.vk.com/cases"),
            ("Форум идей", "https://ads.vk.com/upvote"),
            ("Справка", "https://ads.vk.com/help")
        ]
    )
    @pytest.mark.skip
    def test_navbar_href(self, navbar_page, text, href):
        navbar_page.click_navbar_item(text)
        assert self.is_opened(href)
