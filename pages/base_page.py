from selenium.common.exceptions import NoSuchElementException
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage():
    """Инициализация экземпляров класса"""

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    @staticmethod
    def current_date():
        """Получить текущую дату"""
        now = str(datetime.datetime.now())
        return now

    def is_element_present(self, how, what):
        """Проверка наличия элемента на странице"""
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_file_attached(self, how, what, timeout=10):
        """Проверка прикрепления файла"""
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_clickable(self, how, what, timeout=10):
        """Проверка того, что элемент является кликабельным"""
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            return False
        return True

    def open(self):
        """Открытие страницы по ссылке"""
        self.browser.get(self.url)
