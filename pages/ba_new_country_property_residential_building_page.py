from .base_page import BasePage
from .locators import BaNewCountryPropertyResidentialBuildingPageLocators
from selenium.webdriver.common.keys import Keys

class BaNewCountryPropertyResidentialBuildingPage(BasePage):
    """ Заполнение раздела 'Объект №1' в новом отчете по ЖД """

    def input_name_of_the_object(self):
        assert self.is_element_present(*BaNewCountryPropertyResidentialBuildingPageLocators.INPUT_NAME_OF_THE_OBJECT), \
            " Поле 'Наименование объекта (без учета адреса)' не отображается на странице "
        field_for_input_name_of_the_object = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.INPUT_NAME_OF_THE_OBJECT)
        field_for_input_name_of_the_object.click()
        field_for_input_name_of_the_object.send_keys("Home Sweet Home ^_^")

    def input_the_address_for_documents(self):
        assert self.is_element_present(
            *BaNewCountryPropertyResidentialBuildingPageLocators.INPUT_THE_ADDRESS_FOR_DOCUMENTS), \
            "Поле 'Адрес по документам' не отображается на странице "
        field_for_input_the_address_for_documents = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.INPUT_THE_ADDRESS_FOR_DOCUMENTS)
        field_for_input_the_address_for_documents.click()
        field_for_input_the_address_for_documents.send_keys("г Москва, ул Тестовская, д 1А")

    def input_fias_address(self):
        assert self.is_element_present(*BaNewCountryPropertyResidentialBuildingPageLocators.INPUT_FIAS_ADDRESS), \
            "Поле 'Адрес по ФИАС' не отображается на странице"
        field_for_input_fias_address = self.browser.find_element(*BaNewCountryPropertyResidentialBuildingPageLocators.INPUT_FIAS_ADDRESS)
        #field_for_input_fias_address.click()
        field_for_input_fias_address.send_keys("г Москва, ул Тестовская, д 1А")
        # is_element_presence в течение таймаута чекает подтянувшееся значение из КРОНЫ для поля 'Сотрудник банка'
        assert self.is_element_presence(
            *BaNewCountryPropertyResidentialBuildingPageLocators.SELECT_VALUE_IN_THE_FIELD_FIAS_ADDRESS), \
            " Введенный адрес не отображается в поле 'Адрес по ФИАС'. Возможно тормозит КРОНА "
        field_for_input_fias_address.send_keys(Keys.RETURN)
        #assert self.browser.find_element(*)

    def select_type_in_residential_building_tab(self):
        assert self.is_element_present(*BaNewCountryPropertyResidentialBuildingPageLocators.TYPE_DROP_DOWN_MENU), \
            " Поле 'Тип' не отображается на странице "
        assert self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.CHECKING_THE_SELECTED_TYPE), \
            " Выбранный тип недвижимости != Жилой садовый дом "
