from options.links import LinksBankAppraiser
from ba_pages.ba_login_page import BaLoginPage

import time


def test_srg_verivy_standard_obj_via_report_card(browser, config):
    """
            Верификация аналитиком SRG через карточку отчета. Стандартный объект.
            Признак отсутствия документов присутствует.
            Статус отчета = Готово. Результат верификации = Принято.
    """
    ba_login_page = BaLoginPage(browser)
    ba_login_page.open(LinksBankAppraiser.DefaultTest.login_page_link)
    ba_login_page.close_fb_popup()
    ba_login_page.login_to_bank_appraiser(config['VtbLogin'], config['VtbPassword'])
    time.sleep(3)
