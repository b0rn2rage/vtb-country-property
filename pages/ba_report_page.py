from .base_page import BasePage
from .locators import BaReportPageLocators
from options.data import DataBankAppraiser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time


class BaReportPage(BasePage):
    """
    Описание общих методов отчета, которые не имеют привязки к конкретной странице"
    """
    def go_to_photos_and_documents_tab(self):
        """ Переход в раздел 'Фотографии и документы' """
        self.browser.find_element(
            *BaReportPageLocators.GO_TO_PHOTOS_AND_DOCUMENTS_TAB).click()

    def go_to_new_object_tab(self):
        """ Переход в раздел с добавленным объектом """
        self.browser.find_element(
            *BaReportPageLocators.GO_TO_NEW_OBJECT_TAB).click()

    def pay_report(self):
        assert self.is_element_present(*BaReportPageLocators.PAY_REPORT_BUTTON_BEFORE_CLICK), \
            " Кнопка оплаты отчета отсутствует на странцие "
        pay_report = self.browser.find_element(*BaReportPageLocators.PAY_REPORT_BUTTON_BEFORE_CLICK)
        pay_report.click()
        assert self.is_element_presence(
            *BaReportPageLocators.PAY_REPORT_BUTTON_AFTER_CLICK), "Селектор с кнопкой 'Оплачено' не обновился"
        assert self.text_in_element_is_correct(*BaReportPageLocators.PAY_REPORT_BUTTON_AFTER_CLICK, 'Оплачено'), \
            "Возникла проблема с оплатой отчета"

    def save_report(self):
        """ Сохранение отчета """
        assert self.is_element_present(*BaReportPageLocators.SAVE_REPORT_BUTTON), \
            " Кнопка сохранения отчета отсутствует на странице "
        save_report = self.browser.find_element(*BaReportPageLocators.SAVE_REPORT_BUTTON)
        save_report.click()
        assert self.text_in_element_is_correct(*BaReportPageLocators.SAVE_REPORT_BUTTON, 'Cохранено'), \
            "Сохранить не поменялось на Сохранено. P.S. слово 'сохранено' написано в БО с ошибкой"

    def sign_report(self):
        assert self.is_element_present(*BaReportPageLocators.COMPLETE_AND_SIGN_BUTTON), \
            " Кнопка 'Завершить и подписать' отсутствует на странице"
        button_for_complete_and_sign = self.browser.find_element(*BaReportPageLocators.COMPLETE_AND_SIGN_BUTTON)
        button_for_complete_and_sign.click()
        assert self.is_element_visible(*BaReportPageLocators.THE_COMPLETION_OF_THE_REPORT_WINDOW), \
            " Окно 'Завершение отчета' не появилось на странице "
        assert self.is_element_present(*BaReportPageLocators.ENTER_THE_PASSWORD_FOR_SIGNING), \
            " Поле для ввода пароля при подписании отчета не появилось на странице "
        field_for_enter_the_password_for_singing = self.browser.find_element(
            *BaReportPageLocators.ENTER_THE_PASSWORD_FOR_SIGNING)
        field_for_enter_the_password_for_singing.send_keys(DataBankAppraiser.SharedData.password_for_singing_reports)
        assert self.is_element_present(*BaReportPageLocators.SIGN_BUTTON), " Кнопка 'Подписать' отсутствует на странице"
        sign_button = self.browser.find_element(*BaReportPageLocators.SIGN_BUTTON)
        sign_button.click()

