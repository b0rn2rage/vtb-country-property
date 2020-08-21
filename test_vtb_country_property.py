import pytest
import time
from pages.ba_login_page import BaLoginPage
from pages.ba_main_page import BaMainPage
from pages.ba_new_country_property_general_information_page import BaCountryPropertyNewReportGeneralInformationPage
from pages.ba_new_country_property_photos_and_documents_page import BaNewCountryPropertyPhotosAndDocumentsPage
from pages.ba_new_country_property_residential_building_page import BaNewCountryPropertyResidentialBuildingPage


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
    page.close_simple_notification_modal()  # Закрытие двух всплывающих окон
    page.create_new_report_from_main_page()


def test_filling_general_information_tab(browser):
    """ Заполнение отчета по ЖД. Заполнение раздела 'Общая информация' """
    link = browser.current_url
    page = BaCountryPropertyNewReportGeneralInformationPage(browser, link)
    page.close_modal_popup()  # Закрытие четырех всплывающих окон
    page.select_bank_in_the_general_information_tab()
    page.select_department_in_the_general_information_tab()
    page.select_bank_employee_in_the_general_information_tab()
    page.input_full_name_of_the_borrower_customer_in_the_general_information_tab()
    page.input_report_number_in_the_general_information_tab()
    page.select_report_date_in_the_general_information_tab()
    page.select_valuation_date_in_the_general_information_tab()
    page.select_file_in_the_general_information_tab()
    page.go_to_photos_and_documents_tab_from_general_information_tab()


def test_filling_photo_and_documents(browser):
    """ Заполнение отчета по ЖД. Заполнение раздела 'Фото и документы' """
    link = browser.current_url
    page = BaNewCountryPropertyPhotosAndDocumentsPage(browser, link)
    page.attach_photos_in_photos_and_documents_tab()
    page.attach_documents_in_photos_and_documents_tab()
    page.go_to_first_object_tab_from_photos_and_documents_tab()


def test_filling_residential_filling(browser):
    """ Заполнение отчета по ЖД. Заполнение объекта с типом = 'Жилой дом' """
    link = browser.current_url
    page = BaNewCountryPropertyResidentialBuildingPage(browser, link)
    page.select_type_in_residential_building_tab()
    page.input_name_of_the_object()
    page.input_the_address_for_documents()


