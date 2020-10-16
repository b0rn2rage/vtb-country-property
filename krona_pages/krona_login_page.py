from pages.base_page import BasePage
from .krona_locators import KronaLoginPageLocators
from .krona_locators import KronaMainPageLocators


class KronaLoginPage(BasePage):
    def login_to_krona(self, login: str, password: str):
        """Авторизация в КРОНУ."""
        assert self.is_element_visible(*KronaLoginPageLocators.INPUT_LOGIN), \
            "Поле для ввода имени пользователя отсутствует на странице"
        input_login = self.browser.find_element(*KronaLoginPageLocators.INPUT_LOGIN)
        input_login.send_keys(login)
        input_password = self.browser.find_element(*KronaLoginPageLocators.INPUT_PASSWORD)
        input_password.send_keys(password)
        login_button = self.browser.find_element(*KronaLoginPageLocators.LOGIN_BUTTON)
        login_button.click()
        assert self.is_element_presence(*KronaMainPageLocators.USERNAME, timeout=5), "Авторизация не удалась"

