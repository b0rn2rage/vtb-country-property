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
    MODAL_POPUP = (By.CSS_SELECTOR, '.ui.modal')
    CLOSE_MODAL_POPUP = (By.CSS_SELECTOR, '.ui.large.basic')
    BANK_DROP_DOWN_MENU = (By.XPATH, "//label[contains(text(),'Банк')]/..//div[contains(@id, 'node-SELECT-')]")
    SELECT_BANK = (By.XPATH, "//span[contains( text(), 'ВТБ')]")
    CHECKING_THE_SELECTED_BANK = (By.XPATH, "//div[contains(text(), 'ВТБ')]")
    DEPARTMENT_DROP_DOWN_MENU = (By.XPATH,
                                 "//label[contains(text(),'Департамент')]/..//div[contains(@id, 'node-SELECT-')]")
    SELECT_DEPARTMENT = (By.XPATH, "//span[contains( text(), 'Ипотека')]")
    CHECKING_THE_SELECTED_DEPARTMENT = (By.XPATH, "//div[contains(text(), 'Ипотека')]")
    BANK_EMPLOYEE_DROP_DOWN_MENU = (
        By.XPATH, "//label[contains(text(),'Сотрудник банка')]/..//div[contains(@id, 'node-SELECT-')]")
    INPUT_BANK_EMPLOYEE = (By.XPATH,
                           "//label[contains(text(),'Сотрудник банка')]/..//div[contains(@id, 'node-SELECT-')]/input")
    SELECT_A_VALUE_IN_THE_FIELD_EMPLOYEE_OF_THE_BANK = (
        By.XPATH, "//span[contains(text(), 'Селениумов Питон (autotest-country-property-vtb@test.ru)')]")
    CHECKING_THE_SELECTED_BANK_EMPLOYEE = (
        By.XPATH, "//div[contains(text(), 'Селениумов Питон (autotest-country-property-vtb@test.ru)')]")
    INPUT_FULL_NAME_OF_THE_BORROWER_CUSTOMER = (By.XPATH,
                                                "//label[contains(text(), 'ФИО Заемщика/Заказчика')]/..//input")
    INPUT_REPORT_NUMBER = (By.XPATH, "//label[contains(text(), 'Номер отчета')]/..//input")
    REPORT_DATE_FIELD = (By.XPATH, "//label[contains(text(), 'Дата отчета')]/..//input")
    SELECT_CURRENT_REPORT_DATE = (By.XPATH,
                                  "//label[contains(text(), 'Дата отчета')]/..//td[contains(@class, 'rdtToday')]")
    SELECT_VALUE_IN_REPORT_DATE_FIELD = (By.XPATH, "//label[contains(text(), 'Дата отчета')]/..//input")
    VALUATION_DATE_FIELD = (By.XPATH, "//label[contains(text(), 'Дата оценки')]/..//input")
    SELECT_CURRENT_VALUATION_DATE = (By.XPATH,
                                     "//label[contains(text(), 'Дата оценки')]/..//td[contains(@class, 'rdtToday')]")
    SELECT_VALUE_IN_VALUATION_DATE_FIELD = (By.XPATH, "//label[contains(text(), 'Дата оценки')]/..//input")
    SIGNER_DROP_DOWN_MENU = (
        By.XPATH, "//label[contains(text(),'Подписант от лица организации')]/..//div[contains(@id, 'node-SELECT-')]")
    SELECT_SIGNER = (
        By.XPATH,
        "//label[contains(text(),'Подписант от лица организации')]/..//span[contains(text(), 'Селениумов П. А.')]")
    SELECT_FILE = (By.CSS_SELECTOR, '.ui.basic.primary.button')
    INPUT_FILE = (By.XPATH, "//button[contains(@class, 'ui basic primary button')]/..//input")
    UPLOAD_PROGRESS_HIDE = (By.XPATH, "//div[contains(@class ,'Uploader_progressHide')]")
    DOWNLOAD_FILE_BUTTON = (By.XPATH, "//a[contains(@class, 'UploaderItem_download')]")
    DELETE_FILE_BUTTON = (By.XPATH, "//div[contains(@class, 'UploaderItem_remove')]")
    FOOTER = (By.XPATH, "//div[contains(@class, 'Footer_root')]")


class BaNewCountryPropertyPhotosAndDocumentsPageLocators:
    INPUT_PHOTO = (By.XPATH, "//div[contains(text(), 'Фотографии')]/../../..//input")
    UPLOAD_PROGRESS_BAR_FOR_PHOTO = (
        By.XPATH, "//div[contains(text(), 'Фотографии')]/../../..//div[contains(@class, 'ui') and "
        "contains(@class, 'blue') and @data-percent='100']")
    INPUT_DOCUMENT = (By.XPATH, "//div[contains(text(), 'Документы')]/../../..//input")
    UPLOAD_PROGRESS_BAR_FOR_DOCUMENT = (
        By.XPATH, "//div[contains(text(), 'Документы')]/../../..//div[contains(@class, 'ui') and"
        " contains(@class, 'blue') and @data-percent='100']")


