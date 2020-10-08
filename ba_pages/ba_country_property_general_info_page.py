import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from .ba_locators import BaCountryPropertyGeneralInfoPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


class BaCountryPropertyGeneralInfoPage(BasePage):
    """Заполнение раздела 'Общая информация' в новом отчете по ЖД."""

    def close_modal_popup(self):
        """Закрыть модальные окна на входе в новый отчет."""
        try:
            while self.is_element_visible(*BaCountryPropertyGeneralInfoPageLocators.MODAL_POPUP, timeout=3):
                close_popup = self.browser.find_element(*BaCountryPropertyGeneralInfoPageLocators.CLOSE_MODAL_POPUP)
                close_popup.click()
        except TimeoutException:
            pass

    def get_report_number(self):
        """Получить номер отчета."""
        input_report_number = self.browser.find_element(*BaCountryPropertyGeneralInfoPageLocators.INPUT_REPORT_NUMBER)
        return input_report_number.get_attribute('value')

    def input_name_of_the_borrower_customer(self, name):
        """Ввод ФИО заемщика/заказчика в поле 'ФИО Заемщика/Заказчика'."""
        input_name = self.browser.find_element(
            *BaCountryPropertyGeneralInfoPageLocators.INPUT_NAME_OF_THE_BORROWER_CUSTOMER)
        input_name.send_keys(name)
        assert input_name.get_attribute('value') == f'{name}', \
            f"Значение в поле 'ФИО Заемщика/Заказчика' не соответствует {name}."

    def input_report_number(self, report_number):
        """Ввод номера отчета в поле 'Номер отчета'."""
        input_number = self.browser.find_element(*BaCountryPropertyGeneralInfoPageLocators.INPUT_REPORT_NUMBER)
        full_report_name = report_number + str(self.current_date())
        input_number.send_keys(full_report_name)
        assert input_number.get_attribute('value') == full_report_name, \
            f"Значение в поле 'Номер отчета' не соответствует {full_report_name}"

    def select_bank(self, bank):
        """Выбор банка в поле 'Банк'."""
        drop_down_menu_for_the_bank_field = self.browser.find_element(
            *BaCountryPropertyGeneralInfoPageLocators.BANK_DROP_DOWN_MENU)
        drop_down_menu_for_the_bank_field.click()
        dict_with_the_banks = \
            {
                'ВТБ': BaCountryPropertyGeneralInfoPageLocators.SELECT_BANK_VTB,
                "ПАО Банк 'ФК Открытие'": BaCountryPropertyGeneralInfoPageLocators.SELECT_BANK_OPENBANK
            }
        selected_bank = dict_with_the_banks[bank.value]
        self.browser.find_element(*selected_bank).click()
        assert self.browser.find_element(By.XPATH, f"//div[contains(text(), '{bank.value}')]").text == bank.value, \
            'Значение в поле Банк != выбранному банку'

    def check_selected_value(self, field):
        """Проверка выбранного значения в указанном поле."""
        assert self.browser.find_element()

    def select_department(self, department):
        """Выбор департамента в поле 'Департамент'."""
        drop_down_menu_for_the_department_field = self.browser.find_element(
            *BaCountryPropertyGeneralInfoPageLocators.DEPARTMENT_DROP_DOWN_MENU)
        drop_down_menu_for_the_department_field.click()
        dict_with_departments = \
            {
                'Ипотека': BaCountryPropertyGeneralInfoPageLocators.SELECT_MORTGAGE_DEPARTMENT,
                'Кредитование малого бизнеса':
                    BaCountryPropertyGeneralInfoPageLocators.SELECT_SMALL_BUSINESS_LENDING_DEPARTMENT
            }
        select_department = dict_with_departments[department.value]
        self.browser.find_element(*select_department).click()
        assert self.browser.find_element(By.XPATH,
                                         f"//div[contains(text(), '{department.value}')]").text == department.value, \
            'Значение в поле Департамент != выбранному департаменту'

    def select_bank_employee(self, bank_employee):
        """Ввод сотрудника банка в поле 'Сотрудник банка'."""
        input_bank_employee = self.browser.find_element(*BaCountryPropertyGeneralInfoPageLocators.INPUT_BANK_EMPLOYEE)
        for char in bank_employee:
            input_bank_employee.send_keys(char)
        # is_element_presence в течение таймаута чекает подтянувшееся значение из КРОНЫ для поля 'Сотрудник банка'
        assert self.is_element_presence(By.XPATH, f"//span[contains(text(), '{bank_employee}')]"), \
            " Введенный сотрудник банка не отображается в поле 'Сотрудник банка'. Возможно тормозит КРОНА "
        input_bank_employee.send_keys(Keys.RETURN)
        assert self.browser.find_element(
            By.XPATH, f"//div[contains(text(), '{bank_employee}')]").text == bank_employee, \
            ' Значение в поле Сотрудник банка != autotest-country-property-vtb@test.ru '

    def select_report_date(self):
        """Выбор текущей даты для поля 'Дата отчета'."""
        open_calendar = self.browser.find_element(*BaCountryPropertyGeneralInfoPageLocators.REPORT_DATE_FIELD)
        open_calendar.click()
        select_current_date = self.browser.find_element(
            *BaCountryPropertyGeneralInfoPageLocators.SELECT_CURRENT_REPORT_DATE)
        select_current_date.click()
        assert self.browser.find_element(
            *BaCountryPropertyGeneralInfoPageLocators.SELECT_VALUE_IN_REPORT_DATE_FIELD).get_attribute(
            'value') == self.current_date().strftime(
            "%d.%m.%Y"), " Значение в поле 'Дата отчета' не соответствует текущей дате "

    def select_valuation_date(self):
        """Выбор текущей даты для поля 'Дата оценки'."""
        open_calendar = self.browser.find_element(
            *BaCountryPropertyGeneralInfoPageLocators.VALUATION_DATE_FIELD)
        open_calendar.click()
        select_current_date = self.browser.find_element(
            *BaCountryPropertyGeneralInfoPageLocators.SELECT_CURRENT_VALUATION_DATE)
        select_current_date.click()
        assert self.browser.find_element(
            *BaCountryPropertyGeneralInfoPageLocators.SELECT_VALUE_IN_VALUATION_DATE_FIELD).get_attribute(
            'value') == self.current_date().strftime(
            "%d.%m.%Y"), " Значение в поле 'Дата оценки' не соответствует текущей дате "

    def select_external_inspection(self):
        """Выбор осмотра в поле 'Внешний осмотр'."""
        drop_down_menu_for_external_examination = self.browser.find_element(
            *BaCountryPropertyGeneralInfoPageLocators.EXTERNAL_EXAMINATION_DROP_DOWN_MENU)
        drop_down_menu_for_external_examination.click()
        select_external = self.browser.find_element(
            *BaCountryPropertyGeneralInfoPageLocators.SELECT_EXTERNAL_EXAMINATION)
        select_external.click()
        assert self.browser.find_element(
            *BaCountryPropertyGeneralInfoPageLocators.CHECKING_THE_SELECTED_EXTERNAL_EXAMINATION).text == \
            "Проводился", "Значение в поле 'Внешний осмотр' не соответствует выбранному значению"

    def select_internal_inspection(self):
        """Выбор осмотра в поле 'Внутренний осмотр'."""
        drop_down_menu_for_internal_inspection = self.browser.find_element(
            *BaCountryPropertyGeneralInfoPageLocators.INTERNAL_INSPECTION_DROP_DOWN_MENU)
        drop_down_menu_for_internal_inspection.click()
        select_inspection = self.browser.find_element(
            *BaCountryPropertyGeneralInfoPageLocators.SELECT_INTERNAL_INSPECTION)
        select_inspection.click()
        assert self.browser.find_element(
            *BaCountryPropertyGeneralInfoPageLocators.CHECKING_THE_SELECTED_INTERNAL_INSPECTION).text == \
            "Проводился", "Значение в поле 'Внешний осмотр' не соответствует выбранному значению"

    def select_signer_in_the_general_information_tab(self):
        """
        Выбор подписанта в поле 'Подписант от лица организации'.
        Если подписант в организации один (как в данном случае), то поле заполняется в БО автоматически.
        Включать этот метод в тестовый сценарий только в случае появления других подписантов и оценщиков.
        """
        assert self.is_element_present(*BaCountryPropertyGeneralInfoPageLocators.SIGNER_DROP_DOWN_MENU), \
            "Поле 'Подписант от лица организации отсутствует на странице' "
        drop_down_menu_for_the_signer_field = self.browser.find_element(
            *BaCountryPropertyGeneralInfoPageLocators.SIGNER_DROP_DOWN_MENU)
        drop_down_menu_for_the_signer_field.click()
        select_signer_from_organization = self.browser.find_element(
            *BaCountryPropertyGeneralInfoPageLocators.SELECT_SIGNER)
        select_signer_from_organization.click()

    def select_file(self):
        """
        Прикладывание файла с отчетом об оценке. Проверка всех трех типов файлов (doc, docx, pdf)
        Проверка на загрузку/удаление прикрепленных файлов.
        """
        scroll_to_select_file = self.browser.find_element(*BaCountryPropertyGeneralInfoPageLocators.FOOTER)
        actions = ActionChains(self.browser)
        actions.move_to_element(scroll_to_select_file).perform()
        input_file_report = self.browser.find_element(
            *BaCountryPropertyGeneralInfoPageLocators.INPUT_FILE)
        file = "\\samples\\test pdf.pdf"
        input_file_report.send_keys(os.getcwd() + file)
        assert self.is_element_presence(
            *BaCountryPropertyGeneralInfoPageLocators.UPLOAD_PROGRESS_HIDE, timeout=30), \
            f"Файл {file} не может прикрепиться. Прогресс бар не пропадает."
