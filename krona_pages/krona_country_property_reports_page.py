from pages.base_page import BasePage
from krona_pages.krona_locators import KronaCountryPropertyReportsLocators
import time



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
        assert self.is_element_present(*KronaCountryPropertyReportsLocators.SHOW_TABLE), \
            "Кнопка 'Показать' не отображается на странице."
        show_table_button = self.browser.find_element(*KronaCountryPropertyReportsLocators.SHOW_TABLE)
        show_table_button.click()
        assert self.is_element_presence(*KronaCountryPropertyReportsLocators.RESULT_TABLE_PROCESSING), \
            "Реестр с отчетами по ЖД не успел прогрузиться после фильтрации"
        required_report = self.browser.find_element(
            *KronaCountryPropertyReportsLocators.REPORT_IN_THE_REGISTRY_AFTER_FILTERING)
        required_report.click()
