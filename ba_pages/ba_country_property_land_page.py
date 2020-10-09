from pages.base_page import BasePage
from .ba_locators import BaCountryPropertyLandPageLocators
from selenium.webdriver.common.by import By


class BaCountryPropertyLandPage(BasePage):
    """Заполнение объекта с типом = ЗУ."""
    def input_cadastral_number(self, number):
        """Заполнение поля 'Кадастровый номер'."""
        field_for_input_cadastral_number = self.browser.find_element(
            *BaCountryPropertyLandPageLocators.INPUT_CADASTRAL_NUMBER)
        field_for_input_cadastral_number.send_keys(number)
        assert field_for_input_cadastral_number.get_attribute('value') == number, \
            "Значение в поле 'Кадастровый номер' не совпадает с введенным."

    def input_type_of_permitted_use(self, type_of_use):
        """Заполнения поля 'Вид разрешенного использования'."""
        field_for_input_type_of_permitted_use = self.browser.find_element(
            *BaCountryPropertyLandPageLocators.INPUT_TYPE_OF_PERMITTED_USE)
        field_for_input_type_of_permitted_use.send_keys(type_of_use)
        assert field_for_input_type_of_permitted_use.get_attribute('value') == type_of_use, \
            f"Значение в поле 'Вид разрешенного использования' не соответствует {type_of_use}."

    def select_category(self, category):
        """Выбрать категорию."""
        drop_down_menu_for_category_field = self.browser.find_element(
            *BaCountryPropertyLandPageLocators.CATEGORY_DROP_DOWN_MENU)
        drop_down_menu_for_category_field.click()
        dict_with_categories = \
            {
                'Земли населённых пунктов (земли поселений)': BaCountryPropertyLandPageLocators.SELECT_CATEGORY_SETTLEMENT,
                'Земли сельскохозяйственного назначения': BaCountryPropertyLandPageLocators.SELECT_CATEGORY_AGRICULTURAL,
                'Земли промышленности и иного специального назначения': BaCountryPropertyLandPageLocators.SELECT_CATEGORY_INDUSTRY,
                'Земли особо охраняемых территорий и объектов': BaCountryPropertyLandPageLocators.SELECT_CATEGORY_GUARDED,
                'Земли лесного фонда': BaCountryPropertyLandPageLocators.SELECT_CATEGORY_FOREST,
                'Земли водного фонда': BaCountryPropertyLandPageLocators.SELECT_CATEGORY_WATER,
                'Земли запаса': BaCountryPropertyLandPageLocators.SELECT_CATEGORY_STOCK
            }
        selected_category = dict_with_categories[category.value]
        self.browser.find_element(*selected_category).click()
        assert self.browser.find_element(
            By.XPATH, f"//label[contains(text(),'Категория')]/..//div[contains(text(), '{category.value}')]").text == \
            category.value, f"Значение в поле 'Категория' не соответствует {category.value}."
