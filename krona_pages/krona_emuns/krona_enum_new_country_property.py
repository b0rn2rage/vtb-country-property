from enum import Enum


class CountryPropertyReportStatus(Enum):
    ON_VERIFICATION = 'На верификации'
    THE_END_OF_THE_VERIFICATION = 'Окончание верификации SRG'
    READY = 'Готово'
    CHECK_UZI = 'Проверка УЗИ'
    READY_CHANGE_PRICE = 'Готово. Изменена стоимость'


class CountryPropertyReportFlagForStandard(Enum):
    YES = 'Да'
    NO = 'Нет'


class CountryPropertyReportCardNameTab(Enum):
    GENERAL_INFORMATION = 'Общая информация'
    FIRST_OBJECT = 'Объект 1'
    SECOND_OBJECT = 'Объект 2'
    DOCUMENTS = 'Документы'
    PHOTOS = 'Фотографии'
    VERIFICATION = 'Верификация'


class CountryPropertyReportVerificationResult(Enum):
    ACCEPTED = 'Принято'
    NOT_ACCEPTED = 'Не принято'


class CountryPropertyReportLackDocuments(Enum):
    CHECKED = "true"
    NOT_CHECKED = None


class CountryPropertyReportDecision(Enum):
    APPROVE = 'Принять отчет'
    ADJUST = 'Скорректировать'
