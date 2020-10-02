from pages.base_page import BasePage
from krona_pages.krona_locators import KronaCountryPropertyReportCardPageLocators


class KronaReportCardGeneralInformationPage(BasePage):
    """Карточка отчета, вкладка 'Общая информация'."""

    def check_values_on_general_information_tab(self, status, flag_for_standard):
        assert self.is_element_presence(
            *KronaCountryPropertyReportCardPageLocators.REPORT_STATUS), \
            "Поле 'Статус отчета' не отображается на странице."
        report_status = self.browser.find_element(
            *KronaCountryPropertyReportCardPageLocators.REPORT_STATUS)
        report_flag_for_standard = self.browser.find_element(
            *KronaCountryPropertyReportCardPageLocators.FLAG_FOR_STANDARD)
        assert status.value in report_status.get_attribute('value'), f"Статус отчета != {status.value}"
        assert report_flag_for_standard.get_attribute('value') == flag_for_standard.value, \
            "Признак стандартного отчета проставлен не правильно"

    def go_to_the_tab_in_the_report_card(self, tab):
        """Переход по вкладкам в карточке отчета"""
        dict_with_the_names_of_the_tabs = \
            {
                'Общая информация': KronaCountryPropertyReportCardPageLocators.GENERAL_INFORMATION_TAB,
                'Объект 1': KronaCountryPropertyReportCardPageLocators.FIRST_OBJECT_TAB,
                'Объект 2': KronaCountryPropertyReportCardPageLocators.SECOND_OBJECT_TAB,
                'Документы': KronaCountryPropertyReportCardPageLocators.DOCUMENTS_TAB,
                'Фотографии': KronaCountryPropertyReportCardPageLocators.PHOTOS_TAB,
                'Верификация': KronaCountryPropertyReportCardPageLocators.VERIFICATION_TAB
            }
        selected_tab = dict_with_the_names_of_the_tabs[tab.value]
        self.browser.find_element(*selected_tab).click()