class BaNewCountryPropertyResidentialBuildingPageLocators:
    TYPE_DROP_DOWN_MENU = (By.XPATH, "//label[contains(text(),'Тип')]/..//div[contains(@id, 'node-SELECT-')]")
    CHECK_TYPE_IS_RESIDENTIAL_BUILDING = (By.XPATH, "//div[contains(text(), 'Жилой (садовый) дом')]")
    INPUT_NAME_OF_THE_OBJECT = (
        By.XPATH, "//label[contains(text(), 'Наименование объекта')]/..//textarea[contains(@id, 'node-INPUT-')]")
    INPUT_THE_ADDRESS_FOR_DOCUMENTS = (
        By.XPATH, "//label[contains(text(), 'Адрес по документам')]/..//textarea[contains(@id, 'node-INPUT-')]")
    INPUT_FIAS_ADDRESS = (By.XPATH, "//label[contains(text(), 'Адрес по ФИАС')]/..//input")
    SELECT_VALUE_IN_THE_FIELD_FIAS_ADDRESS = (By.XPATH, "//span[contains(text(), 'г Москва, ул Тестовская, д 1А')]")
    CHECKING_THE_SELECTED_FIAS_ADDRESS = (By.XPATH, "//div[contains(text(), 'г Москва, ул Тестовская, д 1А')]")
    TOTAL_AREA_OF_THE_ASSESSMENT_OBJECT = (
        By.XPATH, "//label[contains(text(), 'Общая площадь объекта оценки')]/..//input[contains(@id, 'node-INPUT-')]")
    PROPERTY_RIGHTS_TO_THE_OBJECT_ASSESSMENT = (
        By.XPATH, "//label[contains(text(), 'Имущественные права на объект оценки')]/..//"
                  "div[contains(@id, 'node-SELECT-')]")
    SELECT_PROPERTY_RIGHTS = (By.XPATH, "//span[contains( text(), 'Право собственности')]")
    CHECKING_THE_SELECTED_PROPERTY_RIGHTS = (By.XPATH, "//div[contains(text(), 'Право собственности')]")
    WALL_MATERIAL_DROP_DOWN_MENU = (By.XPATH,
                                    "//label[contains(text(),'Материал стен')]/..//div[contains(@id, 'node-SELECT-')]")
    SELECT_WALL_MATERIAL = (By.XPATH, "//span[contains( text(), 'Кирпич')]")
    CHECKING_THE_SELECTED_WALL_MATERIAL = (By.XPATH, "//div[contains(text(), 'Кирпич')]")
    REPAIRS_DROP_DOWN_MENU = (By.XPATH,
                              "//label[contains(text(),'Состояние отделки')]/..//div[contains(@id, 'node-SELECT-')]")
    SELECT_REPAIRS = (By.XPATH, "//span[contains( text(), 'Хорошее состояние')]")
    CHECKING_THE_SELECTED_REPAIRS = (By.XPATH, "//div[contains(text(), 'Хорошее состояние')]")
    MARKET_PRICE_OF_THE_OBJECT = (
        By.XPATH, "//label[contains(text(), 'Рыночная стоимость объекта оценки, руб.')]/..//"
                  "input[contains(@id, 'node-INPUT-')]")
    ELECTRICITY_DROP_DOWN_MENU = (
        By.XPATH, "//label[contains(text(),'Электричество')]/..//div[contains(@id, 'node-SELECT-')]")
    SELECT_ELECTRICITY = (By.XPATH,
                          "//label[contains(text(),'Электричество')]/..//"
                          "div[contains(@id, 'node-SELECT-')]/..//span[contains(text(), 'Нет')]")
    CHECKING_THE_SELECTED_ELECTRICITY = (
        By.XPATH, "//label[contains(text(),'Электричество')]/..//div[contains(text(), 'Нет')]")
    WATER_SUPPLY_DROP_DOWN_MENU = (
        By.XPATH, "//label[contains(text(),'Водоснабжение')]/..//div[contains(@id, 'node-SELECT-')]")
    SELECT_WATER_SUPPLY = (By.XPATH,
                           "//label[contains(text(),'Водоснабжение')]/..//"
                           "div[contains(@id, 'node-SELECT-')]/..//span[contains(text(), 'Нет')]")
    CHECKING_THE_SELECTED_WATER_SUPPLY = (
        By.XPATH, "//label[contains(text(),'Водоснабжение')]/..//div[contains(text(), 'Нет')]")
    SEWERAGE_DROP_DOWN_MENU = (
        By.XPATH, "//label[contains(text(),'Канализация')]/..//div[contains(@id, 'node-SELECT-')]")
    SELECT_SEWERAGE = (By.XPATH,
                       "//label[contains(text(),'Канализация')]/..//"
                       "div[contains(@id, 'node-SELECT-')]/..//span[contains(text(), 'Нет')]")
    CHECKING_THE_SELECTED_SEWERAGE = (
        By.XPATH, "//label[contains(text(),'Канализация')]/..//div[contains(text(), 'Нет')]")
    GAS_DROP_DOWN_MENU = (
        By.XPATH, "//label[contains(text(),'Газ')]/..//div[contains(@id, 'node-SELECT-')]")
    SELECT_GAS = (By.XPATH,
                  "//label[contains(text(),'Газ')]/..//"
                  "div[contains(@id, 'node-SELECT-')]/..//span[contains(text(), 'Нет')]")
    CHECKING_THE_SELECTED_GAS = (
        By.XPATH, "//label[contains(text(),'Газ')]/..//div[contains(text(), 'Нет')]")
    HEAT_SUPPLY_DROP_DOWN_MENU = (
        By.XPATH, "//label[contains(text(),'Теплоснабжение')]/..//div[contains(@id, 'node-SELECT-')]")
    SELECT_HEAT_SUPPLY = (By.XPATH,
                          "//label[contains(text(),'Теплоснабжение')]/..//"
                          "div[contains(@id, 'node-SELECT-')]/..//span[contains(text(), 'Нет')]")
    CHECKING_THE_SELECTED_HEAT_SUPPLY = (
        By.XPATH, "//label[contains(text(),'Теплоснабжение')]/..//div[contains(text(), 'Нет')]")
    SELECT_THE_BORROWER_CUSTOMER_ARE_THE_SAME_PERSON = (
        By.XPATH, "//label[contains(text(),'Заемщик/Заказчик и собственник является одним лицом')]/..//input")
    EGRN_DROP_DOWN_MENU = (
        By.XPATH, "//label[contains(text(), 'Причина отсутствия актуальной')]/..//div[contains(@id, 'node-SELECT-')]")
    SELECT_EGRN = (By.XPATH, "//label[contains(text(),'Причина отсутствия')]/..//span[contains(text(), 'Другое')]")
    CHECKING_THE_SELECTED_EGRN = (
        By.XPATH, "//label[contains(text(),'Причина отсутствия')]/..//div[contains(text(), 'Другое')]")


