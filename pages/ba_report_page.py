from .base_page import BasePage
from .locators import BaReportPageLocators


class BaReportPage(BasePage):
    """
    Описание методов, доступных на любой странице отчета, например кнопка "Сохранить", "Оплатить", "Подписать"
    """
    def save_report(self):
        assert self.is_element_present(*BaReportPageLocators.SAVE_REPORT_BUTTON), \
            " Кнопка сохранения отчета отсутствует на странцие "
        save_report = self.browser.find_element(*BaReportPageLocators.SAVE_REPORT_BUTTON)
        save_report.click()

