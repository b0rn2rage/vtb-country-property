from pages.base_page import BasePage
from .ba_locators import BaNewCountryPropertyResidentialBuildingPageLocators
from .ba_locators import BaNewCountryPropertyLandPageLocators
from options.data import DataBankAppraiser


class BaNewCountryPropertyLandPage(BasePage):
    """ Заполнение объекта №2 в новом отчете по ЖД. Тип объекта = ЗУ """
    def input_cadastral_number(self):
        """ Заполнение поля 'Кадастровый номер' """
        assert self.is_element_present(*BaNewCountryPropertyLandPageLocators.INPUT_CADASTRAL_NUMBER), \
            " Поле 'Кадастровый номер' отсутствует на странице "
        field_for_input_cadastral_number = self.browser.find_element(
            *BaNewCountryPropertyLandPageLocators.INPUT_CADASTRAL_NUMBER)
        field_for_input_cadastral_number.send_keys("50:16:0502056:115")
        assert field_for_input_cadastral_number.get_attribute('value') == "50:16:0502056:115", \
            " Значение в поле 'Кадастровый номер' не совпадает с введенным "

    def input_type_of_permitted_use(self):
        """ Заполнения поля 'Вид разрешенного использования' """
        assert self.is_element_present(*BaNewCountryPropertyLandPageLocators.INPUT_TYPE_OF_PERMITTED_USE), \
            "Поле 'Вид разрешенного использования' не отображается на странице "
        field_for_input_type_of_permitted_use = self.browser.find_element(
            *BaNewCountryPropertyLandPageLocators.INPUT_TYPE_OF_PERMITTED_USE)
        field_for_input_type_of_permitted_use.send_keys("Для индивидуального жилищного строительства")
        assert field_for_input_type_of_permitted_use.get_attribute(
            'value') == "Для индивидуального жилищного строительства", \
            " Значение в поле 'Вид разрешенного использования' не соответствует введенному "

    def select_category(self):
        """ Выбрать категорию = """
        assert self.is_element_present(*BaNewCountryPropertyLandPageLocators.CATEGORY_DROP_DOWN_MENU), \
            " Поле 'Категория' отсутствует на странице"
        drop_down_menu_for_category_field = self.browser.find_element(
            *BaNewCountryPropertyLandPageLocators.CATEGORY_DROP_DOWN_MENU)
        drop_down_menu_for_category_field.click()
        select_lands_of_localities = self.browser.find_element(*BaNewCountryPropertyLandPageLocators.SELECT_CATEGORY)
        select_lands_of_localities.click()
        assert self.browser.find_element(*BaNewCountryPropertyLandPageLocators.CHECKING_THE_SELECTED_CATEGORY).text == \
            "Земли населённых пунктов (земли поселений)", \
            "Значение в поле 'Категория' не соответствует выбранному"
