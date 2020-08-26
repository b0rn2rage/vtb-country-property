import os
import time
import datetime
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage
from .locators import BaNewCountryPropertyGeneralInformationPageLocators
from selenium.webdriver.common.by import By


class BaCountryPropertyNewReportGeneralInformationPage(BasePage):
    """ Заполнение раздела 'Общая информация' в новом отчете по ЖД """

    def close_modal_popup(self):
        """ Закрыть модальные окна на входе в новый отчет """
        while self.is_element_visible(*BaNewCountryPropertyGeneralInformationPageLocators.MODAL_POPUP, timeout=2):
            assert self.is_element_visible(
                *BaNewCountryPropertyGeneralInformationPageLocators.MODAL_POPUP), \
                'Всплывающее окно с ГОСТом не успело прогрузиться'
            button_for_closing_modal_popup = self.browser.find_element(
                *BaNewCountryPropertyGeneralInformationPageLocators.CLOSE_MODAL_POPUP)
            button_for_closing_modal_popup.click()

    def go_to_photos_and_documents_tab_from_general_information_tab(self):
        """ Переход из раздела 'Общая информация' в раздел 'Фотографии и документы' """
        self.browser.find_element(
            *BaNewCountryPropertyGeneralInformationPageLocators.FROM_GENERAL_TAB_TO_PHOTOS_AND_DOCUMENTS_TAB).click()

    def input_full_name_of_the_borrower_customer_in_the_general_information_tab(self):
        """ Ввод ФИО заемщика/заказчика в поле 'ФИО Заемщика/Заказчика' """
        assert self.is_element_present(
            *BaNewCountryPropertyGeneralInformationPageLocators.INPUT_FULL_NAME_OF_THE_BORROWER_CUSTOMER), \
            "Поле 'ФИО Заемщика/Заказчика' отсутствует на странице"
        field_for_input_full_name_of_the_borrower_customer = self.browser.find_element(
            *BaNewCountryPropertyGeneralInformationPageLocators.INPUT_FULL_NAME_OF_THE_BORROWER_CUSTOMER)
        field_for_input_full_name_of_the_borrower_customer.send_keys('Рандомное Физическое Лицо')
        assert field_for_input_full_name_of_the_borrower_customer.get_attribute('value') == \
            'Рандомное Физическое Лицо', \
            " Значение в поле 'ФИО Заемщика/Заказчика' не соответствует введенному "

    def input_report_number_in_the_general_information_tab(self):
        """ Ввод номера отчета в поле 'Номер отчета' """
        assert self.is_element_present(*BaNewCountryPropertyGeneralInformationPageLocators.INPUT_REPORT_NUMBER), \
            "Поле 'Номер отчета' отсутствует на странице"
        field_for_input_report_number = self.browser.find_element(
            *BaNewCountryPropertyGeneralInformationPageLocators.INPUT_REPORT_NUMBER)
        report_number = 'autotest_vtb_country_property ' + str(self.current_date())
        field_for_input_report_number.send_keys(report_number)
        assert field_for_input_report_number.get_attribute('value') == report_number, \
            " Значение в поле 'Номер отчета' не соответствует введенному "

    def select_bank_in_the_general_information_tab(self):
        """ Выбор банка 'ВТБ' в поле 'Банк' """
        assert self.is_element_present(*BaNewCountryPropertyGeneralInformationPageLocators.BANK_DROP_DOWN_MENU), \
            "Поле 'Банк' отсутствует на странице"
        drop_down_menu_for_the_bank_field = self.browser.find_element(
            *BaNewCountryPropertyGeneralInformationPageLocators.BANK_DROP_DOWN_MENU)
        drop_down_menu_for_the_bank_field.click()
        select_bank_vtb = self.browser.find_element(*BaNewCountryPropertyGeneralInformationPageLocators.SELECT_BANK)
        select_bank_vtb.click()
        assert self.browser.find_element(
            *BaNewCountryPropertyGeneralInformationPageLocators.CHECKING_THE_SELECTED_BANK).text == 'ВТБ', \
            'Значение в поле Банк != ВТБ'

    def select_department_in_the_general_information_tab(self):
        """ Выбор департамента 'Ипотека' в поле 'Департамент' """
        assert self.is_element_present(*BaNewCountryPropertyGeneralInformationPageLocators.DEPARTMENT_DROP_DOWN_MENU), \
            "Поле 'Департамент' отсутствует на странице"
        drop_down_menu_for_the_department_field = self.browser.find_element(
            *BaNewCountryPropertyGeneralInformationPageLocators.DEPARTMENT_DROP_DOWN_MENU)
        drop_down_menu_for_the_department_field.click()
        select_mortgage_department = self.browser.find_element(
            *BaNewCountryPropertyGeneralInformationPageLocators.SELECT_DEPARTMENT)
        select_mortgage_department.click()
        assert self.browser.find_element(
            *BaNewCountryPropertyGeneralInformationPageLocators.CHECKING_THE_SELECTED_DEPARTMENT).text == 'Ипотека', \
            'Значение в поле Департамент != Ипотека'

    def select_bank_employee_in_the_general_information_tab(self):
        """ Ввод сотрудника банка в поле 'Сотрудник банка' """
        assert self.is_element_present(
            *BaNewCountryPropertyGeneralInformationPageLocators.BANK_EMPLOYEE_DROP_DOWN_MENU), \
            "Поле 'Сотрудник банка' отсутствует на странице"
        drop_down_menu_for_bank_employee = self.browser.find_element(
            *BaNewCountryPropertyGeneralInformationPageLocators.BANK_EMPLOYEE_DROP_DOWN_MENU)
        drop_down_menu_for_bank_employee.click()
        field_for_input_bank_employee = self.browser.find_element(
            *BaNewCountryPropertyGeneralInformationPageLocators.INPUT_BANK_EMPLOYEE)
        field_for_input_bank_employee.send_keys('autotest-country-property-vtb@test.ru')
        # is_element_presence в течение таймаута чекает подтянувшееся значение из КРОНЫ для поля 'Сотрудник банка'
        assert self.is_element_presence(
            *BaNewCountryPropertyGeneralInformationPageLocators.SELECT_A_VALUE_IN_THE_FIELD_EMPLOYEE_OF_THE_BANK), \
            " Введенный сотрудник банка не отображается в поле 'Сотрудник банка'. Возможно тормозит КРОНА "
        field_for_input_bank_employee.send_keys(Keys.RETURN)
        assert self.browser.find_element(
            *BaNewCountryPropertyGeneralInformationPageLocators.CHECKING_THE_SELECTED_BANK_EMPLOYEE).text == \
            'Селениумов Питон (autotest-country-property-vtb@test.ru)', \
            ' Значение в поле Сотрудник банка != autotest-country-property-vtb@test.ru '

    def select_report_date_in_the_general_information_tab(self):
        """ Выбор текущей даты для поля 'Дата отчета' """
        assert self.is_element_present(*BaNewCountryPropertyGeneralInformationPageLocators.REPORT_DATE_FIELD), \
            "Поле 'Дата отчета' отсутствует на странице"
        open_calendar = self.browser.find_element(*BaNewCountryPropertyGeneralInformationPageLocators.REPORT_DATE_FIELD)
        open_calendar.click()
        select_current_date_in_calendar = self.browser.find_element(
            *BaNewCountryPropertyGeneralInformationPageLocators.SELECT_CURRENT_REPORT_DATE)
        select_current_date_in_calendar.click()
        assert self.browser.find_element(
            *BaNewCountryPropertyGeneralInformationPageLocators.SELECT_VALUE_IN_REPORT_DATE_FIELD).get_attribute(
            'value') == self.current_date().strftime(
            "%d.%m.%Y"), " Значение в поле 'Дата отчета' не соответствует текущей дате "

    def select_valuation_date_in_the_general_information_tab(self):
        """ Выбор текущей даты для поля 'Дата оценки' """
        assert self.is_element_present(*BaNewCountryPropertyGeneralInformationPageLocators.VALUATION_DATE_FIELD), \
            "Поле 'Дата оценки' отсутствует на странице"
        open_calendar = self.browser.find_element(
            *BaNewCountryPropertyGeneralInformationPageLocators.VALUATION_DATE_FIELD)
        open_calendar.click()
        select_current_date_in_calendar = self.browser.find_element(
            *BaNewCountryPropertyGeneralInformationPageLocators.SELECT_CURRENT_VALUATION_DATE)
        select_current_date_in_calendar.click()
        assert self.browser.find_element(
            *BaNewCountryPropertyGeneralInformationPageLocators.SELECT_VALUE_IN_VALUATION_DATE_FIELD).get_attribute(
            'value') == self.current_date().strftime(
            "%d.%m.%Y"), " Значение в поле 'Дата оценки' не соответствует текущей дате "

    def select_signer_in_the_general_information_tab(self):
        """
        Выбор подписанта в поле 'Подписант от лица организации'.
        Если подписант в организации один (как в данном случае), то поле заполняется в БО автоматически.
        Включать этот метод в тестовый сценарий только в случае появления других подписантов и оценщиков.
        """
        assert self.is_element_present(*BaNewCountryPropertyGeneralInformationPageLocators.SIGNER_DROP_DOWN_MENU), \
            "Поле 'Подписант от лица организации отсутствует на странице' "
        drop_down_menu_for_the_signer_field = self.browser.find_element(
            *BaNewCountryPropertyGeneralInformationPageLocators.SIGNER_DROP_DOWN_MENU)
        drop_down_menu_for_the_signer_field.click()
        select_signer_from_organization = self.browser.find_element(
            *BaNewCountryPropertyGeneralInformationPageLocators.SELECT_SIGNER)
        select_signer_from_organization.click()

    def select_file_in_the_general_information_tab(self):
        """
        Прикладывание файла с отчетом об оценке. Проверка всех трех типов файлов (doc, docx, pdf)
        Проверка на загрузку/удаление прикрепленных файлов.
        """
        scroll_to_select_file = self.browser.find_element(*BaNewCountryPropertyGeneralInformationPageLocators.FOOTER)
        actions = ActionChains(self.browser)
        actions.move_to_element(scroll_to_select_file).perform()
        input_file_report = self.browser.find_element(
            *BaNewCountryPropertyGeneralInformationPageLocators.INPUT_FILE)
        #file = ["\\samples\\test pdf.pdf", "\\samples\\test doc.doc", "\\samples\\test docx.docx"]
        file = "\\samples\\test pdf.pdf"
        input_file_report.send_keys(os.getcwd() + file)
        #Когда файл начинает прикрепляться, то появляется прогресс бар. Метод is_file_attached ждет 10 секунд
        # пока этот прогресс бар пропадет. Если не пропадает - assert = False
        assert self.is_file_attached(
            *BaNewCountryPropertyGeneralInformationPageLocators.UPLOAD_PROGRESS_HIDE), \
            f"Файл {file} не может прикрепиться. Прогресс бар не пропадает."
