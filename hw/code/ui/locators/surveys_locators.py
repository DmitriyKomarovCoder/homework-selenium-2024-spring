from selenium.webdriver.common.by import By

class SurvaysLocators:
    SurveysMenuButton = (By.XPATH, f'//*[@data-testid="left-menu"and @data-entityid="leadads"]')
    SurveyTabLocator = (By.XPATH, f'//*[@data-testid="tabs-item" and contains(@id, "tab_surveys")]')

    CreateSurveyButton = (By.XPATH, f'//button[contains(@class, "Surveys_createButton__")]')

    SurveyTableStatusCell = (By.XPATH, f'//*[contains(@class, "BaseTable__header-cell") and @data-key="status"]')
    SurveyTableIdCell = (By.XPATH, f'//*[contains(@class, "BaseTable__header-cell") and @data-key="id"]')
    SurveyTableCreatedCell = (By.XPATH, f'//*[contains(@class, "BaseTable__header-cell") and @data-key="created"]')
    SurveyTableResponseCountCell = (By.XPATH, f'//*[contains(@class, "BaseTable__header-cell") and @data-key="respondents_count"]')
    SurveyTableListCell = (By.XPATH, f'//*[contains(@class, "BaseTable__header-cell") and @data-key="xlsx"]')
    SurveyTableNameCell = (By.XPATH, f'//*[contains(@class, "BaseTable__header-cell") and @data-key="name"]')

    SurveyFormNameInput = (By.XPATH, f'//input[@placeholder="Введите название"]')
    SurveyFormCompanyNameInput = (By.XPATH, f'//input[@placeholder="Введите название компании"]')
    SurveyFormHeaderInput = (By.XPATH, f'//input[@placeholder="Введите заголовок"]')
    SurveyFormDescriptionInput = (By.XPATH, f'//textarea[@placeholder="Введите описание опроса"]')

    @staticmethod
    def SurveyFormGradient(colorId: int):
        return By.XPATH, f'//div[contains(@class, "GradientSelector_round__") and @data-id={colorId}]'

    @staticmethod
    def SurveyFormCheckStyle(gradient_style):
        return By.XPATH, f"//div[contains(@class, LeadForm-module_gradient{gradient_style})]"

    SurveyLightButton = (By.XPATH, '//input[@value="light"]')
    SurveyDarkButton = (By.XPATH, '//input[@value="dark"]')

    SurveySetImage = (By.XPATH, f'//div[@data-testid="set-global-image"]')
    SurveyGetLogo = (By.XPATH, f'//div[contains(@class, "ImageItems_image__")]')
    SurveyChangeImage = (By.XPATH, f'//button[@data-testid="change-image"]')

    SurveyQuestionName = (By.XPATH, f'//textarea[@placeholder="Текст вопроса"]')
    SurveyQuestionAnswer = (By.XPATH, f'//input[@placeholder="Введите ответ"]')

    @staticmethod
    def SurveyWithName(name):
        return By.XPATH, f'//div[text()="{name}"]'

    SurveyButtonCountinue = (By.XPATH, f'//button[@data-testid="submit"]')
    SurveyButtonCancel = (By.XPATH, f'//button[@data-testid="cancel"]')

    SurveySort = (By.XPATH, f'//div[contains(@class, "BaseTable__sort-indicator--descending")]')

    SurveyRowIds = (By.XPATH, f'//div[contains(@class, "BaseTable__row-cell")][6]')

    @staticmethod
    def SurveyRowWithId(id):
        return By.XPATH, f'//div[@data-entityid="{id}"]'

    SurveyMoreButton = (By.XPATH, f'//button[@aria-label="More"]')
    SurveyMakeCopy = (By.XPATH, f'//label[@data-testid="dropdown-item"][2]')
    SurveyPreview = (By.XPATH, f'//label[@data-testid="dropdown-item"][3]')

    SurveyEditorHeader = (By.XPATH, f'//h2[text()="Редактирование опроса"]')

    StartSurvey = (By.XPATH, f'//button[//text()="Пройти опрос"]')

