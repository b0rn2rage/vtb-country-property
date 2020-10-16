from enum import Enum

from pages.base_page import BasePage
from .ba_locators import BaCountryPropertyResidentialBuildingPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class BaCountryPropertyResidentialBuildingPage(BasePage):
    """Заполнение раздела с типом объекта = ЖД."""

    def input_name_of_the_object(self, name: str):
        input_name = self.browser.find_element(
            *BaCountryPropertyResidentialBuildingPageLocators.INPUT_NAME_OF_THE_OBJECT)
        input_name.click()
        input_name.send_keys(name)
        input_name.send_keys(Keys.TAB)
        assert self.browser.find_element(
            *BaCountryPropertyResidentialBuildingPageLocators.INPUT_NAME_OF_THE_OBJECT).text == \
            f"{name}", f"Значение в поле 'Наименование объекта...' не соответствует {name}"

    def select_wall_material(self, material: Enum):
        """Выбор материала стен"""
        drop_down_menu_for_wall_material_field = self.browser.find_element(
            *BaCountryPropertyResidentialBuildingPageLocators.WALL_MATERIAL_DROP_DOWN_MENU)
        drop_down_menu_for_wall_material_field.click()
        dict_with_wall_materials = \
            {
                'Кирпич': BaCountryPropertyResidentialBuildingPageLocators.SELECT_WALL_BRICK,
                'Панель': BaCountryPropertyResidentialBuildingPageLocators.SELECT_WALL_PANEL,
                'Монолит': BaCountryPropertyResidentialBuildingPageLocators.SELECT_WALL_MONOLITH,
                'Блок': BaCountryPropertyResidentialBuildingPageLocators.SELECT_WALL_BLOCK,
                'Дерево': BaCountryPropertyResidentialBuildingPageLocators.SELECT_WALL_WOOD,
                'Брус': BaCountryPropertyResidentialBuildingPageLocators.SELECT_WALL_BALK,
                'Каменные': BaCountryPropertyResidentialBuildingPageLocators.SELECT_WALL_STONE,
                'Каркасные': BaCountryPropertyResidentialBuildingPageLocators.SELECT_WALL_CARCASS,
                'Металлокаркасные панели/Легкие конструкции': BaCountryPropertyResidentialBuildingPageLocators.SELECT_WALL_METAL_FRAME_PANELS,
                'Монолит-кирпич': BaCountryPropertyResidentialBuildingPageLocators.SELECT_WALL_MONOLITH_BRICK,
                'СИП панели': BaCountryPropertyResidentialBuildingPageLocators.SELECT_WALL_SIP_PANELS

            }
        select_material = dict_with_wall_materials[material.value]
        self.browser.find_element(*select_material).click()
        assert self.browser.find_element(By.XPATH, f"//div[contains(text(), '{material.value}')]").text == \
            material.value, f"Значение в поле 'Материал стен' != {material.value}."

    def select_repairs(self, repairs: Enum):
        """Выбор состояния отделки"""
        drop_down_menu_for_repairs_field = self.browser.find_element(
            *BaCountryPropertyResidentialBuildingPageLocators.REPAIRS_DROP_DOWN_MENU)
        drop_down_menu_for_repairs_field.click()
        dict_with_repairs = \
            {
                'Без отделки': BaCountryPropertyResidentialBuildingPageLocators.SELECT_REPAIRS_WITHOUT,
                'Под чистовую отделку': BaCountryPropertyResidentialBuildingPageLocators.SELECT_REPAIRS_CLEAN,
                'Среднее (жилое) состояние': BaCountryPropertyResidentialBuildingPageLocators.SELECT_REPAIRS_AVERAGE,
                'Хорошее состояние': BaCountryPropertyResidentialBuildingPageLocators.SELECT_REPAIRS_GOOD,
                'Отличное (евро) состояние': BaCountryPropertyResidentialBuildingPageLocators.SELECT_REPAIRS_EXCELLENT
            }
        select_condition = dict_with_repairs[repairs.value]
        self.browser.find_element(*select_condition).click()
        assert self.browser.find_element(
            By.XPATH, f"//div[contains(text(), '{repairs.value}')]").text == repairs.value, \
            f"Значение в поле 'Состояние отделки' != {repairs.value}."

    def select_heat_supply(self, heat_supply: Enum):
        """Выбор теплоснабжения"""
        drop_down_menu_for_heat_supply_field = self.browser.find_element(
            *BaCountryPropertyResidentialBuildingPageLocators.HEAT_SUPPLY_DROP_DOWN_MENU)
        drop_down_menu_for_heat_supply_field.click()
        dict_with_heat_supply = \
            {
                'Нет': BaCountryPropertyResidentialBuildingPageLocators.SELECT_HEAT_SUPPLY_NO,
                'Есть, автономное': BaCountryPropertyResidentialBuildingPageLocators.SELECT_HEAT_SUPPLY_AUTONOMOUS,
                'Есть, центральное': BaCountryPropertyResidentialBuildingPageLocators.SELECT_HEAT_SUPPLY_CENTRAL
            }
        select_heat = dict_with_heat_supply[heat_supply.value]
        self.browser.find_element(*select_heat).click()
        assert self.browser.find_element(
            *BaCountryPropertyResidentialBuildingPageLocators.CHECKING_THE_SELECTED_HEAT_SUPPLY).text == \
            heat_supply.value, f"Значение в поле 'Теплоснабжение' != {heat_supply.value}"



