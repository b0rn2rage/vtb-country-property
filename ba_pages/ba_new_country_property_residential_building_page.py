from pages.base_page import BasePage
from .ba_locators import BaNewCountryPropertyResidentialBuildingPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from options.data import DataBankAppraiser


class BaNewCountryPropertyResidentialBuildingPage(BasePage):
    """ Заполнение раздела 'Объект №1' в новом отчете по ЖД. Тип объекта = ЖД """

    def input_market_price_of_the_object(self):
        """ Заполнение поля 'Рычноная стоимость объекта оценки' """
        assert self.is_element_present(
            *BaNewCountryPropertyResidentialBuildingPageLocators.MARKET_PRICE_OF_THE_OBJECT), \
            " Поле 'Рыночная стоимость объекта оценки' не отображается на странице "
        field_for_input_market_price_of_the_object = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.MARKET_PRICE_OF_THE_OBJECT)
        field_for_input_market_price_of_the_object.send_keys(DataBankAppraiser.BaCountryReport.Moscow_low_price_house)
        assert field_for_input_market_price_of_the_object.get_attribute('value') == \
            DataBankAppraiser.BaCountryReport.Moscow_low_price_house, \
            "Значение в поле 'Рыночная стоимость объекта оценки' не соответствует введенному"

    def select_type_in_residential_building_tab(self):
        """ Проверка, что тип недвижимости = ЖД """
        assert self.is_element_present(*BaNewCountryPropertyResidentialBuildingPageLocators.TYPE_DROP_DOWN_MENU), \
            " Поле 'Тип' не отображается на странице "
        assert self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.CHECK_TYPE_IS_RESIDENTIAL_BUILDING), \
            " Выбранный тип недвижимости != Жилой садовый дом "

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

    def select_reason_why_not_egrn(self):
        """ Выбор причины актуальной выписки из ЕГРН = Другое """
        assert self.is_element_present(*BaNewCountryPropertyResidentialBuildingPageLocators.EGRN_DROP_DOWN_MENU), \
            " Поле 'Причина отсутствия актуальной выписки из ЕГРН отсутствует на странице' "
        drop_down_menu_for_egrn = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.EGRN_DROP_DOWN_MENU)
        drop_down_menu_for_egrn.click()
        select_reason = self.browser.find_element(*BaNewCountryPropertyResidentialBuildingPageLocators.SELECT_EGRN)
        select_reason.click()
        assert self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.CHECKING_THE_SELECTED_EGRN).text == "Другое", \
            " Значение в поле 'Причина отсутствия актуальной выписки из ЕГРН отсутствует на странице' != Другое "

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



