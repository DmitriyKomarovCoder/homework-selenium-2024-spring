from selenium.webdriver.common.by import By

class LeadPageLocators:
    BUTTON_CREATE = (By.XPATH, '//button[@test-id="create-leadform-button"]')
    DOWNLOAD_LOGO = (By.XPATH, '//div[@data-testid="set-global-image"]')
    GET_LOGO = (By.XPATH, '//div[contains(@class, "ImageItems_image__")]')
    CHANGE_IMAGE = (By.XPATH, '//button[@data-testid="change-image"]')

    @staticmethod
    def BUTTON_STYLE(style_id):
        return By.XPATH, f"//div[@data-id='{style_id}']" # 0-2-3-4-5-6-1
    
    @staticmethod
    def CHECK_STYLE(gradient_style):
        return By.XPATH, f"//div[contains(@class, LeadForm-module_gradient{gradient_style})]" # 0-2-3-4-5-6-1
    
    GET_PREVIEW_LIGHT = (By.XPATH, '//div[contains(@class, "vkui--vkBase--light")]')
    GET_PREVIEW_DARK = (By.XPATH, '//div[contains(@class, "vkui--vkBase--dark")]')

    GET_LEAD_FROM_DESKTOP = (By.XPATH, '//div[contains(@class, "CreateLeadFormModal_desktop__")]')

    INPUT_LIGHT_BUTTON = (By.XPATH, '//input[@value="light"]')
    INPUT_DARK_BUTTON = (By.XPATH, '//input[@value="dark"]')

    INPUT_MOBILE_BUTTON = (By.XPATH, '//input[@value="mobile"]')
    INPUT_NAME_LEAD_FORM = (By.XPATH, '//input[@placeholder="Название лид-формы"]')
    INPUT_NAME_COMPANY = (By.XPATH, '//input[@placeholder="Название компании"]')
    INPUT_TITLE = (By.XPATH, '//input[@placeholder="Текст заголовка"]')
    INPUT_DESCRIPTION = (By.XPATH, '//input[@placeholder="Краткое описание опроса"]') 

    BUTTON_CONTINUE = (By.XPATH, '//button[@data-testid="submit"]')
    BUTTON_CANCEL = (By.XPATH, '//button[@data-testid="cancel"]')

    BUTTON_ADD_CONTACT = (By.XPATH, '//button[contains(@class, "Questions_addContactFieldsBtn__")]')
    CHECKBOX_EMAIL = (By.XPATH, '//div[contains(@class, "AddContactsFieldsModal_checklist__")]//label[2]')
    ADD_BUTTON_CONTACT_INFO = (By.XPATH, '//div[contains(@class, "ModalManagerPage_footer__")]//button')
    FIND_EMAIL_CONTACT_INFO = (By.XPATH, '//input[@placeholder="Введите email"]')

    BUTTON_ADD_QUESTION = (By.XPATH, '//button[.//span[text()="Добавить вопрос"]]')

    QUESTION_TEXTAREA = (By.XPATH, '//textarea[contains(@class, "vkuiTextarea__")]')
    
    @staticmethod
    def TITLE_QUESTION(question_name):
        return By.XPATH, f"//h3[text()='{question_name}']"
    
    CONTACT_INFO_FIRST_NAME_DELETE = (By.XPATH, '//button[@aria-label="Delete" and @data-id="first_name"]')

    BUTTON_ADD_SITE = (By.XPATH, '//div[@data-testid="add-site-btn"]') 
    BUTTON_ADD_PHONE = (By.XPATH, '//div[@data-testid="add-phone-btn"]')
    BUTTON_ADD_PROMO_CODE = (By.XPATH, '//div[@data-testid="add-promo-code-btn"]')

    INPUT_SITE = (By.XPATH, '//div[@placeholder="Введите ссылку на сайт"]//span//input')
    INPUT_PHONE = (By.XPATH, '//input[@placeholder="+7......"]')
    INPUT_PROMOCODE = (By.XPATH, '//input[@placeholder="Введите промокод"]')

    LEAD_PHONE = (By.XPATH, '//a[contains(@href,"tel:")]')
    LEAD_SITE = (By.XPATH, '//a[@rel="noreferrer noopener"]')
    LEAD_PROMOCODE = (By.XPATH, '//button[@aria-label="Скопировать"]')

    NOTIFY_CHECKBOX_EMAIL = (By.XPATH, '//div[contains(@class, "vkuiCheckbox__icon--off")]')
    NOTIFY_EMAIL = (By.XPATH, '//input[@placeholder="email@example.com"]')

    INPUT_LAST_NAME = (By.XPATH, '//input[@placeholder="Введите фамилию, имя и отчество"]')
    INPUT_ADDRESS = (By.XPATH, '//input[@placeholder="Введите адрес"]')

    @staticmethod
    def NAME_LINK(name):
        return By.XPATH, f"//button[contains(@class, 'NameCell_link__') and text()='{name}']"
    
    INPUT_SEARCH = (By.XPATH, '//input[@data-testid="search"]')

    BUTTON_DELETE = (By.XPATH, '//div[contains(@class, "Nav_list")]//button[2]')
    FINALLY_DELETE = (By.XPATH, '//button[@data-testid="submit"]')

    BUTTON_EDIT = (By.XPATH, '//div[contains(@class, "Nav_list")]//button[1]')
    MODAL_HEADER_EDIT = (By.XPATH, '//h2[contains(@class, "ModalSidebarPage_title__")]')

    INPUT_DROP_DOWN = (By.XPATH, '//input[@aria-haspopup="listbox"]')