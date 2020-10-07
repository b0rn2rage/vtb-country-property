import pytest
from options.links import LinksBankAppraiser
from ba_pages.ba_login_page import BaLoginPage

"""
        Верификация аналитиком SRG через карточку отчета. Стандартный объект.
        Признак отсутствия документов присутствует.
        Статус отчета = Готово. Результат верификации = Принято.
"""


@pytest.mark.regression
@pytest.parametrize('select_test_stand', [LinksBankAppraiser.DefaultTest.login_link])
def test_srg_verivy_standard_obj_via_report_card(browser, select_test_stand):
    ba_login_page = BaLoginPage(browser)
    ba_login_page.open(select_test_stand)
