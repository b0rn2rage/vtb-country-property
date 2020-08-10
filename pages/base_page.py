from selenium.common.exceptions import NoSuchElementException
import datetime


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

    def open(self):
        """Открытие страницы по ссылке"""
        self.browser.get(self.url)