class BaNewCountryPropertyLandPageLocators:
    SELECT_TYPE_IS_LAND = (By.XPATH, "//span[contains(text(), 'Земельный участок')]")
    CHECK_TYPE_IS_LAND = (By.XPATH, "//div[contains(text(), 'Земельный участок')]")
    INPUT_CADASTRAL_NUMBER = (
        By.XPATH, "//label[contains(text(),'Кадастровый номер')]/..//input[contains(@id, 'node-INPUT-')]")
    CATEGORY_DROP_DOWN_MENU = (By.XPATH, "//label[contains(text(),'Категория')]/..//div[contains(@id, 'node-SELECT-')]")
    SELECT_CATEGORY = (By.XPATH, "//span[contains(text(), 'Земли населённых пунктов (земли поселений)')]")
    CHECKING_THE_SELECTED_CATEGORY = (By.XPATH,
                                      "//label[contains(text(),'Категория')]/..//div[contains(text(), "
                                      "'Земли населённых пунктов (земли поселений)')]")
    INPUT_TYPE_OF_PERMITTED_USE = (
        By.XPATH, "//label[contains(text(),'Вид разрешенного использования')]/..//input[contains(@id, 'node-INPUT-')]")


class BaReportPageLocators:
    SAVE_REPORT_BUTTON = (By.XPATH, "//button[contains(@id, 'node-REPORT_HEADER-')]")
    PAY_REPORT_BUTTON = (By.XPATH, "//i[contains(@class, 'shopping')]/..")
    COMPLETE_AND_SIGN_BUTTON = (By.XPATH, "//i[contains(@class, 'flag')]/..")
    THE_COMPLETION_OF_THE_REPORT_WINDOW = (By.CSS_SELECTOR, ".ui.tiny.modal.transition.visible.active")
    GO_TO_PHOTOS_AND_DOCUMENTS_TAB = (By.XPATH, "//div[contains(text(), 'Фото и документы')]")
    GO_TO_NEW_OBJECT_TAB = (By.XPATH, "//div[contains(text(), 'Добавить объект')]")
    ENTER_THE_PASSWORD_FOR_SIGNING = (By.CSS_SELECTOR, "input[name='authPassword']")
    SIGN_BUTTON = (By.XPATH, "//button[contains(text(), 'Подписать')]")


