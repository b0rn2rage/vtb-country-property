from selenium.webdriver.common.by import By


class BaLoginPageLocators:
    INPUT_EMAIL = (By.CSS_SELECTOR, '.email.input_login-form')
    INPUT_PASSWORD = (By.CSS_SELECTOR, '.input_login-form#authPassword')
    FACEBOOK_POPUP = (By.CSS_SELECTOR, '.facebook-popup-img')
    CLOSE_FACEBOOK_POPUP = (By.CSS_SELECTOR, '.close.facebook-popup-close')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.login-form-btn#login')


class BaMainPageLocators:
    GOST_POPUP = (By.CSS_SELECTOR, '#gost-popup-modal')
    CLOSE_GOST_POPUP = (By.CSS_SELECTOR, "#gost-popup-modal .modal-header button.close")
    SIMPLE_NOTIFICATION_MODAL = (By.CSS_SELECTOR, 'div.simpleNotificationModal_content')
    CLOSE_SIMPLE_NOTIFICATION_MODAL = (By.CSS_SELECTOR, 'div.simpleNotificationModal_close')
    SHOW_CREATE_REPORT_DIALOG = (By.CSS_SELECTOR, '.new-report .btn.btn-success')
    CREATE_NEW_COUNTRY_PROPERTY_REPORT = (By.CSS_SELECTOR, '#rtm-createNewCountryPropertyReportButton')
    USER_NAME = (By.CSS_SELECTOR, '#headerUserName')


class BaNewCountryPropertyGeneralInformationPageLocators:
    BANK_DROP_DOWN_MENU = (By.XPATH, "//label[contains(text(),'Банк')]/..//div[contains(@id, 'node-SELECT-')]")
    SELECT_BANK = (By.XPATH, "//span[contains( text(), 'ВТБ')]")
    MODAL_POPUP = (By.CSS_SELECTOR, '.ui.modal')
    CLOSE_MODAL_POPUP = (By.CSS_SELECTOR, '.ui.large.basic')
    DEPARTMENT_DROP_DOWN_MENU = (By.XPATH,
                                 "//label[contains(text(),'Департамент')]/..//div[contains(@id, 'node-SELECT-')]")
    SELECT_DEPARTMENT = (By.XPATH, "//span[contains( text(), 'Ипотека')]")
    BANK_EMPLOYEE_DROP_DOWN_MENU = (By.XPATH,
                                    "//label[contains(text(),'Сотрудник банка')]/..//div[contains(@id, 'node-SELECT-')]")
    INPUT_BANK_EMPLOYEE = (By.XPATH,
                           "//label[contains(text(),'Сотрудник банка')]/..//div[contains(@id, 'node-SELECT-')]/input")
    INPUT_FULL_NAME_OF_THE_BORROWER_CUSTOMER = (By.XPATH,
                                                "//label[contains(text(), 'ФИО Заемщика/Заказчика')]/..//input")
    INPUT_REPORT_NUMBER = (By.XPATH, "//label[contains(text(), 'Номер отчета')]/..//input")
    REPORT_DATE = (By.XPATH, "//label[contains(text(), 'Дата отчета')]/..//input")
    SELECT_CURRENT_REPORT_DATE = (By.XPATH,
                                  "//label[contains(text(), 'Дата отчета')]/..//td[contains(@class, 'rdtToday')]")
    VALUATION_DATE = (By.XPATH, "//label[contains(text(), 'Дата оценки')]/..//input")
    SELECT_CURRENT_VALUATION_DATE = (By.XPATH,
                                     "//label[contains(text(), 'Дата оценки')]/..//td[contains(@class, 'rdtToday')]")
    SIGNER_DROP_DOWN_MENU = (By.XPATH,
                             "//label[contains(text(),'Подписант от лица организации')]/..//div[contains(@id, 'node-SELECT-')]")
    SELECT_SIGNER = (By.XPATH,
                     "//label[contains(text(),'Подписант от лица организации')]/..//span[contains(text(), 'Селениумов П. А.')]")
    SELECT_FILE = (By.CSS_SELECTOR, '.ui.basic.primary.button')
    INPUT_FILE = (By.XPATH, "//button[contains(@class, 'ui basic primary button')]/..//input")
    UPLOAD_PROGRESS_HIDE = (By.XPATH, "//div[contains(@class ,'Uploader_progressHide')]")
    DOWNLOAD_FILE_BUTTON = (By.XPATH, "//a[contains(@class, 'UploaderItem_download')]")
    DELETE_FILE_BUTTON = (By.XPATH, "//div[contains(@class, 'UploaderItem_remove')]")
    FOOTER = (By.XPATH, "//div[contains(@class, 'Footer_root')]")
    FROM_GENERAL_TAB_TO_PHOTOS_AND_DOCUMENTS_TAB = (By.XPATH, "//div[contains(text(), 'Фото и документы')]")


class BaNewCountryPropertyPhotosAndDocumentsPageLocators:
    INPUT_PHOTO = (By.XPATH, "//div[contains(text(), 'Фотографии')]/../../..//input")
    UPLOAD_PROGRESS_BAR_PHOTO = (By.XPATH,
                                 "//div[contains(text(), 'Фотографии')]/../../..//div[contains(@class, 'ui') and"
                                 " contains(@class, 'blue') and @data-percent='100']")
    INPUT_DOCUMENT = (By.XPATH, "//div[contains(text(), 'Документы')]/../../..//input")
    UPLOAD_PROGRESS_BAR_DOCUMENT = (By.XPATH,
                                    "//div[contains(text(), 'Документы')]/../../..//div[contains(@class, 'ui') and"
                                    " contains(@class, 'blue') and @data-percent='100']")
    FROM_PHOTO_AND_DOCUMENTS_TAB_TO_FIRST_OBJECT_TAB = (By.XPATH, "//div[contains(text(), 'Добавить объект')]")


class BaNewCountryPropertyResidentialBuildingPageLocators:
    TYPE_DROP_DOWN_MENU = (By.XPATH, "//label[contains(text(),'Тип')]/..//div[contains(@id, 'node-SELECT-')]")
    SELECT_A_PROPERTY_TYPE_WITH_THE_VALUE_RESIDENTIAL = (By.XPATH, "//span[contains( text(), 'Жилой (садовый) дом')]")
    DEFAULT_VALUE_IN_TYPE_FIELD = (By.XPATH, "//div[contains(text(), 'Жилой (садовый) дом')]")

