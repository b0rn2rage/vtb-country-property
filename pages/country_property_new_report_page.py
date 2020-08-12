from .base_page import BasePage
from selenium.webdriver.support.ui import Select
from .locators import BaCountryPropertyNewReportPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


class CountryPropertyNewReport(BasePage):
    """ Заполнить раздел 'Общая информация' """

    def close_modal_popup(self):
        """ Закрыть модальные окна на входе в новый отчет """
        assert WebDriverWait(self.browser, 4).until(EC.visibility_of_element_located(
            BaCountryPropertyNewReportPageLocators.MODAL_POPUP)), "Всплывающее окно 'ГОСТ Р' не появилось на " \
                                                                  "странице или не успело прогрузиться"
        button_for_closing_modal_popup = self.browser.find_element(
            *BaCountryPropertyNewReportPageLocators.CLOSE_MODAL_POPUP)
        button_for_closing_modal_popup.click()

    def go_to_photos_and_documents_from_general_information_tab(self):
        """ Переход из раздела 'Общая информация' в раздел 'Фотографии и документы' """
        self.browser.find_element(
            *BaCountryPropertyNewReportPageLocators.FROM_GENERAL_TAB_TO_PHOTOS_AND_DOCUMENTS_TAB).click()

    def input_full_name_of_the_borrower_customer_in_the_general_information_tab(self):
        """ Ввод ФИО заемщика/заказчика в поле 'ФИО Заемщика/Заказчика' """
        assert self.is_element_present(
            *BaCountryPropertyNewReportPageLocators.INPUT_FULL_NAME_OF_THE_BORROWER_CUSTOMER), \
            "Поле 'ФИО Заемщика/Заказчика' отсутствует на странице"
        field_for_input_full_name_of_the_borrower_customer = self.browser.find_element(
            *BaCountryPropertyNewReportPageLocators.INPUT_FULL_NAME_OF_THE_BORROWER_CUSTOMER)
        field_for_input_full_name_of_the_borrower_customer.click()
        field_for_input_full_name_of_the_borrower_customer.send_keys('Рандомное Физическое Лицо')

    def input_report_number_in_the_general_information_tab(self):
        """ Ввод номера отчета в поле 'Номер отчета' """
        assert self.is_element_present(*BaCountryPropertyNewReportPageLocators.INPUT_REPORT_NUMBER), \
            "Поле 'Номер отчета' отсутствует на странице"
        field_for_input_report_number = self.browser.find_element(
            *BaCountryPropertyNewReportPageLocators.INPUT_REPORT_NUMBER)
        field_for_input_report_number.click()
        field_for_input_report_number.send_keys('autotest_vtb_country_property ' + self.current_date())

    def attach_photos_in_photos_and_documents_tab(self):
        """ Приложить фотографии в разделе 'Фото и документы' """

    def select_bank_in_the_general_information_tab(self):
        """ Выбор банка 'ВТБ' в поле 'Банк' """
        assert self.is_element_present(*BaCountryPropertyNewReportPageLocators.BANK_DROP_DOWN_MENU), \
            "Поле 'Банк' отсутствует на странице"
        drop_down_menu_for_the_bank_field = self.browser.find_element(
            *BaCountryPropertyNewReportPageLocators.BANK_DROP_DOWN_MENU)
        drop_down_menu_for_the_bank_field.click()
        select_bank_vtb = self.browser.find_element(*BaCountryPropertyNewReportPageLocators.SELECT_BANK)
        select_bank_vtb.click()

    def select_department_in_the_general_information_tab(self):
        """ Выбор департамента 'Ипотека' в поле 'Департамент' """
        assert self.is_element_present(*BaCountryPropertyNewReportPageLocators.DEPARTMENT_DROP_DOWN_MENU), \
            "Поле 'Департамент' отсутствует на странице"
        drop_down_menu_for_the_department_field = self.browser.find_element(
            *BaCountryPropertyNewReportPageLocators.DEPARTMENT_DROP_DOWN_MENU)
        drop_down_menu_for_the_department_field.click()
        select_mortgage_department = self.browser.find_element(
            *BaCountryPropertyNewReportPageLocators.SELECT_DEPARTMENT)
        select_mortgage_department.click()

    def select_bank_employee_in_the_general_information_tab(self):
        """ Ввод сотрудника банка в поле 'Сотрудник банка' """
        assert self.is_element_present(*BaCountryPropertyNewReportPageLocators.BANK_EMPLOYEE_DROP_DOWN_MENU), \
            "Поле 'Сотрудник банка' отсутствует на странице"
        drop_down_menu_for_bank_employee = self.browser.find_element(
            *BaCountryPropertyNewReportPageLocators.BANK_EMPLOYEE_DROP_DOWN_MENU)
        drop_down_menu_for_bank_employee.click()
        field_for_input_bank_employee = self.browser.find_element(
            *BaCountryPropertyNewReportPageLocators.INPUT_BANK_EMPLOYEE)
        field_for_input_bank_employee.send_keys('autotest-country-property-vtb@test.ru')
        field_for_input_bank_employee.send_keys(Keys.RETURN)

    def select_report_date_in_the_general_information_tab(self):
        """ Выбор текущей даты для поля 'Дата отчета' """
        assert self.is_element_present(*BaCountryPropertyNewReportPageLocators.REPORT_DATE), \
            "Поле 'Дата отчета' отсутствует на странице"
        open_calendar = self.browser.find_element(*BaCountryPropertyNewReportPageLocators.REPORT_DATE)
        open_calendar.click()
        select_current_date_in_calendar = self.browser.find_element(
            *BaCountryPropertyNewReportPageLocators.SELECT_CURRENT_REPORT_DATE)
        select_current_date_in_calendar.click()

    def select_valuation_date_in_the_general_information_tab(self):
        """ Выбор текущей даты для поля 'Дата оценки' """
        assert self.is_element_present(*BaCountryPropertyNewReportPageLocators.VALUATION_DATE), \
            "Поле 'Дата оценки' отсутствует на странице"
        open_calendar = self.browser.find_element(*BaCountryPropertyNewReportPageLocators.VALUATION_DATE)
        open_calendar.click()
        select_current_date_in_calendar = self.browser.find_element(
            *BaCountryPropertyNewReportPageLocators.SELECT_CURRENT_VALUATION_DATE)
        select_current_date_in_calendar.click()

    def select_signer_in_the_general_information_tab(self):
        """
        Выбор подписанта в поле 'Подписант от лица организации'.
        Если подписант в организации один (как в данном случае), то поле заполняется в БО автоматически.
        Включать этот метод в тестовый сценарий только в случае появления других подписантов и оценщиков.
        """
        assert self.is_element_present(*BaCountryPropertyNewReportPageLocators.SIGNER_DROP_DOWN_MENU), \
            "Поле 'Подписант от лица организации отсутствует на странице' "
        drop_down_menu_for_the_signer_field = self.browser.find_element(
            *BaCountryPropertyNewReportPageLocators.SIGNER_DROP_DOWN_MENU)
        drop_down_menu_for_the_signer_field.click()
        select_signer_from_organization = self.browser.find_element(
            *BaCountryPropertyNewReportPageLocators.SELECT_SIGNER)
        select_signer_from_organization.click()

    def select_file_in_the_general_information_tab(self):
        """
        Прикладывание файла с отчетом об оценке. Проверка всех трех типов файлов (doc, docx, pdf)
        Проверка на загрузку/удаление прикрепленных файлов.
        """
        scroll_to_select_file = self.browser.find_element(*BaCountryPropertyNewReportPageLocators.FOOTER)
        actions = ActionChains(self.browser)
        actions.move_to_element(scroll_to_select_file).perform()
        files = ["\\Test report doc.doc", "\\Test report pdf.pdf", "\\Test report docx.docx"]
        for file in files:
            input_file_report = self.browser.find_element(*BaCountryPropertyNewReportPageLocators.INPUT_FILE)
            input_file_report.send_keys(os.getcwd() + file)
            # Когда файл начинает прикрепляться, то появляется прогресс бар. Метод is_file_attached ждет 10 секунд
            # пока этот прогресс бар пропадет. Если не пропадает - assert = False
            assert self.is_file_attached(
                *BaCountryPropertyNewReportPageLocators.UPLOAD_PROGRESS_HIDE), \
                "Файл не может прикрепиться. Прогресс бар не пропадает."
            if file[0] or file[1]:
                del_file = self.browser.find_element(*BaCountryPropertyNewReportPageLocators.DELETE_FILE_BUTTON).click()