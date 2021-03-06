# Импорт библиотек
import pytest
import time

# Импорт страниц из БО
from ba_pages.ba_country_property_report_page import BaCountryPropertyReportPage
from ba_pages.ba_login_page import BaLoginPage
from ba_pages.ba_main_page import BaMainPage
from ba_pages.ba_country_property_general_info_page import BaCountryPropertyGeneralInfoPage
from ba_pages.ba_country_property_photos_and_docs_page import BaCountryPropertyPhotosAndDocsPage
from ba_pages.ba_country_property_residential_building_page import BaCountryPropertyResidentialBuildingPage
from ba_pages.ba_country_property_land_page import BaCountryPropertyLandPage

# Импорт enum'ов из БО
from ba_pages.ba_enums.ba_enums import BaTypeNewReport
from ba_pages.ba_enums.ba_enums import BaSelectBank
from ba_pages.ba_enums.ba_enums import BaSelectDepartment
from ba_pages.ba_enums.ba_enums import BaSelectObjectType
from ba_pages.ba_enums.ba_enums import BaSelectPropertyRights
from ba_pages.ba_enums.ba_enums import BaSelectWallMaterial
from ba_pages.ba_enums.ba_enums import BaSelectRepairs
from ba_pages.ba_enums.ba_enums import BaSelectReasonWhyNotEGRN
from ba_pages.ba_enums.ba_enums import BaSelectElectricity
from ba_pages.ba_enums.ba_enums import BaSelectWaterSupply
from ba_pages.ba_enums.ba_enums import BaSelectSewerage
from ba_pages.ba_enums.ba_enums import BaSelectGas
from ba_pages.ba_enums.ba_enums import BaSelectHeatSupply
from ba_pages.ba_enums.ba_enums import BaSelectCategory

# Импорт страниц из КРОНЫ
from krona_pages.krona_login_page import KronaLoginPage
from krona_pages.krona_country_property_reports_page import KronaCountryPropertyReportsPage
from krona_pages.krona_country_property_report_card_page import KronaCountryPropertyReportCardPage

# Импорт enum'ов из КРОНЫ
from krona_pages.krona_emuns.krona_enum_new_country_property import KronaCountryPropertyReportStatus
from krona_pages.krona_emuns.krona_enum_new_country_property import KronaCountryPropertyReportFlagForStandard
from krona_pages.krona_emuns.krona_enum_new_country_property import KronaCountryPropertyReportCardNameTab
from krona_pages.krona_emuns.krona_enum_new_country_property import KronaCountryPropertyReportVerificationResult
from krona_pages.krona_emuns.krona_enum_new_country_property import KronaCountryPropertyReportLackDocuments


@pytest.mark.regression
@pytest.mark.run_current_test
def test_srg_verify_non_stand_ready(browser, config, host):
    """
            Верификация аналитиком SRG через карточку отчета. Не стандартный объект.
            Признак отсутствия документов = not checked.
            Статус отчета = Готово. Изменана стоимость. Результат верификации = Не принято.
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
    ba_country_property_report_page = BaCountryPropertyReportPage(browser)
    ba_country_property_report_page.go_to_photos_and_documents_tab()
    ba_country_property_photos_and_docs_page = BaCountryPropertyPhotosAndDocsPage(browser)
    ba_country_property_photos_and_docs_page.attach_photos()
    ba_country_property_photos_and_docs_page.attach_documents()
    ba_country_property_report_page.go_to_new_object_tab()
    ba_country_property_residential_building_page = BaCountryPropertyResidentialBuildingPage(browser)
    ba_country_property_report_page.select_object_type(BaSelectObjectType.RESIDENTIAL)
    ba_country_property_residential_building_page.input_name_of_the_object(
        config['DataBankAppraiser']['BaCountryReport']['NameOfTheObject'])
    ba_country_property_report_page.input_the_address_for_documents(
        config['DataBankAppraiser']['BaCountryReport']['MoscowAddressForCountryProperty'])
    ba_country_property_report_page.input_fias_address(
        config['DataBankAppraiser']['BaCountryReport']['MoscowAddressForCountryProperty'])
    ba_country_property_report_page.input_total_area(config['DataBankAppraiser']['BaCountryReport']['TotalArea'])
    ba_country_property_report_page.select_property_rights(BaSelectPropertyRights.OWNERSHIP)
    ba_country_property_residential_building_page.select_wall_material(BaSelectWallMaterial.BRICK)
    ba_country_property_residential_building_page.select_repairs(BaSelectRepairs.GOOD)
    ba_country_property_report_page.input_market_price(
        config['DataBankAppraiser']['BaCountryReport']['MoscowLowPriceHouse'])
    ba_country_property_report_page.select_reason_why_not_egrn(BaSelectReasonWhyNotEGRN.OTHER)
    ba_country_property_report_page.select_electricity(BaSelectElectricity.NO)
    ba_country_property_report_page.select_water_supply(BaSelectWaterSupply.NO)
    ba_country_property_report_page.select_sewerage(BaSelectSewerage.NO)
    ba_country_property_report_page.select_gas(BaSelectGas.NO)
    ba_country_property_residential_building_page.select_heat_supply(BaSelectHeatSupply.NO)
    ba_country_property_report_page.select_borrower_customer_are_same_person()
    ba_country_property_report_page.save_report()
    ba_country_property_report_page.pay_report()
    ba_country_property_report_page.sign_report(config['DataBankAppraiser']['Auth']['Password']['Vtb'])
    ba_country_property_report_page.open_new_window()
    krona_login_page = KronaLoginPage(browser)
    krona_login_page.open(host['Krona']['test'])
    krona_login_page.login_to_krona(config['DataKrona']['Auth']['Login']['Srg'],
                                    config['DataKrona']['Auth']['Password']['Srg'])
    krona_country_property_reports_page = KronaCountryPropertyReportsPage(browser)
    krona_country_property_reports_page.open_report_in_data_table(report_number)
    krona_country_property_report_card_page = KronaCountryPropertyReportCardPage(browser)
    krona_country_property_report_card_page.check_values_after_ba(
        KronaCountryPropertyReportStatus.THE_END_OF_THE_VERIFICATION, KronaCountryPropertyReportFlagForStandard.NO)
    krona_country_property_report_card_page.go_to_the_tab_in_the_report_card(
        KronaCountryPropertyReportCardNameTab.VERIFICATION)
    krona_country_property_report_card_page.attach_an_expert_calculation()
    # В качестве стоимости используется значение земельного участка, чтобы
    # верифицированная стоимость * 1.2 была меньше стоимости отчета в БО и
    # отчет получил статус = Готово. Изменена стоимость.
    krona_country_property_report_card_page.input_new_price_in_the_verification_table(
        config['DataKrona']['KronaCountryReport']['MoscowVerificationLowPriceLand'])
    krona_country_property_report_card_page.click_the_verification_button()
    krona_country_property_report_card_page.checking_values_after_srg_verification(
        KronaCountryPropertyReportStatus.READY_CHANGE_PRICE, KronaCountryPropertyReportVerificationResult.NOT_ACCEPTED,
        KronaCountryPropertyReportLackDocuments.NOT_CHECKED)

