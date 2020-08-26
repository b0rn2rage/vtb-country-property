from .base_page import BasePage
from .locators import BaNewCountryPropertyResidentialBuildingPageLocators
from .locators import BaNewCountryPropertyLandPageLocators


class BaNewCountryPropertyLandPage(BasePage):
    """ Заполнение объекта №2 в новом отчете по ЖД. Тип объекта = ЗУ """
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
