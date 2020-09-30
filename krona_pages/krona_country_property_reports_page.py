from pages.base_page import BasePage
from krona_pages.krona_locators import KronaCountryPropertyReportsLocators
from ba_pages.ba_new_country_property_general_information_page import BaNewCountryPropertyGeneralInformationPage


class KronaCountryPropertyReportsPage(BasePage):
    """В этом классе описывать все операции внутри карточки отчета ЖД."""

    def open_country_report_in_data_table(self, report_number):
        """Открыть карточку отчета из реестра отчетов по ЖД."""
        assert self.is_element_visible(*KronaCountryPropertyReportsLocators.DATA_TABLE, timeout=15), \
            "В реестре жилых домов не прогружается таблица с отчетами"
        assert self.is_element_present(*KronaCountryPropertyReportsLocators.REPORT_NUMBER), \
            "Фильтр по номеру отчета не отображается на странице"
        report_number_field = self.browser.find_element(*KronaCountryPropertyReportsLocators.REPORT_NUMBER)
        report_number_field.send_keys(report_number)


