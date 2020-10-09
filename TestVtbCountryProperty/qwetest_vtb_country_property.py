import pytest
from ba_pages.ba_login_page import BaLoginPage
from ba_pages.ba_main_page import BaMainPage
from ba_pages.ba_country_property_general_info_page import BaCountryPropertyGeneralInfoPage
from ba_pages.ba_country_property_photos_and_docs_page import BaCountryPropertyPhotosAndDocsPage
from ba_pages.ba_country_property_residential_building_page import BaCountryPropertyResidentialBuildingPage
from ba_pages.ba_country_property_land_page import BaCountryPropertyLandPage
from ba_pages.ba_country_property_report_page import BaCountryPropertyReportPage
from krona_pages.krona_login_page import KronaLoginPage
from krona_pages.krona_country_property_reports_page import KronaCountryPropertyReportsPage
from krona_pages.krona_country_property_report_card_page import \
    KronaReportCardGeneralInformationPage
from ba_pages.ba_enums.ba_enums import BaTypeNewReport
from ba_pages.ba_enums.ba_enums import BaSelectBank
from ba_pages.ba_enums.ba_enums import BaSelectDepartment
from ba_pages.ba_enums.ba_enums import BaSelectPropertyRights
from ba_pages.ba_enums.ba_enums import BaSelectObjectType
from ba_pages.ba_enums.ba_enums import BaSelectReasonWhyNotEGRN
from ba_pages.ba_enums.ba_enums import BaSelectElectricity
from ba_pages.ba_enums.ba_enums import BaSelectWaterSupply
from ba_pages.ba_enums.ba_enums import BaSelectSewerage
from ba_pages.ba_enums.ba_enums import BaSelectGas
from krona_pages.krona_emuns.krona_enum_new_country_property import CountryPropertyReportStatus
from krona_pages.krona_emuns.krona_enum_new_country_property import CountryPropertyReportFlagForStandard
from krona_pages.krona_emuns.krona_enum_new_country_property import CountryPropertyReportCardNameTab
from krona_pages.krona_emuns.krona_enum_new_country_property import CountryPropertyReportVerificationResult
from krona_pages.krona_emuns.krona_enum_new_country_property import CountryPropertyReportLackDocuments
from krona_pages.krona_emuns.krona_enum_new_country_property import CountryPropertyReportDecision

report_number = ''


