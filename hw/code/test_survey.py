from base_case import BaseCase

import time

from ui.fixtures import survey_page

import pytest


def is_sorted_increasing(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

class TestSurveyPage(BaseCase):
    authorize = True

    def test_survey_page(self, survey_page):
        assert self.is_opened("https://ads.vk.com/hq/leadads/surveys")

        assert survey_page.find_status_cell() is not None
        assert survey_page.find_id_cell() is not None
        assert survey_page.find_name_cell() is not None
        assert survey_page.find_list_cell() is not None
        assert survey_page.find_count_cell() is not None
        assert survey_page.find_created_cell() is not None

    @pytest.mark.parametrize(
        'name',
        ["Общие", "comp", "grisha", "2"]
    )
    def test_create_survey(self, survey_page, name):
        survey_page.create_survey(name)
        assert survey_page.find_survey_with_name(name) is not None

    def test_sort_survey(self, survey_page):
        ids = survey_page.get_id_slice()

        if survey_page.is_decreasing():
            assert is_sorted_increasing(ids) is not True
        else:
            assert is_sorted_increasing(ids) is True

        survey_page.click_id_cell()

        ids_back = survey_page.get_id_slice()

        if survey_page.is_decreasing():
            assert is_sorted_increasing(ids_back) is not True
        else:
            assert is_sorted_increasing(ids_back) is True

    def test_editor_opened(self, survey_page):
        survey_page.click_survey()

        assert survey_page.find_editor_header() is not None


    def test_copy(self, survey_page):
        ids = survey_page.get_id_slice()
        ## Copy test
        survey_page.make_copy(ids[0])
        assert survey_page.find_survey_with_name(" (копия)") is not None


    def test_preview(self, survey_page):
        ids = survey_page.get_id_slice()
        survey_page.make_preview(ids[0])

        assert survey_page.is_preview()
