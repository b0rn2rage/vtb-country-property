from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from .ba_locators import BaCountryPropertyResidentialBuildingPageLocators
from .ba_locators import BaReportPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class BaCountryPropertyReportPage(BasePage):
    """Описание общих методов отчета, которые не имеют привязки к конкретной странице."""
    def go_to_photos_and_documents_tab(self):
        """Переход в раздел 'Фотографии и документы'."""
        self.browser.find_element(*BaReportPageLocators.GO_TO_PHOTOS_AND_DOCUMENTS_TAB).click()

    def go_to_new_object_tab(self):
        """Переход в раздел с добавленным объектом."""
        self.browser.find_element(*BaReportPageLocators.GO_TO_NEW_OBJECT_TAB).click()

    def input_the_address_for_documents(self, address):
        """Заполнение поля 'Адрес по документам'."""
        input_the_address = self.browser.find_element(*BaReportPageLocators.INPUT_THE_ADDRESS_FOR_DOCUMENTS)
        input_the_address.send_keys(address)
        input_the_address.send_keys(Keys.TAB)
        assert input_the_address.text == address, \
            f"Значение в поле 'Адрес по документам' не соответствует {address}"

    def input_fias_address(self, fias_address):
        """Заполнение поля 'Адрес по ФИАС'."""
        input_fias = self.browser.find_element(*BaReportPageLocators.INPUT_FIAS_ADDRESS)
        for char in fias_address:
            input_fias.send_keys(char)
        assert self.is_element_presence(
            By.XPATH, f"//span[contains(text(), '{fias_address}')]"), \
            f"Введенный {fias_address} не отображается в поле 'Адрес по ФИАС'. Возможно тормозит КРОНА "
        input_fias.send_keys(Keys.RETURN)
        check_value_in_fias_address_field = self.browser.find_element(
            By.XPATH, f"//div[contains(text(), '{fias_address}')]")
        assert check_value_in_fias_address_field.text == \
            fias_address, f"Значение в поле 'Адрес по ФИАС' не соответствует {fias_address}"

    def input_total_area(self, total_area):
        """Заполнение поля с общей площадью ОО."""
        input_area = self.browser.find_element(*BaReportPageLocators.TOTAL_AREA_OF_THE_ASSESSMENT_OBJECT)
        input_area.send_keys(total_area)
        assert input_area.get_attribute("value") == total_area, \
            f"Значение в поле 'Общая площадь объекта оценки' не соответствует {total_area}"

    def input_market_price(self, market_price):
        """Заполнение поля 'Рычноная стоимость объекта оценки'."""
        market_price = self.browser.find_element(*BaReportPageLocators.MARKET_PRICE_OF_THE_OBJECT)
        market_price.send_keys(market_price)
        assert market_price.get_attribute('value') == market_price, \
            f"Значение в поле 'Рыночная стоимость объекта оценки' не соответствует {market_price}"

    def pay_report(self):
        pay_report = self.browser.find_element(*BaReportPageLocators.PAY_REPORT_BUTTON_BEFORE_CLICK)
        pay_report.click()
        assert self.is_element_presence(
            *BaReportPageLocators.PAY_REPORT_BUTTON_AFTER_CLICK), "Селектор с кнопкой 'Оплачено' не обновился"
        assert self.text_in_element_is_correct(*BaReportPageLocators.PAY_REPORT_BUTTON_AFTER_CLICK, 'Оплачено'), \
            "Возникла проблема с оплатой отчета"

    def open_new_window(self):
        """Открыть новую закладку в браузере."""
        self.browser.execute_script("window.open()")
        self.browser.switch_to.window(self.browser.window_handles[1])

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
        """Сохранение отчета."""
        save_report = self.browser.find_element(*BaReportPageLocators.SAVE_REPORT_BUTTON)
        save_report.click()
        assert self.text_in_element_is_correct(*BaReportPageLocators.SAVE_REPORT_BUTTON, 'Cохранено'), \
            "Сохранить не поменялось на Сохранено. P.S. слово 'сохранено' написано в БО с ошибкой"

    def sign_report(self):
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

    def select_property_rights(self, right):
        """Выбор права в поле 'Имущественные права на объект оценки'."""
        drop_down_menu_for_the_property_rights_field = self.browser.find_element(
            *BaReportPageLocators.PROPERTY_RIGHTS_TO_THE_OBJECT_ASSESSMENT)
        drop_down_menu_for_the_property_rights_field.click()
        dict_with_property_rights = \
            {
                'Право собственности': BaCountryPropertyResidentialBuildingPageLocators.SELECT_OWNERSHIP,
                'Права не оформлены': BaCountryPropertyResidentialBuildingPageLocators.SELECT_RIGHTS_ARE_NOT_ISSUED,
                'Аренда': BaCountryPropertyResidentialBuildingPageLocators.SELECT_RENT
            }
        select_a_right = dict_with_property_rights[right.value]
        self.browser.find_element(*select_a_right).click()
        assert self.browser.find_element(By.XPATH, f"//div[contains(text(), '{right.value}')]").text == right.value, \
            f"Значение в поле 'Имущственые права на объект оценки' != {right}"

    def select_reason_why_not_egrn(self, reason):
        """Выбор причины отсутствия актуальной выписки из ЕГРН."""
        drop_down_menu_for_egrn = self.browser.find_element(*BaReportPageLocators.EGRN_DROP_DOWN_MENU)
        drop_down_menu_for_egrn.click()
        dict_with_reasons = \
            {
                'Техническая проблема на сайте Росреестра': BaReportPageLocators.SELECT_TECHNICAL_ISSUE_EGRN,
                'Другое': BaReportPageLocators.SELECT_OTHER_ISSUE_EGRN
            }
        select_reason = dict_with_reasons[reason.value]
        self.browser.find_element(*select_reason).click()
        assert self.browser.find_element(
            By.XPATH, f"//label[contains(text(),'Причина отсутствия')]/..//div[contains(text(), "
                      f"'{reason.value}')]").text == reason.value, \
            f"Значение в поле 'Причина отсутствия актуальной выписки из ЕГРН отсутствует на странице' != {reason.value}"

    def select_electricity(self, electricity):
        """Выбор электричества."""
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
        """Выбор водоснабжения."""
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
        """Выбор канализации."""
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

    def select_gas(self, gas):
        """Выбор газа."""
        drop_down_menu_for_gas_field = self.browser.find_element(*BaReportPageLocators.GAS_DROP_DOWN_MENU)
        drop_down_menu_for_gas_field.click()
        dict_with_gas = \
            {
                'Нет': BaReportPageLocators.SELECT_NO_GAS,
                'Есть, центральное': BaReportPageLocators.SELECT_CENTRAL_GAS,
                'Есть на участке': BaReportPageLocators.SELECT_ON_THE_SITE_GAS,
                'По границе участка': BaReportPageLocators.SELECT_AT_THE_BORDER_GAS
            }
        selected_value_of_gas = dict_with_gas[gas.value]
        self.browser.find_element(*selected_value_of_gas).click()
        assert self.browser.find_element(
            By.XPATH, f"//label[contains(text(),'Газ')]/..//div[contains(text(), '{gas.value}')]").text == gas.value, \
            f"Значение в поле 'Газ' != {gas.value}"

    def select_borrower_customer_are_same_person(self):
        """Включение чек-бокса 'Замемщик/Заказчик и собственник является одним лицом'."""
        scroll_to_checkbox = self.browser.find_element(
            *BaReportPageLocators.SELECT_THE_BORROWER_CUSTOMER_ARE_THE_SAME_PERSON)
        actions = ActionChains(self.browser)
        actions.move_to_element(scroll_to_checkbox).perform()
        checkbox_before_checked = self.browser.find_element(
            *BaReportPageLocators.SELECT_THE_BORROWER_CUSTOMER_ARE_THE_SAME_PERSON)
        self.browser.execute_script("arguments[0].click();", checkbox_before_checked)
        # После клика по чек-боксу элемент удаляется из DOM и заново загружается туда, поэтому требуется
        # переопределить элемент для проверки на то, что чек-бокс включен
        checkbox_after_checked = self.browser.find_element(
            *BaReportPageLocators.SELECT_THE_BORROWER_CUSTOMER_ARE_THE_SAME_PERSON)
        assert checkbox_after_checked.is_selected(), "Чек-бокс не активен"

