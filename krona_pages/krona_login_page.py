from pages.base_page import BasePage
from .krona_locators import KronaLoginPageLocators
from .krona_locators import KronaMainPageLocators


class KronaLoginPage(BasePage):
    def login_to_krona(self, login, password):
        """Авторизация в КРОНУ"""
        assert self.is_element_visible(*KronaLoginPageLocators.INPUT_LOGIN), \
            "Поле для ввода имени пользователя отсутствует на странице"
        assert self.is_element_visible(*KronaLoginPageLocators.INPUT_PASSWORD), \
            "Поле для ввода пароля отсутсвует на странице"
        field_for_input_login = self.browser.find_element(*KronaLoginPageLocators.INPUT_LOGIN)
        field_for_input_login.send_keys(login)
        field_for_input_password = self.browser.find_element(*KronaLoginPageLocators.INPUT_PASSWORD)
        field_for_input_password.send_keys(password)
        assert self.is_element_present(*KronaLoginPageLocators.LOGIN_BUTTON), \
            "Кнопка 'Войти' отсутсвует на странице "
        login_button = self.browser.find_element(*KronaLoginPageLocators.LOGIN_BUTTON)
        login_button.click()
        assert self.is_element_presence(*KronaMainPageLocators.MENU_USERNAME, timeout=5), "Авторизация не удалась"

