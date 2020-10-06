from selenium.webdriver.common.by import By


class KronaLoginPageLocators:
    INPUT_LOGIN = (By.CSS_SELECTOR, '#username')
    INPUT_PASSWORD = (By.CSS_SELECTOR, '#password.form-control')
    REMEMBER_ME = (By.CSS_SELECTOR, '#remember-me')
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[type='submit'].btn.btn-primary")
    RESET_PASSWORD_BUTTON = (By.CSS_SELECTOR, 'a.btn.btn-primary')


class KronaMainPageLocators:
    USERNAME = (By.XPATH, "//div[contains(@class, 'Menu_username_')]")


class KronaCountryPropertyReportsLocators:
    MENU_COUNTRY_PROPERTY = (By.CSS_SELECTOR, '#country_property_reports')
    DATA_TABLE = (By.CSS_SELECTOR, '.display.dataTable')
    REPORT_NUMBER = (By.CSS_SELECTOR, '#reportNumber')
    SHOW_TABLE = (By.CSS_SELECTOR, '#reportListDataTableSubmitButton.btn')
    RESULT_TABLE_PROCESSING = (By.XPATH, "//div[@id='result_table_processing'][contains(@style, 'display: none')]")
    REPORT_IN_THE_REGISTRY_AFTER_FILTERING = (By.CSS_SELECTOR, '.sorting_1 a')


class KronaCountryPropertyReportCardPageLocators:
    REPORT_STATUS = (By.CSS_SELECTOR, '#reportStatus')
    FLAG_FOR_STANDARD = (By.CSS_SELECTOR, '#isStandardReport')
    GENERAL_INFORMATION_TAB = (
        By.XPATH, "//button[contains(@class, 'tablinks')][contains(text(), 'Общая информация')]")
    FIRST_OBJECT_TAB = (By.XPATH, "//button[contains(@class, 'tablinks')][contains(text(), 'Объект 1')]")
    SECOND_OBJECT_TAB = (By.XPATH, "//button[contains(@class, 'tablinks')][contains(text(), 'Объект 2')]")
    DOCUMENTS_TAB = (By.XPATH, "//button[contains(@class, 'tablinks')][contains(text(), 'Документы')]")
    PHOTOS_TAB = (By.XPATH, "//button[contains(@class, 'tablinks')][contains(text(), 'Фотографии')]")
    VERIFICATION_TAB = (By.XPATH, "//button[contains(@class, 'tablinks')][contains(text(), 'Верификация')]")
    BUTTON_FOR_ATTACH_EXPERT_CALCULATION = (By.CSS_SELECTOR, "[title='file input']")
    PROGRESS_BAR_FINISHED_DOWNLOADING = (By.XPATH, "//div[@aria-valuenow='100']")
    INPUT_PRICE_FOR_FIRST_OBJECT = (By.CSS_SELECTOR, "[name='verifiedObjects[0].price']")
    INPUT_PRICE_FOR_SECOND_OBJECT = (By.CSS_SELECTOR, "[name='verifiedObjects[1].price']")
    LACK_DOCUMENTS = (By.CSS_SELECTOR, "#lackDocuments")
    VERIFICATION_BUTTON = (By.CSS_SELECTOR, "#btnSend.btn.btn-primary")
    RESULT = (By.XPATH, "//td[contains(text(), 'Принято')]")
    DECISION_BUTTON = (By.XPATH, "//a[contains(text(), 'Решение')]")
