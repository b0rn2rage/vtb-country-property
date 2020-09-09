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

    def input_market_price_of_the_object(self):
        """ Заполнение поля 'Рычноная стоимость объекта оценки' """
        assert self.is_element_present(
            *BaNewCountryPropertyResidentialBuildingPageLocators.MARKET_PRICE_OF_THE_OBJECT), \
            " Поле 'Рыночная стоимость объекта оценки' не отображается на странице "
        field_for_input_market_price_of_the_object = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.MARKET_PRICE_OF_THE_OBJECT)
        field_for_input_market_price_of_the_object.send_keys(DataBankAppraiser.VtbData.Moscow_low_price_land)
        assert field_for_input_market_price_of_the_object.get_attribute('value') == \
            DataBankAppraiser.VtbData.Moscow_low_price_land, \
            "Значение в поле 'Рыночная стоимость объекта оценки' не соответствует введенному"

    def select_type_in_land_tab(self):
        """ Выбрать тип недвижимости = ЗУ """
        assert self.is_element_present(*BaNewCountryPropertyResidentialBuildingPageLocators.TYPE_DROP_DOWN_MENU), \
            " Поле 'Тип' не отображается на странице "
        drop_down_menu_for_type_field = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.TYPE_DROP_DOWN_MENU)
        drop_down_menu_for_type_field.click()
        select_land_type = self.browser.find_element(*BaNewCountryPropertyLandPageLocators.SELECT_TYPE_IS_LAND)
        select_land_type.click()
        assert self.browser.find_element(*BaNewCountryPropertyLandPageLocators.CHECK_TYPE_IS_LAND), \
            " Выбранный тип недвижимости != Земельный участок "

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
