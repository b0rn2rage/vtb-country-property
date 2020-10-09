from pages.base_page import BasePage
from krona_pages.krona_locators import KronaCountryPropertyReportCardPageLocators
from krona_pages.krona_emuns.krona_enum_new_country_property import KronaCountryPropertyReportCardNameTab
from selenium.common.exceptions import NoSuchElementException
import os


class KronaCountryPropertyReportCardPage(BasePage):
    """Карточка отчета, все вкладки."""

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

    def check_values_after_ba(self, status, flag_for_standard):
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

    def lack_documents(self):
        """Активация чек-бокса 'Не хватает документов на коммуникации'."""
        assert self.is_element_present(*KronaCountryPropertyReportCardPageLocators.LACK_DOCUMENTS), \
            "Чек-бокс 'Не хватает документов на коммуникации' отсутсвует на странице."
        activate_checkbox = self.browser.find_element(*KronaCountryPropertyReportCardPageLocators.LACK_DOCUMENTS)
        activate_checkbox.click()

    def checking_values_after_srg_verification(self, status, result, lack_documents):
        """Проверка значений в карточке отчета после верифиикации."""
        assert self.is_element_visible(*KronaCountryPropertyReportCardPageLocators.REPORT_STATUS), \
            "Поле со статусом не отображается на странице"
        assert self.browser.find_element(*KronaCountryPropertyReportCardPageLocators.REPORT_STATUS).get_attribute(
            'value') == status.value, f'Статус отчета после верификации != {status.value}'
        KronaCountryPropertyReportCardPage.go_to_the_tab_in_the_report_card(
            self, KronaCountryPropertyReportCardNameTab.VERIFICATION)
        assert self.browser.find_element(*KronaCountryPropertyReportCardPageLocators.LACK_DOCUMENTS).get_attribute(
            'checked') == lack_documents.value, \
            f"Признак отсутствия документов != {lack_documents.value}"
        assert self.browser.find_element(*KronaCountryPropertyReportCardPageLocators.RESULT_ACCEPT).text == result.value, \
            f"Результат отчета после верификации != {result.value}"

    def checking_values_after_vtb_verification(self, status, result):
        """Проверка значений в карточке отчета после верифиикации."""
        assert self.is_element_visible(*KronaCountryPropertyReportCardPageLocators.REPORT_STATUS), \
            "Поле со статусом не отображается на странице"
        assert self.browser.find_element(*KronaCountryPropertyReportCardPageLocators.REPORT_STATUS).get_attribute(
            'value') == status.value, f'Статус отчета после верификации != {status.value}'
        KronaCountryPropertyReportCardPage.go_to_the_tab_in_the_report_card(
            self, KronaCountryPropertyReportCardNameTab.VERIFICATION)
        dict_with_results = \
            {
                'Принято': KronaCountryPropertyReportCardPageLocators.RESULT_ACCEPT,
                'Не принято': KronaCountryPropertyReportCardPageLocators.RESULT_NOT_ACCEPT
            }
        check_result = dict_with_results[result.value]
        assert self.browser.find_element(*check_result).text == result.value, \
            f"Результат после верификации != {result.value}"

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

    def input_new_price_in_the_verification_table(self, house_price, land_price=0):
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
            pass

    def input_new_adjust_price_in_the_decision_form(self, house_price, land_price=0):
        """Ввод скорректированной стоимости в таблицу 'Скорректировать цену'."""
        assert self.is_element_visible(
            *KronaCountryPropertyReportCardPageLocators.INPUT_ADJUST_PRICE), \
            "Поле для ввода новой скорректированной стоимости не отображается на странице"
        try:
            objects = self.browser.find_elements(*KronaCountryPropertyReportCardPageLocators.INPUT_ADJUST_PRICE)
            new_price_for_first_object = objects[0]
            new_price_for_first_object.send_keys(house_price)
            new_price_for_second_object = objects[1]
            new_price_for_second_object.send_keys(land_price)
        except NoSuchElementException:
            pass
        assert self.is_element_present(*KronaCountryPropertyReportCardPageLocators.CHANGE_PRICE), \
            "Кнопка 'Скорректировать' не отображается на странице"
        self.browser.find_element(*KronaCountryPropertyReportCardPageLocators.CHANGE_PRICE).click()

    def taking_decision(self, decision):
        """Нажатте кнопки 'Решение' при верификации за сотрудника банка."""
        assert self.is_element_present(*KronaCountryPropertyReportCardPageLocators.DECISION_BUTTON), \
            "Кнопка 'Решение' отсутствует на странице."
        self.browser.find_element(*KronaCountryPropertyReportCardPageLocators.DECISION_BUTTON).click()
        assert self.is_element_visible(*KronaCountryPropertyReportCardPageLocators.DECISION_FORM), \
            "Форма 'Решение' с кнопками Принять отчет/Скорректировать не отображается на странице"
        dict_with_decisions = \
            {
                'Принять отчет': KronaCountryPropertyReportCardPageLocators.APPROVE_BUTTON,
                'Скорректировать': KronaCountryPropertyReportCardPageLocators.ADJUST_BUTTON
            }
        decide = dict_with_decisions[decision.value]
        self.browser.find_element(*decide).click()
