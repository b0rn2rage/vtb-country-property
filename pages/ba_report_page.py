from .base_page import BasePage
from .locators import BaReportPageLocators
import requests


class BaReportPage(BasePage):
    """
    Описание методов, доступных на любой странице отчета, например кнопка "Сохранить", "Оплатить", "Подписать"
    """
    def save_report(self):
        assert self.is_element_present(*BaReportPageLocators.SAVE_REPORT_BUTTON), \
            " Кнопка сохранения отчета отсутствует на странице "
        save_report = self.browser.find_element(*BaReportPageLocators.SAVE_REPORT_BUTTON)
        save_report.click()
        assert save_report.text == 'Сохранено', 'Возникла ошибка при сохранении отчета'

    def pay_report(self):
        assert self.is_element_present(*BaReportPageLocators.PAY_REPORT_BUTTON), \
            " Кнопка оплаты отчета отсутствует на странцие "
        save_report = self.browser.find_element(*BaReportPageLocators.PAY_REPORT_BUTTON)
        save_report.click()
        assert save_report.text == 'Оплачен', 'Возникла ошибка при оплате отчета'

    def sign_report(self):
        assert self.is_element_present(*BaReportPageLocators.SIGN_REPORT_BUTTON), \
            " Кнопка подписания отчета отсутствует на странице"
        assert self.is_element_visible(*BaReportPageLocators.THE_COMPLETION_OF_THE_REPORT_WINDOW), \
            " Окно 'Завершение отчета' не появилось на странице "
