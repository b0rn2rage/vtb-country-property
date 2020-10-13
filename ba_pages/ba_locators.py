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
    SIMPLE_NOTIFICATION_MODAL = (By.CSS_SELECTOR, '.simpleNotificationModal_content')
    CLOSE_SIMPLE_NOTIFICATION_MODAL = (By.CSS_SELECTOR, 'div.simpleNotificationModal_close')
    SHOW_CREATE_REPORT_DIALOG = (By.CSS_SELECTOR, '.new-report .btn.btn-success')
    USER_NAME = (By.CSS_SELECTOR, '#headerUserName')
    CREATE_NEW_REPORT_FLAT = (
        By.XPATH, "//a[contains(text(), 'Квартиры') and contains(@class, 'btn-success')]")
    CREATE_NEW_REPORT_COMMERCIAL_PROPERTY = (
        By.XPATH, "//a[contains(text(), 'Коммерческая недвижимость') and contains(@class, 'btn-success')]")
    CREATE_NEW_REPORT_COUNTRY_PROPERTY = (
        By.XPATH, "//a[contains(text(), 'Жилые дома') and contains(@class, 'btn-success')]")
    CREATE_NEW_REPORT_INTANGIBLE_ASSET = (
        By.XPATH, "//a[contains(text(), 'Нематериальные активы') and contains(@class, 'btn-success')]")
    CREATE_NEW_REPORT_MOVABLE_PROPERTY = (
        By.XPATH, "//a[contains(text(), 'Движимое имущество') and contains(@class, 'btn-success')]")
    CREATE_NEW_REPORT_NEW_INVENTORY = (
        By.XPATH, "//a[contains(text(), 'Товарно-материальные ценности') and contains(@class, 'btn-success')]")


