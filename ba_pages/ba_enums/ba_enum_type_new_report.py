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
