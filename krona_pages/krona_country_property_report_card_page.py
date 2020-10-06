from pages.base_page import BasePage
from krona_pages.krona_locators import KronaCountryPropertyReportCardPageLocators
from krona_pages.krona_emuns.krona_enum_new_country_property import CountryPropertyReportCardNameTab
from selenium.common.exceptions import NoSuchElementException
import os


class KronaReportCardGeneralInformationPage(BasePage):
    """Карточка отчета, вкладка 'Общая информация'."""

    def attach_an_expert_calculation(self):
        """Прикрепить excel файл с расчетом эксперта."""
        assert self.is_element_present(
            *KronaCountryPropertyReportCardPageLocators.BUTTON_FOR_ATTACH_EXPERT_CALCULATION), \
            "Кнопка 'Загрузить файлы' отсутствует на странице"
        input_expert_calculation = self.browser.find_element(
            *KronaCountryPropertyReportCardPageLocators.BUTTON_FOR_ATTACH_EXPERT_CALCULATION)
        file = "\\samples\\test xlsx.xlsx"
        input_expert_calculation.send_keys(os.getcwd() + file)
        assert self.is_element_presence(*KronaCountryPropertyReportCardPageLocators.PROGRESS_BAR_FINISHED_DOWNLOADING),\
            "Файл с расчетом эксперта не загрузился."

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
            "Признак стандартного отчета проставлен не правильно."

    def checking_lack_documents(self):
        """Активация чек-бокса 'Не хватает документов на коммуникации'."""
        assert self.is_element_present(*KronaCountryPropertyReportCardPageLocators.LACK_DOCUMENTS), \
            "Чек-бокс 'Не хватает документов на коммуникации' отсутсвует на странице."
        activate_checkbox = self.browser.find_element(*KronaCountryPropertyReportCardPageLocators.LACK_DOCUMENTS)
        activate_checkbox.click()

    def checking_values_after_verification(self, status, result, lack_documents):
        """Проверка значений в карточке отчета после верифиикации."""
        assert self.browser.find_element(*KronaCountryPropertyReportCardPageLocators.REPORT_STATUS).get_attribute(
            'value') == status.value, f'Статус отчета после верификации != {status.value}'
        KronaReportCardGeneralInformationPage.go_to_the_tab_in_the_report_card(
            self, CountryPropertyReportCardNameTab.VERIFICATION)
        assert self.browser.find_element(*KronaCountryPropertyReportCardPageLocators.LACK_DOCUMENTS).get_attribute(
            'checked') == lack_documents.value, \
            f"Признак отсутствия документов != {lack_documents.value}"
        assert self.browser.find_element(*KronaCountryPropertyReportCardPageLocators.RESULT).text == result.value, \
            f"Результат отчета после верификации != {result.value}"

    def click_the_verification_button(self):
        """Нажатие кнопки 'Верифицировать'."""
        assert self.is_element_present(*KronaCountryPropertyReportCardPageLocators.VERIFICATION_BUTTON), \
            "Кнопка 'Верифицировать' отсутствует на странице."
        button_for_verification = self.browser.find_element(
            *KronaCountryPropertyReportCardPageLocators.VERIFICATION_BUTTON)
        button_for_verification.click()

    def go_to_the_tab_in_the_report_card(self, tab):
        """Переход по вкладкам в карточке отчета."""
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

    def input_new_price_in_the_table(self, house_price, land_price=0):
        """Ввод новой стоимости в таблицу 'Верифицированная стоимость'."""
        assert self.is_element_present(*KronaCountryPropertyReportCardPageLocators.INPUT_PRICE_FOR_FIRST_OBJECT), \
            "Поле для ввода новой стоимости отсутствует в таблице"
        try:
            new_price_for_first_object = self.browser.find_element(
                *KronaCountryPropertyReportCardPageLocators.INPUT_PRICE_FOR_FIRST_OBJECT)
            new_price_for_first_object.send_keys(house_price)
            new_price_for_second_object = self.browser.find_element(
                *KronaCountryPropertyReportCardPageLocators.INPUT_PRICE_FOR_SECOND_OBJECT)
            new_price_for_second_object.send_keys(land_price)
        except NoSuchElementException:
            print('Поле для ввода не найдено')
