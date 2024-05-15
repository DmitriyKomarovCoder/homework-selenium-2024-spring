import time

from base_case import BaseCase

from hw.code.ui.fixtures import settings_page

import pytest


class TestSettingsPage(BaseCase):
    authorize = True

    def test_setting_redirect(self, settings_page):
        settings_page.click_settings_button()
        time.sleep(3)
