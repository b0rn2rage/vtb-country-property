from selenium.webdriver.common.by import By


class KronaLoginPageLocators:
    INPUT_LOGIN = (By.CSS_SELECTOR, '#username')
    INPUT_PASSWORD = (By.CSS_SELECTOR, '#password.form-control')
    REMEMBER_ME = (By.CSS_SELECTOR, '#remember-me')
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[type='submit'].btn.btn-primary")
    RESET_PASSWORD_BUTTON = (By.CSS_SELECTOR, 'a.btn.btn-primary')


class KronaMainPageLocators:
    MENU_USERNAME = (By.XPATH, "//div[contains(@class, 'Menu_username_')]")
