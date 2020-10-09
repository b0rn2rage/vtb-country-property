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


class BaSelectWallMaterial(Enum):
    BRICK = 'Кирпич'
    PANEL = 'Панель'
    MONOLITH = 'Монолит'
    BLOCK = 'Блок'
    WOOD = 'Дерево'
    BALK = 'Брус'
    STONE = 'Каменные'
    CARCASS = 'Каркасные'
    METAL_FRAME_PANELS = 'Металлокаркасные панели/Легкие конструкции'
    MONOLITH_BRICK = 'Монолит-кирпич'
    SIP_PANELS = 'СИП панели'


class BaSelectRepairs(Enum):
    WITHOUT = 'Без отделки'
    CLEAN = 'Под чистовую отделку'
    AVERAGE = 'Среднее (жилое) состояние'
    GOOD = 'Хорошее состояние'
    EXCELLENT = 'Отличное (евро) состояние'


class BaSelectReasonWhyNotEGRN(Enum):
    TECHNICAL_ISSUE = 'Техническая проблема на сайте Росреестра'
    OTHER = 'Другое'


class BaSelectElectricity(Enum):
    NO = 'Нет'
    CENTRAL = 'Есть, центральное'
    ON_THE_SITE = 'Есть на участке'
    AT_THE_BORDER = 'По границе участка'


class BaSelectWaterSupply(Enum):
    NO = 'Нет'
    AUTONOMOUS = 'Есть, автономное'
    CENTRAL = 'Есть, центральное'
    ON_THE_SITE = 'Есть на участке'
    AT_THE_BORDER = 'По границе участка'


class BaSelectSewerage(Enum):
    NO = 'Нет'
    AUTONOMOUS = 'Есть, автономное'
    CENTRAL = 'Есть, центральное'
    ON_THE_SITE = 'Есть на участке'
    AT_THE_BORDER = 'По границе участка'


class BaSelectGas(Enum):
    NO = 'Нет'
    CENTRAL = 'Есть, центральное'
    ON_THE_SITE = 'Есть на участке'
    AT_THE_BORDER = 'По границе участка'


class BaSelectHeatSupply(Enum):
    NO = 'Нет'
    AUTONOMOUS = 'Есть, автономное'
    CENTRAL = 'Есть, центральное'


class BaSelectCategory(Enum):
    SETTLEMENT = 'Земли населённых пунктов (земли поселений)'
    AGRICULTURAL = 'Земли сельскохозяйственного назначения'
    INDUSTRY = 'Земли промышленности и иного специального назначения'
    GUARDED = 'Земли особо охраняемых территорий и объектов'
    FOREST = 'Земли лесного фонда'
    WATER = 'Земли водного фонда'
    STOCK = 'Земли запаса'
