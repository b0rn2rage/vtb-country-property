from enum import Enum
from typing import Tuple

from ba_pages.ba_enums.ba_enums import BaTypeNewReport
from pages.base_page import BasePage
from .ba_locators import BaMainPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaMainPage(BasePage):
    """Страница 'Список отчетов' - Квартиры."""
    def close_gost_popup(self):
        """Закрытие всплывающего окна ГОСТ, жду 2 секунды, заодно подгружается страница в БО"""
        try:
            self.is_element_visible(*BaMainPageLocators.GOST_POPUP, timeout=4)
            button_for_closing_gost_popup = self.browser.find_element(*BaMainPageLocators.CLOSE_GOST_POPUP)
            button_for_closing_gost_popup.click()
        except TimeoutException:
            pass

    def close_simple_notification_modal(self):
        """Закрытие всплывающИХ окОН 'Уважаемые партнеры'."""
        try:
            while self.is_element_visible(*BaMainPageLocators.SIMPLE_NOTIFICATION_MODAL, timeout=5):
                button_for_closing_simple_notification_modal = self.browser.find_element(
                    *BaMainPageLocators.CLOSE_SIMPLE_NOTIFICATION_MODAL)
                button_for_closing_simple_notification_modal.click()
        except TimeoutException:
            pass

    def create_new_report_from_main_page(self, report_type: Enum):
        """Создание нового отчета с главной страницы БО."""
        button_for_show_create_report_dialog = self.browser.find_element(*BaMainPageLocators.SHOW_CREATE_REPORT_DIALOG)
        button_for_show_create_report_dialog.click()
        assert self.is_element_present(*BaMainPageLocators.CREATE_NEW_REPORT_COUNTRY_PROPERTY), \
            "Кнопка 'Жилые дома' не отображается на странице"
        dict_with_reports_type = {'Квартиры': BaMainPageLocators.CREATE_NEW_REPORT_FLAT,
                                  'Коммерческая недвижимость': BaMainPageLocators.CREATE_NEW_REPORT_COMMERCIAL_PROPERTY,
                                  'Жилые дома': BaMainPageLocators.CREATE_NEW_REPORT_COUNTRY_PROPERTY,
                                  'Нематериальные активы': BaMainPageLocators.CREATE_NEW_REPORT_INTANGIBLE_ASSET,
                                  'Движимое имущество': BaMainPageLocators.CREATE_NEW_REPORT_MOVABLE_PROPERTY,
                                  'Товарно-материальные ценности': BaMainPageLocators.CREATE_NEW_REPORT_NEW_INVENTORY
                                  }
        select_type = dict_with_reports_type[report_type.value]
        select_report_type = self.browser.find_element(*select_type)
        select_report_type.click()
