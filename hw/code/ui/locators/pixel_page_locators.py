from selenium.webdriver.common.by import By

class PixelPageLocators:
    PIXEL_HREF = (By.XPATH, '//a[contains(@href="/hq/pixels")]')
    ADD_PIXEL_BUTTON = (By.XPATH, "//button[contains(@class, 'vkuiButton')]")
    ADD_PIXEL_TEXT = (By.XPATH, '//*[text()="Добавление пикселя"]')
    MODEL_PIXEL_FRAME = (By.XPATH, '//div[contains(@class, "vkui__portal-root")]')
    INPUT_DOMAIN_SYTE = (By.XPATH, '//input[@placeholder="Домен сайта"]')
    BUTTON_IFRAME_PIXEL = (By.XPATH, '//div[contains(@class, "vkuiButtonGroup")]/button')
    ERROR_PIXEL_MESSAGE = (By.XPATH, "//span[text()='Введите корректный адрес сайта (вида: example.ru)']")
    FIND_PIXEL_MESSAGE = (By.XPATH, "//div[contains(@class, 'FlowSelectStep_header__')]")
    INPUT_PIXEL_ID = (By.XPATH, "//input[@value='domain']")
    
    INPUT_ID_PIXEL = (By.XPATH, '//input[@placeholder="ID пикселя"]')
    INPUT_EMAIL = (By.XPATH, '//input[@placeholder="Email владельца"]')

    BUTTON_CREATE_PIXEL = (By.XPATH, "//span[text()='Создать новый пиксель']")
    CREATE_ID_PIXEL_TEXT = (By.XPATH, '//h2[text()="Создан ID пикселя"]')
    CLOSE_FRAME = (By.XPATH, '//div[@aria-label="Закрыть"]')

    BUTTON_MORE = (By.XPATH, '//button[@aria-label="More"]')
    TABLE_DOMAIN_ELEMENT = (By.XPATH, "//div[contains(@class, 'BaseTable__row-cell') and contains(@style, 'width: 50px')]")
    BUTTON_DELETE_DROPDOWN = (By.XPATH, '//div[contains(@class, "ContextMenu_dropdown__")]//label[last()]')
    BUTTON_UPDATE_DROPDOWN = (By.XPATH, '//div[contains(@class, "ContextMenu_dropdown__")]//label[1]')
    BUTTON_DELETE = (By.XPATH, '//div[contains(@class, "vkuiButtonGroup")]//button[last()]')
    BUTTON_UPDATE = (By.XPATH, '//button[@data-testid="submit"]')
    BUTTON_INPUT_UPDATE = (By.XPATH, '//input[@name="name"]')
    UPDATE_TEXT = (By.XPATH, '//div[@class="vkuiSimpleCell__content"]//span')
    NOTHING_PIXEL_TEXT = (By.XPATH, '//h2[text()="Нет привязанных пикселей трекинга"]')
    NOTHING_FIND_TEXT = (By.XPATH, '//h2[text()="Ничего не найдено"]')
    FIND_TEXT = (By.XPATH, '//h2[text()="Example Domain"]')
    INPUT_SEARCH = (By.XPATH, '//input[@placeholder="Поиск"]')