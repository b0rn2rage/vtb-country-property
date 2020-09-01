from .base_page import BasePage
from .locators import BaLoginPageLocators
from .locators import BaMainPageLocators
from options.auth import AuthBankAppraiser


class BaLoginPage(BasePage):

    def close_fb_popup(self):
        """Закрытие всплывающего окна FB"""
        assert self.is_element_visible(*BaLoginPageLocators.FACEBOOK_POPUP), \
            "Всплывающее окно с фэйсбуком отсутствует на странице"
        button_for_closing_fb_popup = self.browser.find_element(*BaLoginPageLocators.CLOSE_FACEBOOK_POPUP)
        button_for_closing_fb_popup.click()

    def login_to_bank_appraiser(self):
        """Авторизация в БО"""
        assert self.is_element_present(*BaLoginPageLocators.INPUT_EMAIL), \
            "Поле для ввода электронной почты отсутствует на странице"
        assert self.is_element_present(*BaLoginPageLocators.INPUT_PASSWORD), \
            "Поля для ввода пароля отсутствует на странице"
        field_for_input_email = self.browser.find_element(*BaLoginPageLocators.INPUT_EMAIL)
        field_for_input_email.send_keys(AuthBankAppraiser.VtbAuth.VtbLogin)
        field_for_input_password = self.browser.find_element(*BaLoginPageLocators.INPUT_PASSWORD)
        field_for_input_password.send_keys(AuthBankAppraiser.VtbAuth.VtbPassword)
        assert self.is_element_present(*BaLoginPageLocators.LOGIN_BUTTON), \
            "Кнопка 'Войти в систему' отсутствует на странице"
        login_button = self.browser.find_element(*BaLoginPageLocators.LOGIN_BUTTON)
        login_button.click()
        assert self.is_element_presence(*BaMainPageLocators.USER_NAME, timeout=2), "Авторизация не удалась"
