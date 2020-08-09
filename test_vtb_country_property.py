from pages.ba_login_page import BaLoginPage
from pages.ba_main_page import BaMainPage
from pages.country_property_new_report_page import CountryPropertyNewReport

import time


def test_login_to_ba(browser):
    """Авторизация в БО"""
    link = 'https://testba.srg-it.ru/login.html'
    page = BaLoginPage(browser, link)
    page.open()
    page.close_fb_popup()
    page.login_to_bank_appraiser()


def test_creating_new_country_property_report(browser):
    """Создание нового отчета по ЖД"""
    link = browser.current_url
    page = BaMainPage(browser, link)
    page.close_gost_popup()
    page.close_simple_notification_modal()
    page.close_simple_notification_modal()  # Закрытие двух всплывающих окон
    page.create_new_report_from_main_page()


def test_filling_new_country_property_report(browser):
    """Заполнение отчета по ЖД"""
    link = browser.current_url
    page = CountryPropertyNewReport(browser, link)
    page.close_modal_popup()
    page.close_modal_popup()
    page.close_modal_popup()
    page.close_modal_popup()  # Закрытие четырех всплывающих окон
    page.select_bank_in_the_general_information_tab()
    page.select_department_in_the_general_information_tab()
    page.select_bank_employee_in_the_general_information_tab()
    page.input_full_name_of_the_borrower_customer_in_the_general_information_tab()
    page.input_report_number_in_the_general_information_tab()
    page.select_report_date_in_the_general_information_tab()
    page.select_valuation_date_in_the_general_information_tab()
    page.select_file_in_the_general_information_tab()
