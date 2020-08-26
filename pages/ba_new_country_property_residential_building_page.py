from .base_page import BasePage
from .locators import BaNewCountryPropertyResidentialBuildingPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


class BaNewCountryPropertyResidentialBuildingPage(BasePage):
    """ Заполнение раздела 'Объект №1' в новом отчете по ЖД. Тип объекта = ЖД """

    def go_to_new_object_tab(self):
        assert self.is_element_present(*BaNewCountryPropertyResidentialBuildingPageLocators.GO_TO_NEW_OBJECT_TAB), \
            "Кнопка добавления нового объекта отсутствует на странице"
        from_residential_tab_go_to_land_object_tab = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.GO_TO_NEW_OBJECT_TAB)
        from_residential_tab_go_to_land_object_tab.click()

    def input_name_of_the_object(self):
        """ Заполнение поля 'Наименование объекта' """
        assert self.is_element_present(*BaNewCountryPropertyResidentialBuildingPageLocators.INPUT_NAME_OF_THE_OBJECT), \
            " Поле 'Наименование объекта (без учета адреса)' не отображается на странице "
        field_for_input_name_of_the_object = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.INPUT_NAME_OF_THE_OBJECT)
        field_for_input_name_of_the_object.click()
        field_for_input_name_of_the_object.send_keys("Home Sweet Home ^_^")
        field_for_input_name_of_the_object.send_keys(Keys.TAB)
        assert self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.INPUT_NAME_OF_THE_OBJECT).text == \
            "Home Sweet Home ^_^", " Значение в поле 'Наименование объекта...' не соответствует введенному "

    def input_the_address_for_documents(self):
        """ Заполнение поля 'Адрес по документам' """
        assert self.is_element_present(
            *BaNewCountryPropertyResidentialBuildingPageLocators.INPUT_THE_ADDRESS_FOR_DOCUMENTS), \
            "Поле 'Адрес по документам' не отображается на странице "
        field_for_input_the_address_for_documents = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.INPUT_THE_ADDRESS_FOR_DOCUMENTS)
        field_for_input_the_address_for_documents.click()
        field_for_input_the_address_for_documents.send_keys("г Москва, ул Тестовская, д 1А")
        field_for_input_the_address_for_documents.send_keys(Keys.TAB)
        assert field_for_input_the_address_for_documents.text == "г Москва, ул Тестовская, д 1А", \
            " Значение в поле 'Адрес по документам' не соответствует введенному "

    def input_fias_address(self):
        """Заполнение поля 'Адрес по ФИАС' """
        assert self.is_element_present(*BaNewCountryPropertyResidentialBuildingPageLocators.INPUT_FIAS_ADDRESS), \
            " Поле 'Адрес по ФИАС' не отображается на странице "
        field_for_input_fias_address = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.INPUT_FIAS_ADDRESS)
        field_for_input_fias_address.click()
        field_for_input_fias_address.send_keys("г Москва, ул Тестовская, д 1А")
        # is_element_presence в течение таймаута чекает подтянувшееся значение из КРОНЫ для поля
        assert self.is_element_presence(
            *BaNewCountryPropertyResidentialBuildingPageLocators.SELECT_VALUE_IN_THE_FIELD_FIAS_ADDRESS), \
            " Введенный адрес не отображается в поле 'Адрес по ФИАС'. Возможно тормозит КРОНА "
        field_for_input_fias_address.send_keys(Keys.RETURN)
        check_value_in_fias_address_field = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.CHECKING_THE_SELECTED_FIAS_ADDRESS)
        assert check_value_in_fias_address_field.text == "г Москва, ул Тестовская, д 1А", \
            " Значение в поле 'Адрес по ФИАС' не соответствует введенному "

    def input_total_area_of_the_assessment_object(self):
        """ Заполнение поля с общей площадью ОО """
        assert self.is_element_present(
            *BaNewCountryPropertyResidentialBuildingPageLocators.TOTAL_AREA_OF_THE_ASSESSMENT_OBJECT), \
            " Поле 'Общая площадь объекта оценки' не отображается на странице "
        field_for_input_total_area_of_the_assessment_object = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.TOTAL_AREA_OF_THE_ASSESSMENT_OBJECT)
        field_for_input_total_area_of_the_assessment_object.send_keys("250")
        assert field_for_input_total_area_of_the_assessment_object.get_attribute(
            "value") == '250', " Значение в поле 'Общая площадь объекта оценки не соответствует введенному' "

    def input_market_price_of_the_object(self):
        """ Заполнение поля 'Рычноная стоимость объекта оценки' """
        assert self.is_element_present(
            *BaNewCountryPropertyResidentialBuildingPageLocators.MARKET_PRICE_OF_THE_OBJECT), \
            " Поле 'Рыночная стоимость объекта оценки' не отображается на странице "
        field_for_input_market_price_of_the_object = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.MARKET_PRICE_OF_THE_OBJECT)
        field_for_input_market_price_of_the_object.send_keys("17000000")
        assert field_for_input_market_price_of_the_object.get_attribute('value') == '17000000', \
            "Значение в поле 'Рыночная стоимость объекта оценки' не соответствует введенному"

    def select_type_in_residential_building_tab(self):
        """ Проверка, что тип недвижимости = ЖД """
        assert self.is_element_present(*BaNewCountryPropertyResidentialBuildingPageLocators.TYPE_DROP_DOWN_MENU), \
            " Поле 'Тип' не отображается на странице "
        assert self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.CHECK_TYPE_IS_RESIDENTIAL_BUILDING), \
            " Выбранный тип недвижимости != Жилой садовый дом "

    def select_property_rights_to_the_object_assessments(self):
        """ Выбор имущественного права = Право собственности """
        assert self.is_element_present(
            *BaNewCountryPropertyResidentialBuildingPageLocators.PROPERTY_RIGHTS_TO_THE_OBJECT_ASSESSMENT), \
            " Поле 'Имущественные права на объект оценки' отсутствует на странице "
        drop_down_menu_for_the_property_rights_field = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.PROPERTY_RIGHTS_TO_THE_OBJECT_ASSESSMENT)
        drop_down_menu_for_the_property_rights_field.click()
        select_ownership = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.SELECT_PROPERTY_RIGHTS)
        select_ownership.click()
        assert self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.CHECKING_THE_SELECTED_PROPERTY_RIGHTS).text == \
            'Право собственности', " Значение в поле 'Имущственые права на объект оценки' != Право собственности "

    def select_wall_material(self):
        """ Выбор материала стен = Кирпич """
        assert self.is_element_present(
            *BaNewCountryPropertyResidentialBuildingPageLocators.WALL_MATERIAL_DROP_DOWN_MENU), \
            " Поле 'Материал стен' не отображается на странице "
        drop_down_menu_for_wall_material_field = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.WALL_MATERIAL_DROP_DOWN_MENU)
        drop_down_menu_for_wall_material_field.click()
        select_a_brick = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.SELECT_WALL_MATERIAL)
        select_a_brick.click()
        assert self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.CHECKING_THE_SELECTED_WALL_MATERIAL).text == "Кирпич",\
            " Значение в поле 'Материал стен' != Кирпич "

    def select_repairs(self):
        """ Выбор состояния отделки = Хорошее состояние """
        assert self.is_element_present(*BaNewCountryPropertyResidentialBuildingPageLocators.REPAIRS_DROP_DOWN_MENU), \
            " Поле 'Состояние отделки' не отображается на странице"
        drop_down_menu_for_repairs_field = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.REPAIRS_DROP_DOWN_MENU)
        drop_down_menu_for_repairs_field.click()
        select_a_good_repair = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.SELECT_REPAIRS)
        select_a_good_repair.click()
        assert self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.CHECKING_THE_SELECTED_REPAIRS).text == \
            "Хорошее состояние", " Значение в поле 'Состояние отделки' != Хорошее состояние "

    def select_electricity(self):
        """ Выбор электричества = Нет """
        assert self.is_element_present(
            *BaNewCountryPropertyResidentialBuildingPageLocators.ELECTRICITY_DROP_DOWN_MENU), \
            " Поле 'Электричество' не отображается на странице "
        drop_down_menu_for_electricity_field = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.ELECTRICITY_DROP_DOWN_MENU)
        drop_down_menu_for_electricity_field.click()
        select_no_electricity = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.SELECT_ELECTRICITY)
        select_no_electricity.click()
        assert self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.CHECKING_THE_SELECTED_ELECTRICITY).text == \
            "Нет", " Значение в поле 'Электричество' != Нет "

    def select_water_supply(self):
        """ Выбор водоснабжения = Нет """
        assert self.is_element_present(
            *BaNewCountryPropertyResidentialBuildingPageLocators.WATER_SUPPLY_DROP_DOWN_MENU), \
            " Поле 'Водоснабжение' не отображается на странице' "
        drop_down_menu_for_water_supply_field = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.WATER_SUPPLY_DROP_DOWN_MENU)
        drop_down_menu_for_water_supply_field.click()
        select_no_water_supply = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.SELECT_WATER_SUPPLY)
        select_no_water_supply.click()
        assert self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.CHECKING_THE_SELECTED_WATER_SUPPLY).text == \
            "Нет", " Значение в поле 'Водоснабжение' != Нет "

    def select_sewerage(self):
        """ Выбор канализации = Нет """
        assert self.is_element_present(
            *BaNewCountryPropertyResidentialBuildingPageLocators.SEWERAGE_DROP_DOWN_MENU), \
            " Поле 'Канализация' не отображается на странице' "
        drop_down_menu_for_sewerage_field = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.SEWERAGE_DROP_DOWN_MENU)
        drop_down_menu_for_sewerage_field.click()
        select_no_sewerage = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.SELECT_SEWERAGE)
        select_no_sewerage.click()
        assert self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.CHECKING_THE_SELECTED_SEWERAGE).text == \
            "Нет", " Значение в поле 'Канализация' != Нет "

    def select_gas(self):
        """ Выбор газа = Нет """
        assert self.is_element_present(
            *BaNewCountryPropertyResidentialBuildingPageLocators.GAS_DROP_DOWN_MENU), \
            " Поле 'Газ' не отображается на странице' "
        drop_down_menu_for_gas_field = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.GAS_DROP_DOWN_MENU)
        drop_down_menu_for_gas_field.click()
        select_no_gas = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.SELECT_GAS)
        select_no_gas.click()
        assert self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.CHECKING_THE_SELECTED_GAS).text == \
            "Нет", " Значение в поле 'Газ' != Нет "

    def select_heat_supply(self):
        """ Выбор теплоснабжения = Нет """
        assert self.is_element_present(
            *BaNewCountryPropertyResidentialBuildingPageLocators.HEAT_SUPPLY_DROP_DOWN_MENU), \
            " Поле 'Теплоснабжение' не отображается на странице' "
        drop_down_menu_for_heat_supply_field = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.HEAT_SUPPLY_DROP_DOWN_MENU)
        drop_down_menu_for_heat_supply_field.click()
        select_no_heat_supply = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.SELECT_HEAT_SUPPLY)
        select_no_heat_supply.click()
        assert self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.CHECKING_THE_SELECTED_HEAT_SUPPLY).text == \
            "Нет", " Значение в поле 'Теплоснабжение' != Нет "

    def select_borrower_customer_are_same_person(self):
        """Включение чек-бокса 'Замемщик/Заказчик и собственник является одним лицом' """
        assert self.is_element_present(
            *BaNewCountryPropertyResidentialBuildingPageLocators.SELECT_THE_BORROWER_CUSTOMER_ARE_THE_SAME_PERSON), \
            " Чек-бокс 'Заемщик/Заказчик и собственник является одним лицом' не отображатеся на странице "
        scroll_to_checkbox = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.SELECT_THE_BORROWER_CUSTOMER_ARE_THE_SAME_PERSON)
        actions = ActionChains(self.browser)
        actions.move_to_element(scroll_to_checkbox).perform()
        checkbox_for_borrower_customer_are_same_person_before_checked = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.SELECT_THE_BORROWER_CUSTOMER_ARE_THE_SAME_PERSON)
        self.browser.execute_script("arguments[0].click();",
                                    checkbox_for_borrower_customer_are_same_person_before_checked)
        # После клика по чек-боксу элемент удаляется из DOM и заново загружается туда, поэтому требуется
        # переопределить элемент для проверки на то, что чек-бокс включен
        checkbox_for_borrower_customer_are_same_person_after_checked = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.SELECT_THE_BORROWER_CUSTOMER_ARE_THE_SAME_PERSON)
        assert checkbox_for_borrower_customer_are_same_person_after_checked.is_selected(), "Чек-бокс не активен"

