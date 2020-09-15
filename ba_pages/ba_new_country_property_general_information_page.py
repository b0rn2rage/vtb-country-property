import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from .ba_locators import BaNewCountryPropertyGeneralInformationPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


class BaCountryPropertyNewReportGeneralInformationPage(BasePage):
    """ Заполнение раздела 'Общая информация' в новом отчете по ЖД """

    def close_modal_popup(self):
        """ Закрыть модальные окна на входе в новый отчет """
        try:
            while WebDriverWait(self.browser, timeout=3).until(
                    EC.visibility_of_element_located(BaNewCountryPropertyGeneralInformationPageLocators.MODAL_POPUP)):
                button_for_closing_modal_popup = self.browser.find_element(
                    *BaNewCountryPropertyGeneralInformationPageLocators.CLOSE_MODAL_POPUP)
                button_for_closing_modal_popup.click()
        except TimeoutException:
            print('Всплывающее окно с ГОСТом не успело прогрузиться')

    def select_bank_in_the_general_information_tab(self, bank):
        """ Выбор банка в поле 'Банк' """
        assert self.is_element_present(*BaNewCountryPropertyGeneralInformationPageLocators.BANK_DROP_DOWN_MENU), \
            "Поле 'Банк' отсутствует на странице"
        drop_down_menu_for_the_bank_field = self.browser.find_element(
            *BaNewCountryPropertyGeneralInformationPageLocators.BANK_DROP_DOWN_MENU)
        drop_down_menu_for_the_bank_field.click()
        dict_with_the_banks = \
            {
                'ВТБ': BaNewCountryPropertyGeneralInformationPageLocators.SELECT_BANK_VTB,
                "ПАО Банк 'ФК Открытие'": BaNewCountryPropertyGeneralInformationPageLocators.SELECT_BANK_OPENBANK
            }
        selected_bank = dict_with_the_banks[bank.value]
        self.browser.find_element(*selected_bank).click()
        assert self.browser.find_element(By.XPATH, f"//div[contains(text(), '{bank.value}')]").text == bank.value, \
            'Значение в поле Банк != выбранному банку'

    def select_department_in_the_general_information_tab(self, department):
        """ Выбор департамента в поле 'Департамент' """
        assert self.is_element_present(*BaNewCountryPropertyGeneralInformationPageLocators.DEPARTMENT_DROP_DOWN_MENU), \
            "Поле 'Департамент' отсутствует на странице"
        drop_down_menu_for_the_department_field = self.browser.find_element(
            *BaNewCountryPropertyGeneralInformationPageLocators.DEPARTMENT_DROP_DOWN_MENU)
        drop_down_menu_for_the_department_field.click()
        dict_with_departments = \
            {
                'Ипотека': BaNewCountryPropertyGeneralInformationPageLocators.SELECT_MORTGAGE_DEPARTMENT,
                'Кредитование малого бизнеса':
                    BaNewCountryPropertyGeneralInformationPageLocators.SELECT_SMALL_BUSINESS_LENDING_DEPARTMENT
            }
        select_department = dict_with_departments[department.value]
        self.browser.find_element(*select_department).click()
        assert self.browser.find_element(By.XPATH,
                                         f"//div[contains(text(), '{department.value}')]").text == department.value, \
            'Значение в поле Департамент != выбранному департаменту'

    def select_bank_employee_in_the_general_information_tab(self, bank_employee):
        """ Ввод сотрудника банка в поле 'Сотрудник банка' """
        assert self.is_element_present(
            *BaNewCountryPropertyGeneralInformationPageLocators.BANK_EMPLOYEE_DROP_DOWN_MENU), \
            "Поле 'Сотрудник банка' отсутствует на странице"
        field_for_input_bank_employee = self.browser.find_element(
            *BaNewCountryPropertyGeneralInformationPageLocators.INPUT_BANK_EMPLOYEE)
        for char in bank_employee:
            field_for_input_bank_employee.send_keys(char)
        # is_element_presence в течение таймаута чекает подтянувшееся значение из КРОНЫ для поля 'Сотрудник банка'
        assert self.is_element_presence(By.XPATH, f"//span[contains(text(), '{bank_employee}')]"), \
            " Введенный сотрудник банка не отображается в поле 'Сотрудник банка'. Возможно тормозит КРОНА "
        field_for_input_bank_employee.send_keys(Keys.RETURN)
        assert self.browser.find_element(
            By.XPATH, f"//div[contains(text(), '{bank_employee}')]").text == bank_employee, \
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

    def select_external_examination_in_the_general_information_tab(self):
        """ Выбор осмотра в поле 'Внешний осмотр' """
        assert self.is_element_present(
            *BaNewCountryPropertyGeneralInformationPageLocators.EXTERNAL_EXAMINATION_DROP_DOWN_MENU), \
            " Поле 'Внешний осмотр' не отображается на странице "
        drop_down_menu_for_external_examination = self.browser.find_element(
            *BaNewCountryPropertyGeneralInformationPageLocators.EXTERNAL_EXAMINATION_DROP_DOWN_MENU)
        drop_down_menu_for_external_examination.click()
        select_external = self.browser.find_element(
            *BaNewCountryPropertyGeneralInformationPageLocators.SELECT_EXTERNAL_EXAMINATION)
        select_external.click()
        assert self.browser.find_element(
            *BaNewCountryPropertyGeneralInformationPageLocators.CHECKING_THE_SELECTED_EXTERNAL_EXAMINATION).text == \
            "Проводился", "Значение в поле 'Внешний осмотр' не соответствует выбранному значению"

    def select_internal_inspection_in_the_general_information_tab(self):
        """ Выбор осмотра в поле 'Внутренний осмотр' """
        assert self.is_element_present(
            *BaNewCountryPropertyGeneralInformationPageLocators.INTERNAL_INSPECTION_DROP_DOWN_MENU), \
            " Поле 'Внутренний осмотр' не отображается на странице "
        drop_down_menu_for_internal_inspection = self.browser.find_element(
            *BaNewCountryPropertyGeneralInformationPageLocators.INTERNAL_INSPECTION_DROP_DOWN_MENU)
        drop_down_menu_for_internal_inspection.click()
        select_inspection = self.browser.find_element(
            *BaNewCountryPropertyGeneralInformationPageLocators.SELECT_INTERNAL_INSPECTION)
        select_inspection.click()
        assert self.browser.find_element(
            *BaNewCountryPropertyGeneralInformationPageLocators.CHECKING_THE_SELECTED_INTERNAL_INSPECTION).text == \
            "Проводился", "Значение в поле 'Внешний осмотр' не соответствует выбранному значению"

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
        assert self.is_element_presence(
            *BaNewCountryPropertyGeneralInformationPageLocators.UPLOAD_PROGRESS_HIDE, timeout=30), \
            f"Файл {file} не может прикрепиться. Прогресс бар не пропадает."
