from enum import Enum


class BaTypeNewReport(Enum):
    FLAT = 'Квартиры'
    COMMERCIAL = 'Коммерческая недвижимость'
    COUNTRY = 'Жилые дома'
    INTANGIBLE = 'Нематериальные активы'
    MOVABLE = 'Движимое имущество'
    INVENTORY = 'Товарно-материальные ценности'


class BaSelectBank(Enum):
    DOM_RF = 'АО БАНК ДОМ.РФ'
    TKB = 'Транскапитал банк'
    Uralsib = 'ПАО "БАНК УРАЛСИБ"'
    Sviaz = 'ПАО АКБ "Связь-Банк"'
    VTB = 'ВТБ'
    OpenBank = 'ПАО Банк "ФК Открытие"'


class BaSelectDepartment(Enum):
    MORTGAGE = 'Ипотека'
    SMALL_BUSINESS_LENDING = 'Кредитование малого бизнеса'


class BaSelectPropertyRights(Enum):
    OWNERSHIP = 'Право собственности'
    RIGHTS_ARE_NOT_ISSUED = 'Права не оформлены'
    RENT = 'Аренда'


class BaSelectObjectType(Enum):
    RESIDENTIAL = 'Жилой (садовый) дом'
    LAND = 'Земельный участок'
    OTHER = 'Иное'


class BaSelectReasonWhyNotEGRN(Enum):
    TECHNICAL_ISSUE = 'Техническая проблема на сайте Росреестра'
    OTHER = 'Другое'
