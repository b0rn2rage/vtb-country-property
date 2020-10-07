from pages.base_page import BasePage
from .ba_locators import BaLoginPageLocators
from .ba_locators import BaMainPageLocators
from options.links import LinksBankAppraiser


class BaLoginPage(BasePage):

    def __init__(self, browser, ):
        self.browser = browser
        self.link = link

    def close_fb_popup(self):
        """Закрытие всплывающего окна FB"""
        self.is_element_visible(*BaLoginPageLocators.FACEBOOK_POPUP)
        button_for_closing_fb_popup = self.browser.find_element(*BaLoginPageLocators.CLOSE_FACEBOOK_POPUP)
        button_for_closing_fb_popup.click()

    def login_to_bank_appraiser(self, login, password):
        """Авторизация в БО"""
        assert self.is_element_visible(*BaLoginPageLocators.INPUT_EMAIL), \
            "Поле для ввода электронной почты отсутствует на странице"
        field_for_input_email = self.browser.find_element(*BaLoginPageLocators.INPUT_EMAIL)
        field_for_input_email.send_keys(login)
        field_for_input_password = self.browser.find_element(*BaLoginPageLocators.INPUT_PASSWORD)
        field_for_input_password.send_keys(password)
        login_button = self.browser.find_element(*BaLoginPageLocators.LOGIN_BUTTON)
        login_button.click()
        assert self.is_element_presence(*BaMainPageLocators.USER_NAME, timeout=5), "Авторизация не удалась"

    def open(self, link):
        """Перейти по ссылке."""
        self.url = link
        self.browser.get.url
