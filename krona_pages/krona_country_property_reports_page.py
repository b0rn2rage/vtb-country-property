import time
from pages.base_page import BasePage
from krona_pages.krona_locators import KronaCountryPropertyReportsPageLocators


class KronaCountryPropertyReportsPage(BasePage):
    """В этом классе описывать все операции внутри карточки отчета ЖД."""

    def open_report_in_data_table(self, report_number):
        """Открыть карточку отчета из реестра отчетов по ЖД."""
        assert self.is_element_visible(*KronaCountryPropertyReportsPageLocators.DATA_TABLE, timeout=15), \
            "В реестре жилых домов не прогружается таблица с отчетами"
        assert self.is_element_present(*KronaCountryPropertyReportsPageLocators.REPORT_NUMBER), \
            "Фильтр по номеру отчета не отображается на странице"
        report_number_field = self.browser.find_element(*KronaCountryPropertyReportsPageLocators.REPORT_NUMBER)
        report_number_field.send_keys(report_number)
        show_table_button = self.browser.find_element(*KronaCountryPropertyReportsPageLocators.SHOW_TABLE)
        show_table_button.click()
        assert self.is_element_presence(*KronaCountryPropertyReportsPageLocators.RESULT_TABLE_PROCESSING), \
            "Реестр с отчетами по ЖД не успел прогрузиться после фильтрации"
        required_report = self.browser.find_element(
            *KronaCountryPropertyReportsPageLocators.REPORT_IN_THE_REGISTRY_AFTER_FILTERING)
        required_report.click()

