from .base_page import BasePage
from .locators import BaReportPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


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
        assert self.is_element_present(*BaReportPageLocators.PAY_REPORT_BUTTON), \
            " Кнопка оплаты отчета отсутствует на странцие "
        pay_report = self.browser.find_element(*BaReportPageLocators.PAY_REPORT_BUTTON)
        pay_report.click()
        assert WebDriverWait(self.browser, timeout=5).until(
            EC.text_to_be_present_in_element(*BaReportPageLocators.PAY_REPORT_BUTTON),
            "Оплачен"), 'Возникла ошибка при оплате отчета'

    def save_report(self):
        """ Сохранение отчета """
        assert self.is_element_present(*BaReportPageLocators.SAVE_REPORT_BUTTON), \
            " Кнопка сохранения отчета отсутствует на странице "
        save_report = self.browser.find_element(*BaReportPageLocators.SAVE_REPORT_BUTTON)
        print(save_report.text)
        save_report.click()
        assert WebDriverWait(self.browser, timeout=5).until(
            EC.text_to_be_present_in_element((BaReportPageLocators.SAVE_REPORT_BUTTON), "Сохранено")) == "Сохранено", \
            " Текст в кнопке 'Сохранить' не поменялся на 'Сохранено' "

    def sign_report(self):
        assert self.is_element_present(*BaReportPageLocators.SIGN_REPORT_BUTTON), \
            " Кнопка подписания отчета отсутствует на странице"
        assert self.is_element_visible(*BaReportPageLocators.THE_COMPLETION_OF_THE_REPORT_WINDOW), \
            " Окно 'Завершение отчета' не появилось на странице "
