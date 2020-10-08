from ba_pages.ba_report_page import BaReportPage
from ba_pages.ba_login_page import BaLoginPage
from ba_pages.ba_main_page import BaMainPage
from ba_pages.ba_country_property_general_info_page import BaCountryPropertyGeneralInfoPage
from ba_pages.ba_country_property_photos_and_docs_page import BaCountryPropertyPhotosAndDocsPage
from ba_pages.ba_country_property_residential_building_page import BaCountryPropertyResidentialBuildingPage
from ba_pages.ba_enums.ba_enum_new_country_property import BaTypeNewReport
from ba_pages.ba_enums.ba_enum_new_country_property import BaSelectBank
from ba_pages.ba_enums.ba_enum_new_country_property import BaSelectDepartment
from ba_pages.ba_enums.ba_enum_new_country_property import BaSelectObjectType
from ba_pages.ba_enums.ba_enum_new_country_property import BaSelectPropertyRights
from ba_pages.ba_enums.ba_enum_new_country_property import BaSelectWallMaterial
from ba_pages.ba_enums.ba_enum_new_country_property import BaSelectRepairs
import pytest
import time


@pytest.mark.regression
def test_srg_verify_standard_obj_via_report_card(browser, config, host):
    """
            Верификация аналитиком SRG через карточку отчета. Стандартный объект.
            Признак отсутствия документов присутствует.
            Статус отчета = Готово. Результат верификации = Принято.
    """
    ba_login_page = BaLoginPage(browser)
    ba_login_page.open(host['BankAppraiser']['test'])
    ba_login_page.close_fb_popup()
    ba_login_page.login_to_bank_appraiser(config['DataBankAppraiser']['Auth']['Login']['Vtb'],
                                          config['DataBankAppraiser']['Auth']['Password']['Vtb'])
    ba_main_page = BaMainPage(browser)
    ba_main_page.close_gost_popup()
    ba_main_page.close_simple_notification_modal()
    ba_main_page.create_new_report_from_main_page(BaTypeNewReport.COUNTRY)
    ba_country_property_general_info_page = BaCountryPropertyGeneralInfoPage(browser)
    ba_country_property_general_info_page.close_modal_popup()
    ba_country_property_general_info_page.select_bank(BaSelectBank.VTB)
    ba_country_property_general_info_page.select_department(BaSelectDepartment.MORTGAGE)
    ba_country_property_general_info_page.select_bank_employee(
        config['DataBankAppraiser']['BaCountryReport']['BankEmployee'])
    ba_country_property_general_info_page.input_name_of_the_borrower_customer(
        config['DataBankAppraiser']['BaCountryReport']['BorrowerCustomerName'])
    ba_country_property_general_info_page.input_report_number(
        config['DataBankAppraiser']['BaCountryReport']['ReportNumber'])
    report_number = ba_country_property_general_info_page.get_report_number()
    ba_country_property_general_info_page.select_report_date()
    ba_country_property_general_info_page.select_valuation_date()
    ba_country_property_general_info_page.select_external_inspection()
    ba_country_property_general_info_page.select_internal_inspection()
    ba_country_property_general_info_page.select_file()
    ba_report_page = BaReportPage(browser)
    ba_report_page.go_to_photos_and_documents_tab()
    ba_country_property_photos_and_docs_page = BaCountryPropertyPhotosAndDocsPage(browser)
    ba_country_property_photos_and_docs_page.attach_photos()
    ba_country_property_photos_and_docs_page.attach_documents()
    ba_report_page.go_to_new_object_tab()
    ba_country_property_residential_building_page = BaCountryPropertyResidentialBuildingPage(browser)
    ba_report_page.select_object_type(BaSelectObjectType.RESIDENTIAL)
    ba_country_property_residential_building_page.input_name_of_the_object(
        config['DataBankAppraiser']['BaCountryReport']['NameOfTheObject'])
    ba_report_page.input_the_address_for_documents(
        config['DataBankAppraiser']['BaCountryReport']['MoscowAddressForCountryProperty'])
    ba_report_page.input_fias_address(
        config['DataBankAppraiser']['BaCountryReport']['MoscowAddressForCountryProperty'])
    ba_report_page.input_total_area(config['DataBankAppraiser']['BaCountryReport']['TotalArea'])
    ba_report_page.select_property_rights(BaSelectPropertyRights.OWNERSHIP)
    ba_country_property_residential_building_page.select_wall_material(BaSelectWallMaterial.BRICK)
    ba_country_property_residential_building_page.select_repairs(BaSelectRepairs.GOOD)

