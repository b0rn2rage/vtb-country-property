from pages.base_page import BasePage
from .ba_locators import BaCountryPropertyResidentialBuildingPageLocators
from selenium.webdriver.common.keys import Keys


class BaCountryPropertyResidentialBuildingPage(BasePage):
    """Заполнение раздела с типом объекта = ЖД."""

    def input_name_of_the_object(self, name):
        input_name = self.browser.find_element(
            *BaCountryPropertyResidentialBuildingPageLocators.INPUT_NAME_OF_THE_OBJECT)
        input_name.click()
        input_name.send_keys(name)
        input_name.send_keys(Keys.TAB)
        assert self.browser.find_element(
            *BaCountryPropertyResidentialBuildingPageLocators.INPUT_NAME_OF_THE_OBJECT).text == \
            f"{name}", f"Значение в поле 'Наименование объекта...' не соответствует {name}"

    def select_wall_material(self, material):
        """Выбор материала стен"""
        drop_down_menu_for_wall_material_field = self.browser.find_element(
            *BaCountryPropertyResidentialBuildingPageLocators.WALL_MATERIAL_DROP_DOWN_MENU)
        drop_down_menu_for_wall_material_field.click()
        dict_with_wall_materials = \
            {

            }
        assert self.browser.find_element(
            *BaCountryPropertyResidentialBuildingPageLocators.CHECKING_THE_SELECTED_WALL_MATERIAL).text == "Кирпич",\
            " Значение в поле 'Материал стен' != Кирпич "

    def select_repairs(self):
        """Выбор состояния отделки"""
        assert self.is_element_present(*BaCountryPropertyResidentialBuildingPageLocators.REPAIRS_DROP_DOWN_MENU), \
            " Поле 'Состояние отделки' не отображается на странице"
        drop_down_menu_for_repairs_field = self.browser.find_element(
            *BaCountryPropertyResidentialBuildingPageLocators.REPAIRS_DROP_DOWN_MENU)
        drop_down_menu_for_repairs_field.click()
        select_a_good_repair = self.browser.find_element(
            *BaCountryPropertyResidentialBuildingPageLocators.SELECT_REPAIRS)
        select_a_good_repair.click()
        assert self.browser.find_element(
            *BaCountryPropertyResidentialBuildingPageLocators.CHECKING_THE_SELECTED_REPAIRS).text == \
            "Хорошее состояние", " Значение в поле 'Состояние отделки' != Хорошее состояние "

    def select_heat_supply(self):
        """Выбор теплоснабжения"""
        assert self.is_element_present(
            *BaCountryPropertyResidentialBuildingPageLocators.HEAT_SUPPLY_DROP_DOWN_MENU), \
            " Поле 'Теплоснабжение' не отображается на странице' "
        drop_down_menu_for_heat_supply_field = self.browser.find_element(
            *BaCountryPropertyResidentialBuildingPageLocators.HEAT_SUPPLY_DROP_DOWN_MENU)
        drop_down_menu_for_heat_supply_field.click()
        select_no_heat_supply = self.browser.find_element(
            *BaCountryPropertyResidentialBuildingPageLocators.SELECT_HEAT_SUPPLY)
        select_no_heat_supply.click()
        assert self.browser.find_element(
            *BaCountryPropertyResidentialBuildingPageLocators.CHECKING_THE_SELECTED_HEAT_SUPPLY).text == \
            "Нет", " Значение в поле 'Теплоснабжение' != Нет "



