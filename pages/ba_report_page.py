from .base_page import BasePage
from .locators import BaReportPageLocators
import requests


class BaReportPage(BasePage):
    """
    Описание методов, доступных на любой странице отчета, например кнопка "Сохранить", "Оплатить", "Подписать"
    """
    def save_report(self):
        assert self.is_element_present(*BaReportPageLocators.SAVE_REPORT_BUTTON), \
            " Кнопка сохранения отчета отсутствует на странцие "
        save_report = self.browser.find_element(*BaReportPageLocators.SAVE_REPORT_BUTTON)
        save_report.click()
        response = requests.get("https://testba.srg-it.ru/jetty/save_country_property_report", timeout=10)
        assert response.status_code == 200, \
            ' При сохранении отчета возникла ошибка, status code != 200 или превышен таймаут '

    def pay_report(self):
        assert self.is_element_present()
