import datetime
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    """Инициализация экземпляров класса"""

    def __init__(self, browser):
        self.browser = browser

    @staticmethod
    def current_date():
        """Получить текущую дату"""
        now = datetime.datetime.now()
        return now

    def is_element_present(self, how, what):
        """Проверка наличия элемента на странице"""
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_element_not_present(self, how, what):
        """Проверка отсутствия элемента на странице"""
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return True
        return False

    def is_element_clickable(self, how, what, timeout=10):
        """ Проверка того, что элемент является кликабельным """
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_presence(self, how, what, timeout=10):
        """ Проверка того, что элемент находится в DOM дереве """
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_visible(self, how, what, timeout=10):
        """Проверка того, что элемент находится в DOM дереве + отображается"""
        try:
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def text_in_element_is_correct(self, how, what, expected_text, timeout=5):
        """ Проверка того, что текст внутри элемента изменяется на правильный """
        try:
            WebDriverWait(self.browser, timeout).until(EC.text_to_be_present_in_element((how, what), expected_text))
        except TimeoutException:
            return False
        return True