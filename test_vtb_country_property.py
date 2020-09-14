import pytest
import time
from ba_pages.ba_login_page import BaLoginPage
from ba_pages.ba_main_page import BaMainPage
from ba_pages.ba_new_country_property_general_information_page import BaCountryPropertyNewReportGeneralInformationPage
from ba_pages.ba_new_country_property_photos_and_documents_page import BaNewCountryPropertyPhotosAndDocumentsPage
from ba_pages.ba_new_country_property_residential_building_page import BaNewCountryPropertyResidentialBuildingPage
from ba_pages.ba_new_country_property_land_page import BaNewCountryPropertyLandPage
from ba_pages.ba_report_page import BaReportPage
from options.links import LinksBankAppraiser
from options.auth import AuthBankAppraiser
from options.data import DataBankAppraiser
from ba_pages.ba_enums.ba_enum_type_new_report import BaTypeNewReport
from selenium.webdriver.common.by import By
from ba_pages.ba_locators import BaNewCountryPropertyGeneralInformationPageLocators
from ba_pages.ba_locators import BaNewCountryPropertyResidentialBuildingPageLocators
from ba_pages.ba_enums.ba_enum_type_new_report import BaSelectBank
from ba_pages.ba_enums.ba_enum_type_new_report import BaSelectDepartment


@pytest.mark.parametrize('login, password',
                         [(AuthBankAppraiser.VtbAuth.VtbLogin, AuthBankAppraiser.VtbAuth.VtbPassword)])
def test_login_to_ba(browser, login, password):
    """Авторизация в БО"""
    link = LinksBankAppraiser.DefaultTest.login_link
    page = BaLoginPage(browser, link)
    page.open()
    page.close_fb_popup()
    page.login_to_bank_appraiser(login, password)


def test_creating_new_country_property_report(browser):
    """Создание нового отчета """
    link = browser.current_url
    page = BaMainPage(browser, link)
    page.close_gost_popup()
    page.close_simple_notification_modal()  # Закрытие двух всплывающих окон
    page.create_new_report_from_main_page(BaTypeNewReport.COUNTRY)  # Создать новый отчет, enum = Тип отчёта


def test_filling_general_information_tab(browser):
    """ Заполнение отчета по ЖД. Заполнение раздела 'Общая информация' """
    link = browser.current_url
    page = BaCountryPropertyNewReportGeneralInformationPage(browser, link)
    page.close_modal_popup()  # Закрытие четырех всплывающих окон
    page.select_bank_in_the_general_information_tab(BaSelectBank.VTB)  # Выбрать банк ВТБ
    page.select_department_in_the_general_information_tab(BaSelectDepartment.MORTGAGE)
    page.select_bank_employee_in_the_general_information_tab()
    page2 = BaReportPage(browser, link)
    # Ввод ФИО заемщика/заказчика в поле 'ФИО Заемщика/Заказчика'
    page2.input_in_field(
        *BaNewCountryPropertyGeneralInformationPageLocators.INPUT_FULL_NAME_OF_THE_BORROWER_CUSTOMER,
        text_in_field=DataBankAppraiser.BaCountryReport.Borrower_Customer_Name)
    # Ввод номера отчета в поле 'Номер отчета'
    page2.input_in_field(*BaNewCountryPropertyGeneralInformationPageLocators.INPUT_REPORT_NUMBER,
                         text_in_field=DataBankAppraiser.BaCountryReport.Report_Name + str(page.current_date()))
    page.select_report_date_in_the_general_information_tab()
    page.select_valuation_date_in_the_general_information_tab()
    page.select_file_in_the_general_information_tab()
    page.select_external_examination_in_the_general_information_tab()
    page.select_internal_inspection_in_the_general_information_tab()
    page2 = BaReportPage(browser, link)
    page2.go_to_photos_and_documents_tab()


def test_filling_photo_and_documents(browser):
    """ Заполнение отчета по ЖД. Заполнение раздела 'Фото и документы' """
    link = browser.current_url
    page = BaNewCountryPropertyPhotosAndDocumentsPage(browser, link)
    page.attach_photos_in_photos_and_documents_tab()
    page.attach_documents_in_photos_and_documents_tab()
    page2 = BaReportPage(browser, link)
    page2.go_to_new_object_tab()


def test_filling_residential_building(browser):
    """ Заполнение отчета по ЖД. Заполнение объекта с типом = 'Жилой дом' """
    link = browser.current_url
    page = BaNewCountryPropertyResidentialBuildingPage(browser, link)
    page.select_type_in_residential_building_tab()
    page2 = BaReportPage(browser, link)
    # Ввод наименования объекта в поле 'Наименование объекта'
    page2.input_in_textarea(*BaNewCountryPropertyResidentialBuildingPageLocators.INPUT_NAME_OF_THE_OBJECT,
                            text_in_field=DataBankAppraiser.BaCountryReport.Name_of_the_object)
    # Ввод адреса в поле 'Адрес по документам'
    page2.input_in_textarea(*BaNewCountryPropertyResidentialBuildingPageLocators.INPUT_THE_ADDRESS_FOR_DOCUMENTS,
                            text_in_field=DataBankAppraiser.BaCountryReport.Moscow_address_for_country_property)
    page.input_fias_address()
    page.input_total_area_of_the_assessment_object()
    page.select_property_rights_to_the_object_assessments()
    page.select_wall_material()
    page.select_repairs()
    page.input_market_price_of_the_object()
    page.select_reason_why_not_egrn()
    page.select_electricity()
    page.select_water_supply()
    page.select_sewerage()
    page.select_gas()
    page.select_heat_supply()
    page.select_borrower_customer_are_same_person()
    page2 = BaReportPage(browser, link)
    page2.go_to_new_object_tab()


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
    page3 = BaReportPage(browser, link)
    page3.input_in_textarea(*BaNewCountryPropertyResidentialBuildingPageLocators.INPUT_THE_ADDRESS_FOR_DOCUMENTS,
                            text_in_field=DataBankAppraiser.BaCountryReport.Moscow_address_for_country_property)
    page2.input_fias_address()
    page.input_cadastral_number()
    page2.input_total_area_of_the_assessment_object()
    page.select_category()
    page.input_type_of_permitted_use()
    page2.select_property_rights_to_the_object_assessments()
    page.input_market_price_of_the_object()
    page2.select_reason_why_not_egrn()
    page2.select_electricity()
    page2.select_water_supply()
    page2.select_sewerage()
    page2.select_gas()
    page2.select_borrower_customer_are_same_person()


def test_save_report(browser):
    """ Сохранение отчета """
    link = browser.current_url
    page = BaReportPage(browser, link)
    page.save_report()


def test_pay_report(browser):
    """ Оплата отчета """
    link = browser.current_url
    page = BaReportPage(browser, link)
    page.pay_report()


def test_sign_report(browser):
    """ Подписание отчета """
    link = browser.current_url
    page = BaReportPage(browser, link)
    page.sign_report()