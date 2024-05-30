import time

from base_case import BaseCase

from ui.fixtures import settings_page

import pytest


class TestSettingsPage(BaseCase):
    authorize = True
    
    @pytest.mark.skip
    def test_setting_redirect(self, settings_page):
        settings_page.click_settings_button()
    
    @pytest.mark.skip
    @pytest.mark.parametrize(
    'text, href',
        [
            ("Общие", "https://ads.vk.com/hq/settings"),
            ("Уведомления", "https://ads.vk.com/hq/settings/notifications"),
            ("Права доступа", "https://ads.vk.com/hq/settings/access"),
            ("История изменений", "https://ads.vk.com/hq/settings/logs")
        ]
    )
    
    @pytest.mark.skip
    def test_settings_pages(self, settings_page, text, href):
        settings_page.click_settings_button()
        
        settings_page.click_settings_item(text)
        
        assert self.is_opened(href)
    @pytest.mark.skip    
    @pytest.mark.parametrize(
    'phone, result',
        [
            ("89252583897", 0),
            ("79252583897", 0),
            ("+79252583897", 1),
        ]
    )

    @pytest.mark.skip
    def test_phone_field(self, settings_page, phone, result):
        settings_page.click_settings_button()
        settings_page.set_number(phone)
        
        assert settings_page.is_input_error() == result

    @pytest.mark.skip    
    def test_redirect_api_help(self, settings_page):
        settings_page.click_settings_button()
        
        settings_page.click_api_about()
        settings_page.go_to_new_tab()
        
        assert self.is_opened("https://ads.vk.com/help/articles/help_api")

    @pytest.mark.skip        
    def test_languege_change(self, settings_page):
        settings_page.click_settings_button()
        
        settings_page.change_languegue()
        
        settings_page.click_save()
        
        assert settings_page.is_input_error()
        
    @pytest.mark.skip
    @pytest.mark.parametrize(
    'email, result',
        [
            ("", None),
            ("aaa", None),
            ("a@a.ru", 1),
        ]
    )

    @pytest.mark.skip
    def test_add_email(self, settings_page, email, result):
        settings_page.click_settings_button()
        
        settings_page.click_add_email()
        
        settings_page.enter_email(email)
        
        assert settings_page.is_input_error() == result
    
    @pytest.mark.skip
    def test_my_target_popup(self, settings_page):
        settings_page.click_settings_button()
        
        settings_page.click_my_target()
        
        assert settings_page.is_popup_displayed() != None

    @pytest.mark.skip
    def test_telegram_redirect(self, settings_page):
        settings_page.click_settings_button()
        
        settings_page.click_settings_item("Уведомления")
        
        settings_page.click_telegram()
        
        settings_page.go_to_new_tab()
        
        assert self.is_opened('https://t.me/vkadssenderbot')
    
    @pytest.mark.skip
    def test_checkbox_update(self, settings_page):
        settings_page.click_settings_button()
        
        settings_page.click_checkbox_item("Финансы")
        settings_page.click_checkbox_item("Изменения в API")
        settings_page.click_checkbox_item("Мероприятия")
        settings_page.click_checkbox_item("Новости")
        
        settings_page.click_save()
        
        assert settings_page.is_input_error() == None
        