class TestSrgVerificationStandardObjectViaReportCard:
    """
        Верификация аналитиком SRG через карточку отчета. Стандартный объект.
        Признак отсутствия документов присутствует.
        Статус отчета = Готово. Результат верификации = Принято.
        """
    def test_login_to_ba(self, browser):
        """Авторизация в БО."""
        link = LinksBankAppraiser.DefaultTest.login_page_link  # Выбор тестового стенда
        page = BaLoginPage(browser, link)
        page.open()
        page.close_fb_popup()
        page.login_to_bank_appraiser(AuthBankAppraiser.VtbAuth.VtbLogin, AuthBankAppraiser.VtbAuth.VtbPassword)

    def test_creating_new_country_property_report(self, browser):
        """Создание нового отчета."""
        link = browser.current_url
        page = BaMainPage(browser, link)
        page.close_gost_popup()
        page.close_simple_notification_modal()  # Закрытие двух всплывающих окон
        page.create_new_report_from_main_page(BaTypeNewReport.COUNTRY)  # Создать новый отчет, enum = Тип отчёта

    def test_filling_general_information_tab(self, browser):
        """Заполнение отчета по ЖД. Заполнение раздела 'Общая информация'."""
        link = browser.current_url
        page = BaCountryPropertyGeneralInfoPage(browser, link)
        page.close_modal_popup()  # Закрытие четырех всплывающих окон
        page.select_bank(BaSelectBank.VTB)  # Выбрать банк, enum = Банк
        page.select_department(BaSelectDepartment.MORTGAGE)
        page.select_bank_employee(DataBankAppraiser.BaCountryReport.bank_employee)
        page.input_name_of_the_borrower_customer(
            DataBankAppraiser.BaCountryReport.Borrower_Customer_Name)
        page.input_report_number(DataBankAppraiser.BaCountryReport.Report_Number)
        global report_number
        report_number = page.get_report_number()  # Глобальной переменной присваиваю значение номера отчета
        page.select_report_date()
        page.select_valuation_date()
        page.select_external_inspection()
        page.select_internal_inspection()
        page.select_file()
        shared_method = BaCountryPropertyReportPage(browser, link)
        shared_method.go_to_photos_and_documents_tab()

    def test_filling_photo_and_documents(self, browser):
        """Заполнение отчета по ЖД. Заполнение раздела 'Фото и документы'."""
        link = browser.current_url
        page = BaCountryPropertyPhotosAndDocsPage(browser, link)
        page.attach_photos()
        page.attach_documents()
        shared_method = BaCountryPropertyReportPage(browser, link)
        shared_method.go_to_new_object_tab()

    def test_filling_residential_building(self, browser):
        """Заполнение отчета по ЖД. Заполнение объекта с типом = 'Жилой дом'."""
        link = browser.current_url
        page = BaCountryPropertyResidentialBuildingPage(browser, link)
        shared_method = BaCountryPropertyReportPage(browser, link)
        shared_method.select_object_type(BaSelectObjectType.RESIDENTIAL)
        page.input_name_of_the_object(DataBankAppraiser.BaCountryReport.Name_of_the_object)
        shared_method.input_the_address_for_documents(
            DataBankAppraiser.BaCountryReport.Moscow_address_for_country_property)
        shared_method.input_fias_address(DataBankAppraiser.BaCountryReport.Moscow_address_for_country_property)
        shared_method.input_total_area(DataBankAppraiser.BaCountryReport.Total_area)
        shared_method.select_property_rights(BaSelectPropertyRights.OWNERSHIP)
        page.select_wall_material()
        page.select_repairs()
        shared_method.input_market_price(DataBankAppraiser.BaCountryReport.Moscow_low_price_house)
        shared_method.select_reason_why_not_egrn(BaSelectReasonWhyNotEGRN.OTHER)
        shared_method.select_electricity(BaSelectElectricity.NO)
        shared_method.select_water_supply(BaSelectWaterSupply.NO)
        shared_method.select_sewerage(BaSelectSewerage.NO)
        shared_method.select_gas(BaSelectGas.NO)
        page.select_heat_supply()
        shared_method.select_borrower_customer_are_same_person()
        shared_method.go_to_new_object_tab()

    def test_filling_land(self, browser):
        """Заполнение отчета по ЖД. Заполнение объекта с типом = 'Земельный участок'."""
        link = browser.current_url
        page = BaCountryPropertyLandPage(browser, link)
        shared_method = BaCountryPropertyReportPage(browser, link)
        shared_method.select_object_type(BaSelectObjectType.LAND)
        shared_method.input_the_address_for_documents(
            DataBankAppraiser.BaCountryReport.Moscow_address_for_country_property)
        shared_method.input_fias_address(DataBankAppraiser.BaCountryReport.Moscow_address_for_country_property)
        page.input_cadastral_number()
        shared_method.input_total_area(DataBankAppraiser.BaCountryReport.Total_area)
        page.select_category()
        page.input_type_of_permitted_use()
        shared_method.select_property_rights(BaSelectPropertyRights.OWNERSHIP)
        shared_method.input_market_price(DataBankAppraiser.BaCountryReport.Moscow_low_price_land)
        shared_method.select_reason_why_not_egrn(BaSelectReasonWhyNotEGRN.OTHER)
        shared_method.select_electricity(BaSelectElectricity.NO)
        shared_method.select_water_supply(BaSelectWaterSupply.NO)
        shared_method.select_sewerage(BaSelectSewerage.NO)
        shared_method.select_gas(BaSelectGas.NO)
        shared_method.select_borrower_customer_are_same_person()

    def test_save_report(self, browser):
        """Сохранение отчета."""
        link = browser.current_url
        page = BaCountryPropertyReportPage(browser, link)
        page.save_report()

    def test_pay_report(self, browser):
        """Оплата отчета."""
        link = browser.current_url
        page = BaCountryPropertyReportPage(browser, link)
        page.pay_report()

    def test_sign_report(self, browser):
        """Подписание отчета."""
        link = browser.current_url
        page = BaCountryPropertyReportPage(browser, link)
        page.sign_report()

    def test_redirect_to_krona(self, browser):
        """Переход в КРОНУ."""
        link = LinksKrona.DefaultTest.login_link
        page = BaCountryPropertyReportPage(browser, link)
        page.redirect_to_krona_login_page()

    def test_login_to_krona(self, browser):
        """Логин в КРОНУ."""
        link = browser.current_url
        page = KronaLoginPage(browser, link)
        page.login_to_krona(AuthKrona.SrgAuth.SrgLogin, AuthKrona.SrgAuth.SrgPassword)

    def test_open_country_property_report_in_krona(self, browser):
        """Открытие карточки отчета в реестре 'Жилые дома'."""
        link = browser.current_url
        page = KronaCountryPropertyReportsPage(browser, link)
        page.open_country_report_in_data_table(report_number)  # Аргумент = глобальная переменная

    def test_srg_verification_via_report_card(self, browser):
        """Верификация сотрудником SRG через карточку отчета."""
        link = browser.current_url
        page = KronaReportCardGeneralInformationPage(browser, link)
        page.check_values_after_ba_on_general_information_tab(CountryPropertyReportStatus.THE_END_OF_THE_VERIFICATION,
                                                              CountryPropertyReportFlagForStandard.YES)
        page.go_to_the_tab_in_the_report_card(CountryPropertyReportCardNameTab.VERIFICATION)
        page.attach_an_expert_calculation()
        page.input_new_price_in_the_verification_table(DataKrona.KronaCountryReport.Moscow_verification_low_price_house,
                                                       DataKrona.KronaCountryReport.Moscow_verification_low_price_land)
        page.checking_lack_documents()
        page.click_the_verification_button()
        page.checking_values_after_verification(CountryPropertyReportStatus.READY,
                                                CountryPropertyReportVerificationResult.ACCEPTED,
                                                CountryPropertyReportLackDocuments.CHECKED)


