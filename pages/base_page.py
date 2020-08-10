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

    def is_disappeared(self, how, what, timeout=1):
        try:
            WebDriverWait(self.browser, timeout, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def open(self):
        """Открытие страницы по ссылке"""
        self.browser.get(self.url)
