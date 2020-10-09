from enum import Enum


class KronaCountryPropertyReportStatus(Enum):
    ON_VERIFICATION = 'На верификации'
    THE_END_OF_THE_VERIFICATION = 'Окончание верификации SRG'
    READY = 'Готово'
    CHECK_UZI = 'Проверка УЗИ'
    READY_CHANGE_PRICE = 'Готово. Изменена стоимость'


class KronaCountryPropertyReportFlagForStandard(Enum):
    YES = 'Да'
    NO = 'Нет'


class KronaCountryPropertyReportCardNameTab(Enum):
    GENERAL_INFORMATION = 'Общая информация'
    FIRST_OBJECT = 'Объект 1'
    SECOND_OBJECT = 'Объект 2'
    DOCUMENTS = 'Документы'
    PHOTOS = 'Фотографии'
    VERIFICATION = 'Верификация'


class KronaCountryPropertyReportVerificationResult(Enum):
    ACCEPTED = 'Принято'
    NOT_ACCEPTED = 'Не принято'


class KronaCountryPropertyReportLackDocuments(Enum):
    CHECKED = "true"
    NOT_CHECKED = None


class KronaCountryPropertyReportDecision(Enum):
    APPROVE = 'Принять отчет'
    ADJUST = 'Скорректировать'
