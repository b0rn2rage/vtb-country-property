from pages.base_page import BasePage
from .ba_locators import BaReportPageLocators
from options.data import DataBankAppraiser
from selenium.webdriver.common.keys import Keys
from .ba_locators import BaNewCountryPropertyResidentialBuildingPageLocators
from .ba_locators import BaNewCountryPropertySharedFieldsLocators
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

    def input_the_address_for_documents(self, address):
        """ Заполнение поля 'Адрес по документам' """
        assert self.is_element_present(
            *BaNewCountryPropertyResidentialBuildingPageLocators.INPUT_THE_ADDRESS_FOR_DOCUMENTS), \
            "Поле 'Адрес по документам' не отображается на странице "
        field_for_input_the_address_for_documents = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.INPUT_THE_ADDRESS_FOR_DOCUMENTS)
        field_for_input_the_address_for_documents.send_keys(address)
        field_for_input_the_address_for_documents.send_keys(Keys.TAB)
        assert field_for_input_the_address_for_documents.text == address, \
            f"Значение в поле 'Адрес по документам' не соответствует {address}"

    def input_fias_address(self, fias_address):
        """Заполнение поля 'Адрес по ФИАС' """
        assert self.is_element_present(*BaNewCountryPropertyResidentialBuildingPageLocators.FIAS_DROP_DOWN_MENU), \
            " Поле 'Адрес по ФИАС' не отображается на странице "
        field_for_input_fias_address = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.INPUT_FIAS_ADDRESS)
        for char in fias_address:
            field_for_input_fias_address.send_keys(char)
        # is_element_presence в течение таймаута чекает подтянувшееся значение из КРОНЫ для поля
        assert self.is_element_presence(
            By.XPATH, f"//span[contains(text(), '{fias_address}')]"), \
            " Введенный адрес не отображается в поле 'Адрес по ФИАС'. Возможно тормозит КРОНА "
        field_for_input_fias_address.send_keys(Keys.RETURN)
        check_value_in_fias_address_field = self.browser.find_element(
            By.XPATH, f"//div[contains(text(), '{fias_address}')]")
        assert check_value_in_fias_address_field.text == \
            fias_address, \
            " Значение в поле 'Адрес по ФИАС' не соответствует введенному "

    def input_total_area_of_the_assessment_object(self, total_area):
        """ Заполнение поля с общей площадью ОО """
        assert self.is_element_present(
            *BaNewCountryPropertyResidentialBuildingPageLocators.TOTAL_AREA_OF_THE_ASSESSMENT_OBJECT), \
            " Поле 'Общая площадь объекта оценки' не отображается на странице "
        field_for_input_total_area_of_the_assessment_object = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.TOTAL_AREA_OF_THE_ASSESSMENT_OBJECT)
        field_for_input_total_area_of_the_assessment_object.send_keys(total_area)
        assert field_for_input_total_area_of_the_assessment_object.get_attribute("value") == total_area, \
            f"Значение в поле 'Общая площадь объекта оценки' не соответствует {total_area}"

    def input_market_price_of_the_object(self, market_price):
        """ Заполнение поля 'Рычноная стоимость объекта оценки' """
        assert self.is_element_present(
            *BaNewCountryPropertyResidentialBuildingPageLocators.MARKET_PRICE_OF_THE_OBJECT), \
            " Поле 'Рыночная стоимость объекта оценки' не отображается на странице "
        field_for_input_market_price_of_the_object = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.MARKET_PRICE_OF_THE_OBJECT)
        field_for_input_market_price_of_the_object.send_keys(market_price)
        assert field_for_input_market_price_of_the_object.get_attribute('value') == market_price, \
            f"Значение в поле 'Рыночная стоимость объекта оценки' не соответствует {market_price}"

    def pay_report(self):
        assert self.is_element_present(*BaReportPageLocators.PAY_REPORT_BUTTON_BEFORE_CLICK), \
            " Кнопка оплаты отчета отсутствует на странице "
        pay_report = self.browser.find_element(*BaReportPageLocators.PAY_REPORT_BUTTON_BEFORE_CLICK)
        pay_report.click()
        assert self.is_element_presence(
            *BaReportPageLocators.PAY_REPORT_BUTTON_AFTER_CLICK), "Селектор с кнопкой 'Оплачено' не обновился"
        assert self.text_in_element_is_correct(*BaReportPageLocators.PAY_REPORT_BUTTON_AFTER_CLICK, 'Оплачено'), \
            "Возникла проблема с оплатой отчета"

    def select_object_type(self, object_type):
        """ Выбор типа объекта Жилой (садовый) дом/Земельный участок/Иное """
        assert self.is_element_present(*BaNewCountryPropertySharedFieldsLocators.TYPE_DROP_DOWN_MENU), \
            " Поле 'Тип' не отображается на странице "
        self.browser.find_element(*BaNewCountryPropertySharedFieldsLocators.TYPE_DROP_DOWN_MENU).click()
        dict_with_object_types = \
        {
            'Жилой (садовый) дом': BaNewCountryPropertySharedFieldsLocators.SELECT_RESIDENTIAL_TYPE,
            'Земельный участок': BaNewCountryPropertySharedFieldsLocators.SELECT_LAND_TYPE,
            'Иное': BaNewCountryPropertySharedFieldsLocators.SELECT_OTHER_TYPE
        }
        selected_type = dict_with_object_types[object_type.value]
        self.browser.find_element(*selected_type).click()
        assert self.browser.find_element(By.XPATH, f"//div[contains(text(), '{object_type.value}')]").text == \
            object_type.value, f"Выбранный тип недвижимости != {object_type.value}"

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
        assert self.is_element_visible(*BaReportPageLocators.ENTER_THE_PASSWORD_FOR_SIGNING), \
            " Поле для ввода пароля при подписании отчета не появилось на странице "
        field_for_enter_the_password_for_singing = self.browser.find_element(
            *BaReportPageLocators.ENTER_THE_PASSWORD_FOR_SIGNING)
        field_for_enter_the_password_for_singing.send_keys(DataBankAppraiser.SharedData.password_for_singing_reports)
        assert self.is_element_present(*BaReportPageLocators.SIGN_BUTTON), " Кнопка 'Подписать' отсутствует на странице"
        sign_button = self.browser.find_element(*BaReportPageLocators.SIGN_BUTTON)
        sign_button.click()
        assert self.text_in_element_is_correct(*BaReportPageLocators.SUCCESSFUL_SIGN,
                                               'Отчет готов к печати!'), "При подписании отчета возникла ошибка"

    def select_property_rights_to_the_object_assessments(self, right):
        """ Выбор права в поле 'Имущественные права на объект оценки' """
        assert self.is_element_present(
            *BaNewCountryPropertyResidentialBuildingPageLocators.PROPERTY_RIGHTS_TO_THE_OBJECT_ASSESSMENT), \
            " Поле 'Имущественные права на объект оценки' отсутствует на странице "
        drop_down_menu_for_the_property_rights_field = self.browser.find_element(
            *BaNewCountryPropertyResidentialBuildingPageLocators.PROPERTY_RIGHTS_TO_THE_OBJECT_ASSESSMENT)
        drop_down_menu_for_the_property_rights_field.click()
        dict_with_property_rights = \
            {
                'Право собственности': BaNewCountryPropertyResidentialBuildingPageLocators.SELECT_OWNERSHIP,
                'Права не оформлены': BaNewCountryPropertyResidentialBuildingPageLocators.SELECT_RIGHTS_ARE_NOT_ISSUED,
                'Аренда': BaNewCountryPropertyResidentialBuildingPageLocators.SELECT_RENT
            }
        select_a_right = dict_with_property_rights[right.value]
        self.browser.find_element(*select_a_right).click()
        assert self.browser.find_element(By.XPATH, f"//div[contains(text(), '{right.value}')]").text == right.value, \
            "Значение в поле 'Имущственые права на объект оценки' != выбранному праву"

    def select_reason_why_not_egrn(self, reason):
        """ Выбор причины актуальной выписки из ЕГРН = Другое """
        assert self.is_element_present(*BaNewCountryPropertySharedFieldsLocators.EGRN_DROP_DOWN_MENU), \
            " Поле 'Причина отсутствия актуальной выписки из ЕГРН отсутствует на странице' "
        drop_down_menu_for_egrn = self.browser.find_element(
            *BaNewCountryPropertySharedFieldsLocators.EGRN_DROP_DOWN_MENU)
        drop_down_menu_for_egrn.click()
        dict_with_reasons = \
            {
                'Техническая проблема на сайте Росреестра':
                    BaNewCountryPropertySharedFieldsLocators.SELECT_TECHNICAL_ISSUE_EGRN,
                'Другое': BaNewCountryPropertySharedFieldsLocators.SELECT_OTHER_ISSUE_EGRN
            }
        select_reason = dict_with_reasons[reason.value]
        self.browser.find_element(*select_reason).click()
        assert self.browser.find_element(
            By.XPATH, f"//label[contains(text(),'Причина отсутствия')]/..//div[contains(text(), "
                      f"'{reason.value}')]").text == "Другое", \
            f"Значение в поле 'Причина отсутствия актуальной выписки из ЕГРН отсутствует на странице' != {reason.value}"
