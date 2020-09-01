import pytest
import time
from pages.ba_login_page import BaLoginPage
from pages.ba_main_page import BaMainPage
from pages.ba_new_country_property_general_information_page import BaCountryPropertyNewReportGeneralInformationPage
from pages.ba_new_country_property_photos_and_documents_page import BaNewCountryPropertyPhotosAndDocumentsPage
from pages.ba_new_country_property_residential_building_page import BaNewCountryPropertyResidentialBuildingPage
from pages.ba_new_country_property_land_page import BaNewCountryPropertyLandPage
from options.links import LinksBankAppraiser


def test_login_to_ba(browser):
    """Авторизация в БО"""
    link = LinksBankAppraiser.DefaultTestStand.login_link
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


def test_filling_residential_building(browser):
    """ Заполнение отчета по ЖД. Заполнение объекта с типом = 'Жилой дом' """
    link = browser.current_url
    page = BaNewCountryPropertyResidentialBuildingPage(browser, link)
    page.select_type_in_residential_building_tab()
    page.input_name_of_the_object()
    page.input_the_address_for_documents()
    page.input_fias_address()
    page.input_total_area_of_the_assessment_object()
    page.select_property_rights_to_the_object_assessments()
    page.select_wall_material()
    page.select_repairs()
    page.input_market_price_of_the_object()
    page.select_electricity()
    page.select_water_supply()
    page.select_sewerage()
    page.select_gas()
    page.select_heat_supply()
    page.select_borrower_customer_are_same_person()
    page.go_to_new_object_tab()


def test_filling_land(browser):
    """
    Заполнение отчета по ЖД. Заполнение объекта с типом = 'Земельный участок'
    Для новых методов, (у которых поля отличаются от объекта с типом = ЖД) используется экземпляр page
    Повторяющиеся методы вызываются из класса с типом ЖД, для них создан экземпляр page2.
    """
    link = browser.current_url
    page = BaNewCountryPropertyLandPage(browser, link)  # Экземпляр с классом ЗУ
    page.select_type_in_land_tab()
    page2 = BaNewCountryPropertyResidentialBuildingPage(browser, link)  # Экземпляр с классом ЖД
    page2.select_property_rights_to_the_object_assessments()
    page2.input_the_address_for_documents()
    page2.input_fias_address()
    page.input_cadastral_number()
    page2.input_total_area_of_the_assessment_object()
    page.select_category()
    page.input_type_of_permitted_use()
    page2.select_property_rights_to_the_object_assessments()
    page.input_market_price_of_the_object()
    page2.select_electricity()
    page2.select_water_supply()
    page2.select_sewerage()
    page2.select_gas()
    page2.select_borrower_customer_are_same_person()
    time.sleep(3)