@pytest.mark.regression
class TestSrgVerificationNonStandardObjectViaReportCard:
    """
    Верификация аналитиком SRG через карточку отчета. Не стандартный объект.
    Признак отсутствия документов отсутствует. Статус отчета = Готово. Результат верификации = Принято.
    """
    def test_login_to_ba(self, browser):
        """Авторизация в БО."""
        link = LinksBankAppraiser.DefaultTest.login_page_link  # Выбор тестового стенда
        page = BaLoginPage(browser, link)
        page.open()
        page.close_fb_popup()
        page.login_to_bank_appraiser(AuthBankAppraiser.VtbAuth.VtbLogin, AuthBankAppraiser.VtbAuth.VtbPassword)

    def test_creating_new_country_property_report(self, browser):
        """Создание нового отчета."""
        link = browser.current_url
        page = BaMainPage(browser, link)
        page.close_gost_popup()
        page.close_simple_notification_modal()  # Закрытие двух всплывающих окон
        page.create_new_report_from_main_page(BaTypeNewReport.COUNTRY)  # Создать новый отчет, enum = Тип отчёта

    def test_filling_general_information_tab(self, browser):
        """Заполнение отчета по ЖД. Заполнение раздела 'Общая информация'."""
        link = browser.current_url
        page = BaCountryPropertyGeneralInfoPage(browser, link)
        page.close_modal_popup()  # Закрытие четырех всплывающих окон
        page.select_bank(BaSelectBank.VTB)  # Выбрать банк, enum = Банк
        page.select_department(BaSelectDepartment.MORTGAGE)
        page.select_bank_employee(DataBankAppraiser.BaCountryReport.bank_employee)
        page.input_name_of_the_borrower_customer(
            DataBankAppraiser.BaCountryReport.Borrower_Customer_Name)
        page.input_report_number(DataBankAppraiser.BaCountryReport.Report_Number)
        global report_number
        report_number = page.get_report_number()  # Глобальной переменной присваиваю значение номера отчета
        page.select_report_date()
        page.select_valuation_date()
        page.select_external_inspection()
        page.select_internal_inspection()
        page.select_file()
        shared_method = BaCountryPropertyReportPage(browser, link)
        shared_method.go_to_photos_and_documents_tab()

    def test_filling_photo_and_documents(self, browser):
        """Заполнение отчета по ЖД. Заполнение раздела 'Фото и документы'."""
        link = browser.current_url
        page = BaCountryPropertyPhotosAndDocsPage(browser, link)
        page.attach_photos()
        page.attach_documents()
        shared_method = BaCountryPropertyReportPage(browser, link)
        shared_method.go_to_new_object_tab()

    def test_filling_residential_building(self, browser):
        """Заполнение отчета по ЖД. Заполнение объекта с типом = 'Жилой дом'."""
        link = browser.current_url
        page = BaCountryPropertyResidentialBuildingPage(browser, link)
        shared_method = BaCountryPropertyReportPage(browser, link)
        shared_method.select_object_type(BaSelectObjectType.RESIDENTIAL)
        page.input_name_of_the_object(DataBankAppraiser.BaCountryReport.Name_of_the_object)
        shared_method.input_the_address_for_documents(
            DataBankAppraiser.BaCountryReport.Moscow_address_for_country_property)
        shared_method.input_fias_address(DataBankAppraiser.BaCountryReport.Moscow_address_for_country_property)
        shared_method.input_total_area(DataBankAppraiser.BaCountryReport.Total_area)
        shared_method.select_property_rights(BaSelectPropertyRights.OWNERSHIP)
        page.select_wall_material()
        page.select_repairs()
        shared_method.input_market_price(DataBankAppraiser.BaCountryReport.Moscow_low_price_house)
        shared_method.select_reason_why_not_egrn(BaSelectReasonWhyNotEGRN.OTHER)
        shared_method.select_electricity(BaSelectElectricity.NO)
        shared_method.select_water_supply(BaSelectWaterSupply.NO)
        shared_method.select_sewerage(BaSelectSewerage.NO)
        shared_method.select_gas(BaSelectGas.NO)
        page.select_heat_supply()
        shared_method.select_borrower_customer_are_same_person()

    def test_save_report(self, browser):
        """Сохранение отчета."""
        link = browser.current_url
        page = BaCountryPropertyReportPage(browser, link)
        page.save_report()

    def test_pay_report(self, browser):
        """Оплата отчета."""
        link = browser.current_url
        page = BaCountryPropertyReportPage(browser, link)
        page.pay_report()

    def test_sign_report(self, browser):
        """Подписание отчета."""
        link = browser.current_url
        page = BaCountryPropertyReportPage(browser, link)
        page.sign_report()

    def test_redirect_to_krona(self, browser):
        """Переход в КРОНУ."""
        link = LinksKrona.DefaultTest.login_link
        page = BaCountryPropertyReportPage(browser, link)
        page.redirect_to_krona_login_page()

    def test_login_to_krona(self, browser):
        """Логин в КРОНУ."""
        link = browser.current_url
        page = KronaLoginPage(browser, link)
        page.login_to_krona(AuthKrona.SrgAuth.SrgLogin, AuthKrona.SrgAuth.SrgPassword)

    def test_open_country_property_report_in_krona(self, browser):
        """Открытие карточки отчета в реестре 'Жилые дома'."""
        link = browser.current_url
        page = KronaCountryPropertyReportsPage(browser, link)
        page.open_country_report_in_data_table(report_number)  # Аргумент = глобальная переменная

    def test_srg_verification_via_report_card(self, browser):
        """Верификация сотрудником SRG через карточку отчета."""
        link = browser.current_url
        page = KronaReportCardGeneralInformationPage(browser, link)
        page.check_values_after_ba_on_general_information_tab(CountryPropertyReportStatus.THE_END_OF_THE_VERIFICATION,
                                                              CountryPropertyReportFlagForStandard.NO)
        page.go_to_the_tab_in_the_report_card(CountryPropertyReportCardNameTab.VERIFICATION)
        page.attach_an_expert_calculation()
        page.input_new_price_in_the_verification_table(DataKrona.KronaCountryReport.Moscow_verification_low_price_house)
        page.click_the_verification_button()
        page.checking_values_after_srg_verification(CountryPropertyReportStatus.READY,
                                                    CountryPropertyReportVerificationResult.ACCEPTED,
                                                    CountryPropertyReportLackDocuments.NOT_CHECKED)


