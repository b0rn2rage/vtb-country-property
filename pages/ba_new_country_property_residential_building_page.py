from .base_page import BasePage
from .locators import BaNewCountryPropertyResidentialBuildingPageLocators


class BaNewCountryPropertyResidentialBuildingPage(BasePage):
    """ Заполнение раздела 'Объект №1' в новом отчете по ЖД """

    def select_type_in_residential_building_tab(self):
        assert self.is_element_present(*BaNewCountryPropertyResidentialBuildingPageLocators.TYPE_DROP_DOWN_MENU), \
            " Поле 'Тип' не отображается на странице "
