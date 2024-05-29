from ui.pages.base_page import BasePage
from ui.locators.surveys_locators import SurvaysLocators

import time


class SurveyPage(BasePage):
    locators = SurvaysLocators()
    url = 'https://ads.vk.com/hq/leadads/surveys'

    def find_status_cell(self):
        return self.find(self.locators.SurveyTableStatusCell)

    def find_id_cell(self):
        return self.find(self.locators.SurveyTableIdCell)

    def click_id_cell(self):
        return self.click(self.locators.SurveyTableIdCell)

    def find_created_cell(self):
        return self.find(self.locators.SurveyTableCreatedCell)

    def find_count_cell(self):
        return self.find(self.locators.SurveyTableResponseCountCell)

    def find_list_cell(self):
        return self.find(self.locators.SurveyTableListCell)

    def find_name_cell(self):
        return self.find(self.locators.SurveyTableNameCell)

    def click_create_survey(self):
        self.click(self.locators.CreateSurveyButton, 5)

    def set_logo(self):
        self.click(self.locators.SurveySetImage, 3)
        self.click(self.locators.SurveyGetLogo, 3)

    def find_replace(self):
        return self.find(self.locators.SurveyChangeImage, 7)

    def change_style(self, item):
        self.click(self.locators.SurveyFormGradient(item))

    def find_style(self, item):
        return self.find(self.locators.SurveyFormCheckStyle(item))

    def click_continue(self):
        self.click(self.locators.SurveyButtonCountinue)

    def survey_start_page(self, name):
        self.set_logo()
        survey_name = self.find(self.locators.SurveyFormNameInput)

        survey_name.clear()
        survey_name.send_keys(name)

        survey_name_company = self.find(self.locators.SurveyFormCompanyNameInput)
        survey_name_company.send_keys(name)

        survey_title = self.find(self.locators.SurveyFormHeaderInput)
        survey_title.send_keys(name)

        survey_description = self.find(self.locators.SurveyFormDescriptionInput)
        survey_description.send_keys(name)
        self.find_replace()
        self.click_continue()

    def add_question(self, q_name, q_ans):
        qa_name = self.find(self.locators.SurveyQuestionName)

        qa_name.clear()
        qa_name.send_keys(q_name)

        qa_ans = self.finds(self.locators.SurveyQuestionAnswer)

        for ans in qa_ans:
            ans.clear()
            ans.send_keys(q_ans)

    def create_survey(self, name_lead):
        # Оформление
        self.click_create_survey()
        self.survey_start_page(name_lead)

        # Вопросы
        self.add_question(1, 1)

        self.click_continue()

        # Результаты
        self.click_continue()

    def find_survey_with_name(self, name):
        return self.find(self.locators.SurveyWithName(name))

    def get_id_slice(self):
        arr = []
        items = self.finds(self.locators.SurveyRowIds)
        for it in items:
            arr.append(it.text)
        return [int(x) for x in arr]

    def is_decreasing(self):
        return self.find(self.locators.SurveySort) is not None

    def click_survey(self, e_id):
        self.click(self.locators.SurveyRowWithId(e_id))

    def make_copy(self, e_id):
        self.hover_elem(self.locators.SurveyRowWithId(e_id))
        self.hover_elem(self.locators.SurveyMoreButton)
        self.click(self.locators.SurveyMakeCopy)

    def make_preview(self, e_id):
        self.hover_elem(self.locators.SurveyRowWithId(e_id))
        self.hover_elem(self.locators.SurveyMoreButton)
        self.click(self.locators.SurveyPreview)

    def is_preview(self):
        self.go_to_new_tab()
        return self.find(self.locators.StartSurvey) is not None

    def find_editor_header(self):
        return self.find(self.locators.SurveyEditorHeader)