@pytest.mark.run_current_test
@pytest.mark.regression
class TestVtbVerificationStandardObjectDecisionCorrect:
    """
   Верификация сотрудником ВТБ через карточку отчета. Стандартный объект.
   Решение сотрудника = Скорректировать.
   """
    def test_login_to_ba(self, browser):
        """Авторизация в БО."""
        link = LinksBankAppraiser.DefaultTest.login_page_link  # Выбор тестового стенда
        page = BaLoginPage(browser, link)
        page.open()
        page.close_fb_popup()
        page.login_to_bank_appraiser(AuthBankAppraiser.VtbAuth.VtbLogin, AuthBankAppraiser.VtbAuth.VtbPassword)

    def test_creating_new_country_property_report(self, browser):
        """Создание нового отчета."""
        link = browser.current_url
        page = BaMainPage(browser, link)
        page.close_gost_popup()
        page.close_simple_notification_modal()  # Закрытие двух всплывающих окон
        page.create_new_report_from_main_page(BaTypeNewReport.COUNTRY)  # Создать новый отчет, enum = Тип отчёта

    def test_filling_general_information_tab(self, browser):
        """Заполнение отчета по ЖД. Заполнение раздела 'Общая информация'."""
        link = browser.current_url
        page = BaCountryPropertyGeneralInfoPage(browser, link)
        page.close_modal_popup()  # Закрытие четырех всплывающих окон
        page.select_bank(BaSelectBank.VTB)  # Выбрать банк, enum = Банк
        page.select_department(BaSelectDepartment.MORTGAGE)
        page.select_bank_employee(DataBankAppraiser.BaCountryReport.bank_employee)
        page.input_name_of_the_borrower_customer(
            DataBankAppraiser.BaCountryReport.Borrower_Customer_Name)
        page.input_report_number(DataBankAppraiser.BaCountryReport.Report_Number)
        global report_number
        report_number = page.get_report_number()  # Глобальной переменной присваиваю значение номера отчета
        page.select_report_date()
        page.select_valuation_date()
        page.select_external_inspection()
        page.select_internal_inspection()
        page.select_file()
        shared_method = BaCountryPropertyReportPage(browser, link)
        shared_method.go_to_photos_and_documents_tab()

    def test_filling_photo_and_documents(self, browser):
        """Заполнение отчета по ЖД. Заполнение раздела 'Фото и документы'."""
        link = browser.current_url
        page = BaCountryPropertyPhotosAndDocsPage(browser, link)
        page.attach_photos()
        page.attach_documents()
        shared_method = BaCountryPropertyReportPage(browser, link)
        shared_method.go_to_new_object_tab()

    def test_filling_residential_building(self, browser):
        """Заполнение отчета по ЖД. Заполнение объекта с типом = 'Жилой дом'."""
        link = browser.current_url
        page = BaCountryPropertyResidentialBuildingPage(browser, link)
        shared_method = BaCountryPropertyReportPage(browser, link)
        shared_method.select_object_type(BaSelectObjectType.RESIDENTIAL)
        page.input_name_of_the_object(DataBankAppraiser.BaCountryReport.Name_of_the_object)
        shared_method.input_the_address_for_documents(
            DataBankAppraiser.BaCountryReport.Moscow_address_for_country_property)
        shared_method.input_fias_address(DataBankAppraiser.BaCountryReport.Moscow_address_for_country_property)
        shared_method.input_total_area(DataBankAppraiser.BaCountryReport.Total_area)
        shared_method.select_property_rights(BaSelectPropertyRights.OWNERSHIP)
        page.select_wall_material()
        page.select_repairs()
        shared_method.input_market_price(DataBankAppraiser.BaCountryReport.Moscow_high_price_house)
        shared_method.select_reason_why_not_egrn(BaSelectReasonWhyNotEGRN.OTHER)
        shared_method.select_electricity(BaSelectElectricity.NO)
        shared_method.select_water_supply(BaSelectWaterSupply.NO)
        shared_method.select_sewerage(BaSelectSewerage.NO)
        shared_method.select_gas(BaSelectGas.NO)
        page.select_heat_supply()
        shared_method.select_borrower_customer_are_same_person()
        shared_method.go_to_new_object_tab()

    def test_filling_land(self, browser):
        """Заполнение отчета по ЖД. Заполнение объекта с типом = 'Земельный участок'."""
        link = browser.current_url
        page = BaCountryPropertyLandPage(browser, link)
        shared_method = BaCountryPropertyReportPage(browser, link)
        shared_method.select_object_type(BaSelectObjectType.LAND)
        shared_method.input_the_address_for_documents(
            DataBankAppraiser.BaCountryReport.Moscow_address_for_country_property)
        shared_method.input_fias_address(DataBankAppraiser.BaCountryReport.Moscow_address_for_country_property)
        page.input_cadastral_number()
        shared_method.input_total_area(DataBankAppraiser.BaCountryReport.Total_area)
        page.select_category()
        page.input_type_of_permitted_use()
        shared_method.select_property_rights(BaSelectPropertyRights.OWNERSHIP)
        shared_method.input_market_price(DataBankAppraiser.BaCountryReport.Moscow_high_price_land)
        shared_method.select_reason_why_not_egrn(BaSelectReasonWhyNotEGRN.OTHER)
        shared_method.select_electricity(BaSelectElectricity.NO)
        shared_method.select_water_supply(BaSelectWaterSupply.NO)
        shared_method.select_sewerage(BaSelectSewerage.NO)
        shared_method.select_gas(BaSelectGas.NO)
        shared_method.select_borrower_customer_are_same_person()

    def test_save_report(self, browser):
        """Сохранение отчета."""
        link = browser.current_url
        page = BaCountryPropertyReportPage(browser, link)
        page.save_report()

    def test_pay_report(self, browser):
        """Оплата отчета."""
        link = browser.current_url
        page = BaCountryPropertyReportPage(browser, link)
        page.pay_report()

    def test_sign_report(self, browser):
        """Подписание отчета."""
        link = browser.current_url
        page = BaCountryPropertyReportPage(browser, link)
        page.sign_report()

    def test_redirect_to_krona(self, browser):
        """Переход в КРОНУ."""
        link = LinksKrona.DefaultTest.login_link
        page = BaCountryPropertyReportPage(browser, link)
        page.redirect_to_krona_login_page()

    def test_login_to_krona(self, browser):
        """Логин в КРОНУ."""
        link = browser.current_url
        page = KronaLoginPage(browser, link)
        page.login_to_krona(AuthKrona.VtbAuth.VtbLogin, AuthKrona.VtbAuth.VtbPassword)

    def test_open_country_property_report_in_krona(self, browser):
        """Открытие карточки отчета в реестре 'Жилые дома'."""
        link = browser.current_url
        page = KronaCountryPropertyReportsPage(browser, link)
        page.open_country_report_in_data_table(report_number)  # Аргумент = глобальная переменная

    def test_vtb_verification_via_report_card(self, browser):
        """Верификация сотрудником SRG через карточку отчета."""
        link = browser.current_url
        page = KronaReportCardGeneralInformationPage(browser, link)
        page.check_values_after_ba_on_general_information_tab(CountryPropertyReportStatus.CHECK_UZI,
                                                              CountryPropertyReportFlagForStandard.YES)
        page.go_to_the_tab_in_the_report_card(CountryPropertyReportCardNameTab.VERIFICATION)
        page.taking_decision(CountryPropertyReportDecision.ADJUST)
        page.input_new_adjust_price_in_the_decision_form(
            DataKrona.KronaCountryReport.Moscow_verification_high_price_house,
            DataKrona.KronaCountryReport.Moscow_verification_high_price_land)
        page.checking_values_after_vtb_verification(CountryPropertyReportStatus.READY_CHANGE_PRICE,
                                                    CountryPropertyReportVerificationResult.NOT_ACCEPTED)