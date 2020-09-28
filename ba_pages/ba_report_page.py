from pages.base_page import BasePage
from .ba_locators import BaReportPageLocators
from options.data import DataBankAppraiser
from selenium.webdriver.common.keys import Keys
from .ba_locators import BaNewCountryPropertyResidentialBuildingPageLocators
from .ba_locators import BaReportPageLocators
from selenium.webdriver.common.by import By


class BaReportPage(BasePage):
    """
    Описание общих методов отчета, которые не имеют привязки к конкретной странице"
    """
    def go_to_photos_and_documents_tab(self):
        """ Переход в раздел 'Фотографии и документы' """
        self.browser.find_element(
            *BaReportPageLocators.GO_TO_PHOTOS_AND_DOCUMENTS_TAB).click()

    def go_to_new_object_tab(self):
        """ Переход в раздел с добавленным объектом """
        self.browser.find_element(
            *BaReportPageLocators.GO_TO_NEW_OBJECT_TAB).click()

    def input_the_address_for_documents(self, address):
        """ Заполнение поля 'Адрес по документам' """
        assert self.is_element_present(
            *BaReportPageLocators.INPUT_THE_ADDRESS_FOR_DOCUMENTS), \
            "Поле 'Адрес по документам' не отображается на странице "
        field_for_input_the_address_for_documents = self.browser.find_element(
            *BaReportPageLocators.INPUT_THE_ADDRESS_FOR_DOCUMENTS)
        field_for_input_the_address_for_documents.send_keys(address)
        field_for_input_the_address_for_documents.send_keys(Keys.TAB)
        assert field_for_input_the_address_for_documents.text == address, \
            f"Значение в поле 'Адрес по документам' не соответствует {address}"

    def input_fias_address(self, fias_address):
        """Заполнение поля 'Адрес по ФИАС' """
        assert self.is_element_present(*BaReportPageLocators.FIAS_DROP_DOWN_MENU), \
            " Поле 'Адрес по ФИАС' не отображается на странице "
        field_for_input_fias_address = self.browser.find_element(*BaReportPageLocators.INPUT_FIAS_ADDRESS)
        for char in fias_address:
            field_for_input_fias_address.send_keys(char)
        # is_element_presence в течение таймаута чекает подтянувшееся значение из КРОНЫ
        assert self.is_element_presence(
            By.XPATH, f"//span[contains(text(), '{fias_address}')]"), \
            f"Введенный {fias_address} не отображается в поле 'Адрес по ФИАС'. Возможно тормозит КРОНА "
        field_for_input_fias_address.send_keys(Keys.RETURN)
        check_value_in_fias_address_field = self.browser.find_element(
            By.XPATH, f"//div[contains(text(), '{fias_address}')]")
        assert check_value_in_fias_address_field.text == \
            fias_address, f"Значение в поле 'Адрес по ФИАС' не соответствует {fias_address}"

    def input_total_area_of_the_assessment_object(self, total_area):
        """ Заполнение поля с общей площадью ОО """
        assert self.is_element_present(*BaReportPageLocators.TOTAL_AREA_OF_THE_ASSESSMENT_OBJECT), \
            " Поле 'Общая площадь объекта оценки' не отображается на странице "
        field_for_input_total_area_of_the_assessment_object = self.browser.find_element(
            *BaReportPageLocators.TOTAL_AREA_OF_THE_ASSESSMENT_OBJECT)
        field_for_input_total_area_of_the_assessment_object.send_keys(total_area)
        assert field_for_input_total_area_of_the_assessment_object.get_attribute("value") == total_area, \
            f"Значение в поле 'Общая площадь объекта оценки' не соответствует {total_area}"

    def input_market_price_of_the_object(self, market_price):
        """ Заполнение поля 'Рычноная стоимость объекта оценки' """
        assert self.is_element_present(*BaReportPageLocators.MARKET_PRICE_OF_THE_OBJECT), \
            " Поле 'Рыночная стоимость объекта оценки' не отображается на странице "
        field_for_input_market_price_of_the_object = self.browser.find_element(
            *BaReportPageLocators.MARKET_PRICE_OF_THE_OBJECT)
        field_for_input_market_price_of_the_object.send_keys(market_price)
        assert field_for_input_market_price_of_the_object.get_attribute('value') == market_price, \
            f"Значение в поле 'Рыночная стоимость объекта оценки' не соответствует {market_price}"

    def pay_report(self):
        assert self.is_element_present(*BaReportPageLocators.PAY_REPORT_BUTTON_BEFORE_CLICK), \
            " Кнопка оплаты отчета отсутствует на странице "
        pay_report = self.browser.find_element(*BaReportPageLocators.PAY_REPORT_BUTTON_BEFORE_CLICK)
        pay_report.click()
        assert self.is_element_presence(
            *BaReportPageLocators.PAY_REPORT_BUTTON_AFTER_CLICK), "Селектор с кнопкой 'Оплачено' не обновился"
        assert self.text_in_element_is_correct(*BaReportPageLocators.PAY_REPORT_BUTTON_AFTER_CLICK, 'Оплачено'), \
            "Возникла проблема с оплатой отчета"

    def select_object_type(self, object_type):
        """ Выбор типа объекта Жилой (садовый) дом/Земельный участок/Иное """
        assert self.is_element_present(*BaReportPageLocators.TYPE_DROP_DOWN_MENU), \
            " Поле 'Тип' не отображается на странице "
        self.browser.find_element(*BaReportPageLocators.TYPE_DROP_DOWN_MENU).click()
        dict_with_object_types = \
        {
            'Жилой (садовый) дом': BaReportPageLocators.SELECT_RESIDENTIAL_TYPE,
            'Земельный участок': BaReportPageLocators.SELECT_LAND_TYPE,
            'Иное': BaReportPageLocators.SELECT_OTHER_TYPE
        }
        selected_type = dict_with_object_types[object_type.value]
        self.browser.find_element(*selected_type).click()
        assert self.browser.find_element(By.XPATH, f"//div[contains(text(), '{object_type.value}')]").text == \
            object_type.value, f"Выбранный тип недвижимости != {object_type.value}"

    def save_report(self):
        """ Сохранение отчета """
        assert self.is_element_present(*BaReportPageLocators.SAVE_REPORT_BUTTON), \
            " Кнопка сохранения отчета отсутствует на странице "
        save_report = self.browser.find_element(*BaReportPageLocators.SAVE_REPORT_BUTTON)
        save_report.click()
        assert self.text_in_element_is_correct(*BaReportPageLocators.SAVE_REPORT_BUTTON, 'Cохранено'), \
            "Сохранить не поменялось на Сохранено. P.S. слово 'сохранено' написано в БО с ошибкой"

    def sign_report(self):
        assert self.is_element_present(*BaReportPageLocators.COMPLETE_AND_SIGN_BUTTON), \
            " Кнопка 'Завершить и подписать' отсутствует на странице"
        button_for_complete_and_sign = self.browser.find_element(*BaReportPageLocators.COMPLETE_AND_SIGN_BUTTON)
        button_for_complete_and_sign.click()
        assert self.is_element_visible(*BaReportPageLocators.THE_COMPLETION_OF_THE_REPORT_WINDOW), \
            " Окно 'Завершение отчета' не появилось на странице "
        assert self.is_element_visible(*BaReportPageLocators.ENTER_THE_PASSWORD_FOR_SIGNING), \
            " Поле для ввода пароля при подписании отчета не появилось на странице "
        field_for_enter_the_password_for_singing = self.browser.find_element(
            *BaReportPageLocators.ENTER_THE_PASSWORD_FOR_SIGNING)
        field_for_enter_the_password_for_singing.send_keys(DataBankAppraiser.SharedData.password_for_singing_reports)
        assert self.is_element_present(*BaReportPageLocators.SIGN_BUTTON), " Кнопка 'Подписать' отсутствует на странице"
        sign_button = self.browser.find_element(*BaReportPageLocators.SIGN_BUTTON)
        sign_button.click()
        assert self.text_in_element_is_correct(*BaReportPageLocators.SUCCESSFUL_SIGN,
                                               'Отчет готов к печати!'), "При подписании отчета возникла ошибка"

    def select_property_rights_to_the_object_assessments(self, right):
        """ Выбор права в поле 'Имущественные права на объект оценки' """
        assert self.is_element_present(*BaReportPageLocators.PROPERTY_RIGHTS_TO_THE_OBJECT_ASSESSMENT), \
            " Поле 'Имущественные права на объект оценки' отсутствует на странице "
        drop_down_menu_for_the_property_rights_field = self.browser.find_element(
            *BaReportPageLocators.PROPERTY_RIGHTS_TO_THE_OBJECT_ASSESSMENT)
        drop_down_menu_for_the_property_rights_field.click()
        dict_with_property_rights = \
            {
                'Право собственности': BaNewCountryPropertyResidentialBuildingPageLocators.SELECT_OWNERSHIP,
                'Права не оформлены': BaNewCountryPropertyResidentialBuildingPageLocators.SELECT_RIGHTS_ARE_NOT_ISSUED,
                'Аренда': BaNewCountryPropertyResidentialBuildingPageLocators.SELECT_RENT
            }
        select_a_right = dict_with_property_rights[right.value]
        self.browser.find_element(*select_a_right).click()
        assert self.browser.find_element(By.XPATH, f"//div[contains(text(), '{right.value}')]").text == right.value, \
            f"Значение в поле 'Имущственые права на объект оценки' != {right}"

    def select_reason_why_not_egrn(self, reason):
        """ Выбор причины отсутствия актуальной выписки из ЕГРН """
        assert self.is_element_present(*BaReportPageLocators.EGRN_DROP_DOWN_MENU), \
            " Поле 'Причина отсутствия актуальной выписки из ЕГРН отсутствует на странице' "
        drop_down_menu_for_egrn = self.browser.find_element(*BaReportPageLocators.EGRN_DROP_DOWN_MENU)
        drop_down_menu_for_egrn.click()
        dict_with_reasons = \
            {
                'Техническая проблема на сайте Росреестра':
                    BaReportPageLocators.SELECT_TECHNICAL_ISSUE_EGRN,
                'Другое': BaReportPageLocators.SELECT_OTHER_ISSUE_EGRN
            }
        select_reason = dict_with_reasons[reason.value]
        self.browser.find_element(*select_reason).click()
        assert self.browser.find_element(
            By.XPATH, f"//label[contains(text(),'Причина отсутствия')]/..//div[contains(text(), "
                      f"'{reason.value}')]").text == reason.value, \
            f"Значение в поле 'Причина отсутствия актуальной выписки из ЕГРН отсутствует на странице' != {reason.value}"

    def select_electricity(self, electricity):
        """ Выбор электричества """
        assert self.is_element_present(
            *BaReportPageLocators.ELECTRICITY_DROP_DOWN_MENU), " Поле 'Электричество' не отображается на странице "
        drop_down_menu_for_electricity_field = self.browser.find_element(
            *BaReportPageLocators.ELECTRICITY_DROP_DOWN_MENU)
        drop_down_menu_for_electricity_field.click()
        dict_with_electricity = \
            {
                'Нет': BaReportPageLocators.SELECT_NO_ELECTRICITY,
                'Есть, центральное': BaReportPageLocators.SELECT_CENTRAL_ELECTRICITY,
                'Есть на участке': BaReportPageLocators.SELECT_ON_THE_SITE_ELECTRICITY,
                'По границе участка': BaReportPageLocators.SELECT_AT_THE_BORDER_ELECTRICITY
            }
        selected_value_of_electricity = dict_with_electricity[electricity.value]
        self.browser.find_element(*selected_value_of_electricity).click()
        assert self.browser.find_element(
            By.XPATH, "//label[contains(text(),'Электричество')]"
            f"/..//div[contains(text(), '{electricity.value}')]").text == electricity.value, \
            f"Значение в поле 'Электричество' != {electricity.value}"

    def select_water_supply(self, water_supply):
        """ Выбор водоснабжения """
        assert self.is_element_present(
            *BaReportPageLocators.WATER_SUPPLY_DROP_DOWN_MENU), " Поле 'Водоснабжение' не отображается на странице' "
        drop_down_menu_for_water_supply_field = self.browser.find_element(
            *BaReportPageLocators.WATER_SUPPLY_DROP_DOWN_MENU)
        drop_down_menu_for_water_supply_field.click()
        dict_with_water_supply = \
            {
                'Нет': BaReportPageLocators.SELECT_NO_WATER_SUPPLY,
                'Есть, автономное': BaReportPageLocators.SELECT_AUTONOMOUS_WATER_SUPPLY,
                'Есть, центральное': BaReportPageLocators.SELECT_CENTRAL_WATER_SUPPLY,
                'Есть на участке': BaReportPageLocators.SELECT_ON_THE_SITE_WATER_SUPPLY,
                'По границе участка': BaReportPageLocators.SELECT_AT_THE_BORDER_WATER_SUPPLY
            }
        selected_value_of_water_supply = dict_with_water_supply[water_supply.value]
        self.browser.find_element(*selected_value_of_water_supply).click()
        assert self.browser.find_element(
            By.XPATH, "//label[contains(text(),'Водоснабжение')]"
            f"/..//div[contains(text(), '{water_supply.value}')]").text == water_supply.value, \
            f"Значение в поле 'Водоснабжение' != {water_supply.value}"

    def select_sewerage(self, sewerage):
        """ Выбор канализации """
        assert self.is_element_present(
            *BaReportPageLocators.SEWERAGE_DROP_DOWN_MENU), " Поле 'Канализация' не отображается на странице' "
        drop_down_menu_for_sewerage_field = self.browser.find_element(
            *BaReportPageLocators.SEWERAGE_DROP_DOWN_MENU)
        drop_down_menu_for_sewerage_field.click()
        dict_with_sewerage = \
            {
                'Нет': BaReportPageLocators.SELECT_NO_SEWERAGE,
                'Есть, автономное': BaReportPageLocators.SELECT_AUTONOMOUS_SEWERAGE,
                'Есть, центральное': BaReportPageLocators.SELECT_CENTRAL_SEWERAGE,
                'Есть на участке': BaReportPageLocators.SELECT_ON_THE_SITE_SEWERAGE,
                'По границе участка': BaReportPageLocators.SELECT_AT_THE_BORDER_SEWERAGE
            }
        selected_value_of_sewerage = dict_with_sewerage[sewerage.value]
        self.browser.find_element(*selected_value_of_sewerage).click()
        assert self.browser.find_element(
            By.XPATH, "//label[contains(text(),'Канализация')]"
            f"/..//div[contains(text(), '{sewerage.value}')]").text == sewerage.value, \
            f"Значение в поле 'Канализация' != {sewerage.value}"