class BaCountryPropertyGeneralInfoPageLocators:
    MODAL_POPUP = (By.CSS_SELECTOR, '.ui.modal')
    CLOSE_MODAL_POPUP = (By.CSS_SELECTOR, '.ui.large.basic')
    BANK_DROP_DOWN_MENU = (By.XPATH, "//label[contains(text(),'Банк')]/..//div[contains(@id, 'node-SELECT-')]")
    SELECT_BANK_VTB = (By.XPATH, "//span[contains(text(), 'ВТБ')]")
    SELECT_BANK_OPENBANK = (By.XPATH, "//span[contains(text(), 'ПАО Банк 'ФК Открытие'')]")
    DEPARTMENT_DROP_DOWN_MENU = (By.XPATH,
                                 "//label[contains(text(),'Департамент')]/..//div[contains(@id, 'node-SELECT-')]")
    SELECT_MORTGAGE_DEPARTMENT = (By.XPATH, "//span[contains( text(), 'Ипотека')]")
    SELECT_SMALL_BUSINESS_LENDING_DEPARTMENT = (By.XPATH, "//span[contains( text(), 'Кредитование малого бизнеса')]")
    BANK_EMPLOYEE_DROP_DOWN_MENU = (
        By.XPATH, "//label[contains(text(),'Сотрудник банка')]/..//div[contains(@id, 'node-SELECT-')]")
    INPUT_BANK_EMPLOYEE = (By.XPATH,
                           "//label[contains(text(),'Сотрудник банка')]/..//div[contains(@id, 'node-SELECT-')]/input")
    INPUT_NAME_OF_THE_BORROWER_CUSTOMER = (By.XPATH,
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
    INPUT_FILE = (By.XPATH, "//button[contains(@class, 'ui basic primary button')]/..//input")
    UPLOAD_PROGRESS_HIDE = (By.XPATH, "//div[contains(@class ,'Uploader_progressHide')]")
    FOOTER = (By.XPATH, "//div[contains(@class, 'Footer_root')]")
    EXTERNAL_EXAMINATION_DROP_DOWN_MENU = (
        By.XPATH, "//label[contains(text(),'Внешний осмотр')]/..//div[contains(@id, 'node-SELECT-')]")
    SELECT_EXTERNAL_EXAMINATION = (By.XPATH,
                                   "//label[contains(text(),'Внешний осмотр')]/..//div[contains(@id, 'node-SELECT-')]"
                                   "//span[contains( text(), 'Проводился')]")
    CHECKING_THE_SELECTED_EXTERNAL_EXAMINATION = (
        By.XPATH, "//label[contains(text(),'Внешний осмотр')]/..//div[contains(text(), 'Проводился')]")
    INTERNAL_INSPECTION_DROP_DOWN_MENU = (
        By.XPATH, "//label[contains(text(),'Внутренний осмотр')]/..//div[contains(@id, 'node-SELECT-')]")
    SELECT_INTERNAL_INSPECTION = (By.XPATH,
                                  "//label[contains(text(),'Внутренний осмотр')]/..//div[contains(@id, 'node-SELECT-')]"
                                  "//span[contains( text(), 'Проводился')]")
    CHECKING_THE_SELECTED_INTERNAL_INSPECTION = (
        By.XPATH, "//label[contains(text(),'Внутренний осмотр')]/..//div[contains(text(), 'Проводился')]")


class BaCountryPropertyPhotosAndDocsPageLocators:
    INPUT_PHOTO = (By.XPATH, "//div[contains(text(), 'Фотографии')]/../../..//input")
    UPLOAD_PROGRESS_BAR_FOR_PHOTO = (
        By.XPATH, "//div[contains(text(), 'Фотографии')]/../../..//div[contains(@class, 'ui') and "
                  "contains(@class, 'blue') and @data-percent='100']")
    INPUT_DOCUMENT = (By.XPATH, "//div[contains(text(), 'Документы')]/../../..//input")
    UPLOAD_PROGRESS_BAR_FOR_DOCUMENT = (
        By.XPATH, "//div[contains(text(), 'Документы')]/../../..//div[contains(@class, 'ui') and"
                  " contains(@class, 'blue') and @data-percent='100']")


class BaCountryPropertyResidentialBuildingPageLocators:
    INPUT_NAME_OF_THE_OBJECT = (
        By.XPATH, "//label[contains(text(), 'Наименование объекта')]/..//textarea[contains(@id, 'node-INPUT-')]")
    SELECT_OWNERSHIP = (By.XPATH, "//span[contains(text(), 'Право собственности')]")
    SELECT_RIGHTS_ARE_NOT_ISSUED = (By.XPATH, "//span[contains(text(), 'Права не оформлены')]")
    SELECT_RENT = (By.XPATH, "//span[contains(text(), 'Аренда')]")
    WALL_MATERIAL_DROP_DOWN_MENU = (By.XPATH,
                                    "//label[contains(text(),'Материал стен')]/..//div[contains(@id, 'node-SELECT-')]")
    SELECT_WALL_BRICK = (By.XPATH, "//span[contains( text(), 'Кирпич')]")
    SELECT_WALL_PANEL = (By.XPATH, "//span[contains( text(), 'Панель')]")
    SELECT_WALL_MONOLITH = (By.XPATH, "//span[contains( text(), 'Монолит')]")
    SELECT_WALL_BLOCK = (By.XPATH, "//span[contains( text(), 'Блок')]")
    SELECT_WALL_WOOD = (By.XPATH, "//span[contains( text(), 'Дерево')]")
    SELECT_WALL_BALK = (By.XPATH, "//span[contains( text(), 'Брус')]")
    SELECT_WALL_STONE = (By.XPATH, "//span[contains( text(), 'Каменные')]")
    SELECT_WALL_CARCASS = (By.XPATH, "//span[contains( text(), 'Каркасные')]")
    SELECT_WALL_METAL_FRAME_PANELS = (
        By.XPATH, "//span[contains( text(), 'Металлокаркасные панели/Легкие конструкции')]")
    SELECT_WALL_MONOLITH_BRICK = (By.XPATH, "//span[contains( text(), 'Монолит-кирпич')]")
    SELECT_WALL_SIP_PANELS = (By.XPATH, "//span[contains( text(), 'СИП панели')]")
    REPAIRS_DROP_DOWN_MENU = (By.XPATH,
                              "//label[contains(text(),'Состояние отделки')]/..//div[contains(@id, 'node-SELECT-')]")
    SELECT_REPAIRS_WITHOUT = (By.XPATH, "//span[contains( text(), 'Без отделки')]")
    SELECT_REPAIRS_CLEAN = (By.XPATH, "//span[contains( text(), 'Под чистовую отделку')]")
    SELECT_REPAIRS_AVERAGE = (By.XPATH, "//span[contains( text(), 'Среднее (жилое) состояние')]")
    SELECT_REPAIRS_GOOD = (By.XPATH, "//span[contains( text(), 'Хорошее состояние')]")
    SELECT_REPAIRS_EXCELLENT = (By.XPATH, "//span[contains( text(), 'Отличное (евро) состояние')]")
    HEAT_SUPPLY_DROP_DOWN_MENU = (
        By.XPATH, "//label[contains(text(),'Теплоснабжение')]/..//div[contains(@id, 'node-SELECT-')]")
    SELECT_HEAT_SUPPLY_NO = (By.XPATH, "//label[contains(text(),'Теплоснабжение')]/.."
                                       "//div[contains(@id, 'node-SELECT-')]/..//span[contains(text(), 'Нет')]")
    SELECT_HEAT_SUPPLY_AUTONOMOUS = (By.XPATH,
                                     "//label[contains(text(),'Теплоснабжение')]/..//"
                                     "div[contains(@id, 'node-SELECT-')]/..//span[contains(text(), 'Есть, автономное')]")
    SELECT_HEAT_SUPPLY_CENTRAL = (By.XPATH,
                                  "//label[contains(text(),'Теплоснабжение')]/..//"
                                  "div[contains(@id, 'node-SELECT-')]/..//span[contains(text(), 'Есть, центральное')]")
    CHECKING_THE_SELECTED_HEAT_SUPPLY = (
        By.XPATH, "//label[contains(text(),'Теплоснабжение')]/..//div[contains(text(), 'Нет')]")


class BaCountryPropertyLandPageLocators:
    INPUT_CADASTRAL_NUMBER = (
        By.XPATH, "//label[contains(text(),'Кадастровый номер')]/..//input[contains(@id, 'node-INPUT-')]")
    CATEGORY_DROP_DOWN_MENU = (By.XPATH, "//label[contains(text(),'Категория')]/..//div[contains(@id, 'node-SELECT-')]")
    SELECT_CATEGORY_SETTLEMENT = (By.XPATH, "//span[contains(text(), 'Земли населённых пунктов (земли поселений)')]")
    SELECT_CATEGORY_AGRICULTURAL = (By.XPATH, "//span[contains(text(), 'Земли сельскохозяйственного назначения')]")
    SELECT_CATEGORY_INDUSTRY = (
        By.XPATH, "//span[contains(text(), 'Земли промышленности и иного специального назначения')]")
    SELECT_CATEGORY_GUARDED = (By.XPATH, "//span[contains(text(), 'Земли особо охраняемых территорий и объектов')]")
    SELECT_CATEGORY_FOREST = (By.XPATH, "//span[contains(text(), 'Земли лесного фонда')]")
    SELECT_CATEGORY_WATER = (By.XPATH, "//span[contains(text(), 'Земли водного фонда')]")
    SELECT_CATEGORY_STOCK = (By.XPATH, "//span[contains(text(), 'Земли запаса')]")
    INPUT_TYPE_OF_PERMITTED_USE = (
        By.XPATH, "//label[contains(text(),'Вид разрешенного использования')]/..//input[contains(@id, 'node-INPUT-')]")


class BaReportPageLocators:
    SAVE_REPORT_BUTTON = (By.XPATH, "//button[contains(@id, 'node-REPORT_HEADER-')]")
    PAY_REPORT_BUTTON_BEFORE_CLICK = (By.XPATH, "//i[contains(@class, 'shopping')]/..")
    PAY_REPORT_BUTTON_AFTER_CLICK = (By.CSS_SELECTOR, ".ui.green.small.disabled.button")
    COMPLETE_AND_SIGN_BUTTON = (By.XPATH, "//i[contains(@class, 'flag')]/..")
    THE_COMPLETION_OF_THE_REPORT_WINDOW = (By.CSS_SELECTOR, ".ui.tiny.modal.transition.visible.active")
    GO_TO_PHOTOS_AND_DOCUMENTS_TAB = (By.XPATH, "//div[contains(text(), 'Фото и документы')]")
    GO_TO_NEW_OBJECT_TAB = (By.XPATH, "//div[contains(text(), 'Добавить объект')]")
    ENTER_THE_PASSWORD_FOR_SIGNING = (By.CSS_SELECTOR, "input[name='authPassword']")
    SIGN_BUTTON = (By.XPATH, "//button[contains(text(), 'Подписать')]")
    SUCCESSFUL_SIGN = (By.XPATH, "//div[contains(text(), 'Отчет готов к печати')]")
    TYPE_DROP_DOWN_MENU = (By.XPATH, "//label[contains(text(),'Тип')]/..//div[contains(@id, 'node-SELECT-')]")
    SELECT_RESIDENTIAL_TYPE = (By.XPATH, "//span[contains(text(), 'Жилой (садовый) дом')]")
    SELECT_LAND_TYPE = (By.XPATH, "//span[contains(text(), 'Земельный участок')]")
    SELECT_OTHER_TYPE = (By.XPATH, "//span[contains(text(), 'Иное')]")
    INPUT_THE_ADDRESS_FOR_DOCUMENTS = (
        By.XPATH, "//label[contains(text(), 'Адрес по документам')]/..//textarea[contains(@id, 'node-INPUT-')]")
    FIAS_DROP_DOWN_MENU = (By.XPATH, "//label[contains(text(),'Адрес по ФИАС')]/..//div[contains(@id, 'node-SELECT-')]")
    INPUT_FIAS_ADDRESS = (By.XPATH, "//label[contains(text(), 'Адрес по ФИАС')]/..//input")
    TOTAL_AREA_OF_THE_ASSESSMENT_OBJECT = (
        By.XPATH, "//label[contains(text(), 'Общая площадь объекта оценки')]/..//input[contains(@id, 'node-INPUT-')]")
    EGRN_DROP_DOWN_MENU = \
        (By.XPATH, "//label[contains(text(), 'Причина отсутствия актуальной')]/..//div[contains(@id, 'node-SELECT-')]")
    SELECT_TECHNICAL_ISSUE_EGRN = \
        (By.XPATH, "//label[contains(text(),'Причина отсутствия')]/..//span[contains(text(), "
                   "'Техническая проблема на сайте Росреестра')]")
    SELECT_OTHER_ISSUE_EGRN = \
        (By.XPATH, "//label[contains(text(),'Причина отсутствия')]/..//span[contains(text(), 'Другое')]")
    PROPERTY_RIGHTS_TO_THE_OBJECT_ASSESSMENT = (
        By.XPATH, "//label[contains(text(), 'Имущественные права на объект оценки')]/..//"
                  "div[contains(@id, 'node-SELECT-')]")
    MARKET_PRICE_OF_THE_OBJECT = (
        By.XPATH, "//label[contains(text(), 'Рыночная стоимость объекта оценки, руб.')]/..//"
                  "input[contains(@id, 'node-INPUT-')]")
    ELECTRICITY_DROP_DOWN_MENU = (
        By.XPATH, "//label[contains(text(),'Электричество')]/..//div[contains(@id, 'node-SELECT-')]")
    SELECT_NO_ELECTRICITY = (By.XPATH,
                             "//label[contains(text(),'Электричество')]/..//"
                             "div[contains(@id, 'node-SELECT-')]/..//span[contains(text(), 'Нет')]")
    SELECT_CENTRAL_ELECTRICITY = (By.XPATH,
                                  "//label[contains(text(),'Электричество')]/..//"
                                  "div[contains(@id, 'node-SELECT-')]/..//span[contains(text(), 'Есть, центральное')]")
    SELECT_ON_THE_SITE_ELECTRICITY = (
        By.XPATH, "//label[contains(text(),'Электричество')]/..//"
        "div[contains(@id, 'node-SELECT-')]/..//span[contains(text(), 'Есть на участке')]")
    SELECT_AT_THE_BORDER_ELECTRICITY = (
        By.XPATH, "//label[contains(text(),'Электричество')]/..//"
        "div[contains(@id, 'node-SELECT-')]/..//span[contains(text(), 'По границе участка')]")
    WATER_SUPPLY_DROP_DOWN_MENU = (
        By.XPATH, "//label[contains(text(),'Водоснабжение')]/..//div[contains(@id, 'node-SELECT-')]")
    SELECT_NO_WATER_SUPPLY = (By.XPATH,
                              "//label[contains(text(),'Водоснабжение')]/..//"
                              "div[contains(@id, 'node-SELECT-')]/..//span[contains(text(), 'Нет')]")
    SELECT_AUTONOMOUS_WATER_SUPPLY = (
        By.XPATH, "//label[contains(text(),'Водоснабжение')]/..//"
                  "div[contains(@id, 'node-SELECT-')]/..//span[contains(text(), 'Есть, автономное')]")
    SELECT_CENTRAL_WATER_SUPPLY = (
        By.XPATH, "//label[contains(text(),'Водоснабжение')]/..//"
                  "div[contains(@id, 'node-SELECT-')]/..//span[contains(text(), 'Есть, центральное')]")
    SELECT_ON_THE_SITE_WATER_SUPPLY = (
        By.XPATH, "//label[contains(text(),'Водоснабжение')]/..//"
                  "div[contains(@id, 'node-SELECT-')]/..//span[contains(text(), 'Есть, на участке')]")
    SELECT_AT_THE_BORDER_WATER_SUPPLY = (
        By.XPATH, "//label[contains(text(),'Водоснабжение')]/..//"
                  "div[contains(@id, 'node-SELECT-')]/..//span[contains(text(), 'По границе участка')]")
    SEWERAGE_DROP_DOWN_MENU = (
        By.XPATH, "//label[contains(text(),'Канализация')]/..//div[contains(@id, 'node-SELECT-')]")
    SELECT_NO_SEWERAGE = (By.XPATH,
                          "//label[contains(text(),'Канализация')]/..//"
                          "div[contains(@id, 'node-SELECT-')]/..//span[contains(text(), 'Нет')]")
    SELECT_AUTONOMOUS_SEWERAGE = (
        By.XPATH, "//label[contains(text(),'Канализация')]/..//"
                  "div[contains(@id, 'node-SELECT-')]/..//span[contains(text(), 'Есть, автономное')]")
    SELECT_CENTRAL_SEWERAGE = (
        By.XPATH, "//label[contains(text(),'Канализация')]/..//"
                  "div[contains(@id, 'node-SELECT-')]/..//span[contains(text(), 'Есть, центральное')]")
    SELECT_ON_THE_SITE_SEWERAGE = (
        By.XPATH, "//label[contains(text(),'Канализация')]/..//"
                  "div[contains(@id, 'node-SELECT-')]/..//span[contains(text(), 'Есть, на участке')]")
    SELECT_AT_THE_BORDER_SEWERAGE = (
        By.XPATH, "//label[contains(text(),'Канализация')]/..//"
                  "div[contains(@id, 'node-SELECT-')]/..//span[contains(text(), 'По границе участка')]")
    GAS_DROP_DOWN_MENU = (
        By.XPATH, "//label[contains(text(),'Газ')]/..//div[contains(@id, 'node-SELECT-')]")
    SELECT_NO_GAS = (By.XPATH,
                     "//label[contains(text(),'Газ')]/..//"
                     "div[contains(@id, 'node-SELECT-')]/..//span[contains(text(), 'Нет')]")
    SELECT_CENTRAL_GAS = (
        By.XPATH, "//label[contains(text(),'Газ')]/..//"
                  "div[contains(@id, 'node-SELECT-')]/..//span[contains(text(), 'Есть, центральное')]")
    SELECT_ON_THE_SITE_GAS = (
        By.XPATH, "//label[contains(text(),'Газ')]/..//"
                  "div[contains(@id, 'node-SELECT-')]/..//span[contains(text(), 'Есть, на участке')]")
    SELECT_AT_THE_BORDER_GAS = (
        By.XPATH, "//label[contains(text(),'Газ')]/..//"
                  "div[contains(@id, 'node-SELECT-')]/..//span[contains(text(), 'По границе участка')]")
    SELECT_THE_BORROWER_CUSTOMER_ARE_THE_SAME_PERSON = (
        By.XPATH, "//label[contains(text(),'Заемщик/Заказчик и собственник является одним лицом')]/..//input")
