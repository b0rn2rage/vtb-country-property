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
from ba_pages.ba_enums.ba_enum_new_country_property import BaTypeNewReport
from ba_pages.ba_locators import BaNewCountryPropertyResidentialBuildingPageLocators
from ba_pages.ba_enums.ba_enum_new_country_property import BaSelectBank
from ba_pages.ba_enums.ba_enum_new_country_property import BaSelectDepartment
from ba_pages.ba_enums.ba_enum_new_country_property import BaSelectPropertyRights
from ba_pages.ba_enums.ba_enum_new_country_property import BaSelectObjectType
from ba_pages.ba_enums.ba_enum_new_country_property import BaSelectReasonWhyNotEGRN


@pytest.mark.parametrize('login, password',
                         [(AuthBankAppraiser.VtbAuth.VtbLogin, AuthBankAppraiser.VtbAuth.VtbPassword)])
def test_login_to_ba(browser, login, password):
    """Авторизация в БО."""
    link = LinksBankAppraiser.DefaultTest.login_link  # Выбор тестового стенда
    page = BaLoginPage(browser, link)
    page.open()
    page.close_fb_popup()
    page.login_to_bank_appraiser(login, password)  # login, password - параметры запуска теста


def test_creating_new_country_property_report(browser):
    """Создание нового отчета."""
    link = browser.current_url
    page = BaMainPage(browser, link)
    page.close_gost_popup()
    page.close_simple_notification_modal()  # Закрытие двух всплывающих окон
    page.create_new_report_from_main_page(BaTypeNewReport.COUNTRY)  # Создать новый отчет, enum = Тип отчёта


def test_filling_general_information_tab(browser):
    """Заполнение отчета по ЖД. Заполнение раздела 'Общая информация'."""
    link = browser.current_url
    page = BaCountryPropertyNewReportGeneralInformationPage(browser, link)
    page.close_modal_popup()  # Закрытие четырех всплывающих окон
    page.select_bank_in_the_general_information_tab(BaSelectBank.VTB)  # Выбрать банк, enum = Банк
    page.select_department_in_the_general_information_tab(BaSelectDepartment.MORTGAGE)
    page.select_bank_employee_in_the_general_information_tab(DataBankAppraiser.BaCountryReport.bank_employee)
    page.input_full_name_of_the_borrower_customer_in_the_general_information_tab(
        DataBankAppraiser.BaCountryReport.Borrower_Customer_Name)
    page.input_report_number_in_the_general_information_tab(DataBankAppraiser.BaCountryReport.Report_Number)
    page.select_report_date_in_the_general_information_tab()
    page.select_valuation_date_in_the_general_information_tab()
    page.select_external_examination_in_the_general_information_tab()
    page.select_internal_inspection_in_the_general_information_tab()
    page.select_file_in_the_general_information_tab()
    shared_method = BaReportPage(browser, link)
    shared_method.go_to_photos_and_documents_tab()


def test_filling_photo_and_documents(browser):
    """Заполнение отчета по ЖД. Заполнение раздела 'Фото и документы'."""
    link = browser.current_url
    page = BaNewCountryPropertyPhotosAndDocumentsPage(browser, link)
    page.attach_photos_in_photos_and_documents_tab()
    page.attach_documents_in_photos_and_documents_tab()
    shared_method = BaReportPage(browser, link)
    shared_method.go_to_new_object_tab()


def test_filling_residential_building(browser):
    """Заполнение отчета по ЖД. Заполнение объекта с типом = 'Жилой дом'."""
    link = browser.current_url
    page = BaNewCountryPropertyResidentialBuildingPage(browser, link)
    shared_method = BaReportPage(browser, link)
    shared_method.select_object_type(BaSelectObjectType.RESIDENTIAL)
    page.input_name_of_the_object(DataBankAppraiser.BaCountryReport.Name_of_the_object)
    shared_method.input_the_address_for_documents(DataBankAppraiser.BaCountryReport.Moscow_address_for_country_property)
    shared_method = BaReportPage(browser, link)
    shared_method.input_fias_address(DataBankAppraiser.BaCountryReport.Moscow_address_for_country_property)
    shared_method.input_total_area_of_the_assessment_object(DataBankAppraiser.BaCountryReport.Total_area)
    shared_method.select_property_rights_to_the_object_assessments(BaSelectPropertyRights.OWNERSHIP)
    page.select_wall_material()
    page.select_repairs()
    shared_method.input_market_price_of_the_object(DataBankAppraiser.BaCountryReport.Moscow_low_price_house)
    shared_method.select_reason_why_not_egrn(BaSelectReasonWhyNotEGRN.OTHER)
    page.select_electricity()
    page.select_water_supply()
    page.select_sewerage()
    page.select_gas()
    page.select_heat_supply()
    page.select_borrower_customer_are_same_person()
    shared_method.go_to_new_object_tab()


def test_filling_land(browser):
    """Заполнение отчета по ЖД. Заполнение объекта с типом = 'Земельный участок'."""
    link = browser.current_url
    page = BaNewCountryPropertyLandPage(browser, link)  # Экземпляр с классом ЗУ
    shared_method = BaReportPage(browser, link)
    shared_method.select_object_type(BaSelectObjectType.LAND)
    page2 = BaNewCountryPropertyResidentialBuildingPage(browser, link)  # Экземпляр с классом ЖД
    shared_method.input_the_address_for_documents(DataBankAppraiser.BaCountryReport.Moscow_address_for_country_property)
    shared_method.input_fias_address(DataBankAppraiser.BaCountryReport.Moscow_address_for_country_property)
    page.input_cadastral_number()
    shared_method.input_total_area_of_the_assessment_object(DataBankAppraiser.BaCountryReport.Total_area)
    page.select_category()
    page.input_type_of_permitted_use()
    shared_method.select_property_rights_to_the_object_assessments(BaSelectPropertyRights.OWNERSHIP)
    shared_method.input_market_price_of_the_object(DataBankAppraiser.BaCountryReport.Moscow_low_price_house)
    shared_method.select_reason_why_not_egrn(BaSelectReasonWhyNotEGRN.OTHER)
    page2.select_electricity()
    page2.select_water_supply()
    page2.select_sewerage()
    page2.select_gas()
    page2.select_borrower_customer_are_same_person()


def test_save_report(browser):
    """Сохранение отчета."""
    link = browser.current_url
    page = BaReportPage(browser, link)
    page.save_report()


def test_pay_report(browser):
    """Оплата отчета."""
    link = browser.current_url
    page = BaReportPage(browser, link)
    page.pay_report()


def test_sign_report(browser):
    """Подписание отчета."""
    link = browser.current_url
    page = BaReportPage(browser, link)
    page.sign_report()