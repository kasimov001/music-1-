from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import logging

menuStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Uzbek music"),
            KeyboardButton(text="bass music")
        ],
        [
            KeyboardButton(text="Rus Music"),
            KeyboardButton(text="Turk Music")
        ],
        [
            KeyboardButton(text="Nasheedlar"),
            KeyboardButton(text="Trend")
        ]
    ],
    resize_keyboard=True
)
menuuzbek = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Yorqinxoja Umarov"),
            KeyboardButton(text="Munisa Rizaayev"),
            # KeyboardButton(text="ortga")
        ],
        [
            KeyboardButton(text="Ortga")
        ]
    ],
    resize_keyboard=True
)
menuummon = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Bir kunlik", callback_data="Yorqinxoja Umarov"),
        ],
        [
            InlineKeyboardButton(text="yomgir", callback_data="YORQINXOJA UMAROV")
        ],
        [
            InlineKeyboardButton(text="👈", callback_data="b1"),
            InlineKeyboardButton(text="❌", callback_data="❌"),
            InlineKeyboardButton(text="👉", callback_data="a1")
        ]
    ]
)
menushox = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Senga qolim yetmadimi",callback_data="Munisa Rizaayev")
        ],
        [
            InlineKeyboardButton(text="yomgir",callback_data="mirunisa rizayeva")
        ],
        [
            InlineKeyboardButton(text="👈", callback_data="a2"),
            InlineKeyboardButton(text="❌", callback_data="❌"),
            InlineKeyboardButton(text="👉", callback_data="a2")

        ]
    ]
)
menubass = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="avto bass"),
            KeyboardButton(text="quloqchin bass")
        ],
        [
            KeyboardButton(text="Ortga")
        ]
    ],
    resize_keyboard=True
)
menuavto = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Miyagi & Andy Panda - Minor", callback_data="avto bass"),
        ],
        [
            InlineKeyboardButton(text="jbl music", callback_data="AVTO BASS")
        ],
        [
            InlineKeyboardButton(text="👈", callback_data="xq"),
            InlineKeyboardButton(text="❌", callback_data="❌"),
            InlineKeyboardButton(text="👉", callback_data="a3")
        ]
    ]
)
menuquloqchin = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Я люблю тебя давно", callback_data="quloqchin bass")
        ],
        [
            InlineKeyboardButton(text="Детства", callback_data="QULOQ")
        ],
        [
            InlineKeyboardButton(text="👈", callback_data="xw"),
            InlineKeyboardButton(text="❌", callback_data="❌"),
            InlineKeyboardButton(text="👉", callback_data="a4")
        ]
    ]
)
menurus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Jony"),
            KeyboardButton(text="Miyagi")
        ],
        [
            KeyboardButton(text="Ortga")
        ]
    ],
    resize_keyboard=True
)
menujony = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="JONY - Комета", callback_data="Jony")
        ],
        [
            InlineKeyboardButton(text="Lolipop", callback_data="Jony ft Gafur")
        ],
        [
            InlineKeyboardButton(text="👈", callback_data="b5"),
            InlineKeyboardButton(text="❌", callback_data="❌i"),
            InlineKeyboardButton(text="👉", callback_data="a5")
        ]
    ]
)
menutimmati = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Патрон", callback_data="Miyagi")
        ],
        [
            InlineKeyboardButton(text="Моя дикая Касандра", callback_data="MIYAGI")
        ],
        [
            InlineKeyboardButton(text="👈", callback_data="m5"),
            InlineKeyboardButton(text="❌", callback_data="❌"),
            InlineKeyboardButton(text="👉", callback_data="a6")
        ]
    ]
)
menuturk = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Sami Yusuf"),
            KeyboardButton(text="Zeyneb")
        ],
        [
            KeyboardButton(text="Ortga")
        ]
    ],
    resize_keyboard=True
)
menusami = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Allohu Alloh", callback_data="Sami Yusuf")
        ],
        [
            InlineKeyboardButton(text="Hasbi Rabbi", callback_data="sami yusuf")
        ],
        [
            InlineKeyboardButton(text="👈", callback_data="b7"),
            InlineKeyboardButton(text="❌", callback_data="❌"),
            InlineKeyboardButton(text="👉", callback_data="a7")
        ]
    ]
)
menutolib = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Səbr Elə", callback_data="Zeyneb")
        ],
        [
            InlineKeyboardButton(text="Mod", callback_data="ZEYNEB")
        ],
        [
            InlineKeyboardButton(text="👈", callback_data="b8"),
            InlineKeyboardButton(text="❌", callback_data="❌"),
            InlineKeyboardButton(text="👉", callback_data="a8")
        ]
    ]
)
menuNasheed = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Nasheed"),
            KeyboardButton(text="Nasheed 1")
        ],
        [
            KeyboardButton(text="Ortga")
        ]
    ],
    resize_keyboard=True
)
menuarab = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Лабайк", callback_data="arabic")
        ],
        [
           InlineKeyboardButton(text="ROHMAN YA ROHMAN", callback_data="ARABIC")
        ],
        [
            InlineKeyboardButton(text="👈", callback_data="b9"),
            InlineKeyboardButton(text="❌", callback_data="❌"),
            InlineKeyboardButton(text="👉", callback_data="a9")
        ]
    ]
)
menuarab1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="kuntu_maytan", callback_data="uf")
        ],
        [
            InlineKeyboardButton(text="Rasulluloh keladur", callback_data="ok")
        ],
        [
            InlineKeyboardButton(text="👈", callback_data="b10"),
            InlineKeyboardButton(text="❌", callback_data="❌"),
            InlineKeyboardButton(text="👉", callback_data="a10")
        ]
    ]
)
menutrend = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="uzb"),
            KeyboardButton(text="rus")
        ],
        [
            KeyboardButton(text="Ortga")
        ]
    ],
    resize_keyboard=True
)
menuuzb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Yomgir", callback_data="uzb")
        ],
        [
            InlineKeyboardButton(text="SALOM FARISHTA", callback_data="UZ")
        ],
        [
            InlineKeyboardButton(text="👈", callback_data="x2"),
            InlineKeyboardButton(text="❌", callback_data="❌"),
            InlineKeyboardButton(text="👉", callback_data="y2")
        ]
    ]
)
menuru = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="zulayxo", callback_data="rus")
        ],
        [
            InlineKeyboardButton(text="Комета", callback_data="RU")
        ],
        [
            InlineKeyboardButton(text="👈", callback_data="y1"),
            InlineKeyboardButton(text="❌", callback_data="❌"),
            InlineKeyboardButton(text="👉", callback_data="o1")
        ]
    ]
)

# 2 chi kru ----------------------------------------------------------------

menuummon2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Jana Jana",callback_data="Yorqinxoja")
        ],
        [
            InlineKeyboardButton(text="Sogindim Yomon", callback_data="yorqinxoja")
        ],
        [
            InlineKeyboardButton(text="👈", callback_data="b1"),
            InlineKeyboardButton(text="❌", callback_data="❌"),
            InlineKeyboardButton(text="👉", callback_data="a1")
        ]
    ]
)
menushox2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ogiri",callback_data="munisa")
        ],
        [
            InlineKeyboardButton(text="Armon",callback_data="MUNISA")
        ],
        [
            InlineKeyboardButton(text="👈", callback_data="b2"),
            InlineKeyboardButton(text="❌", callback_data="❌"),
            InlineKeyboardButton(text="👉", callback_data="a2")
        ]
    ]
)
menuavto2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Патрон", callback_data="AVTO")
        ],
        [
            InlineKeyboardButton(text="Jbl music", callback_data="avto")
        ],
        [
            InlineKeyboardButton(text="👈", callback_data="b3"),
            InlineKeyboardButton(text="❌", callback_data="❌"),
            InlineKeyboardButton(text="👉", callback_data="a3")
        ]
    ]
)
menuquloqchin2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ты Расскажи Ка Мне",callback_data="quluq bass")
        ],
        [
            InlineKeyboardButton(text="Baby Driver", callback_data="QULOQ")
        ],
        [
            InlineKeyboardButton(text="👈", callback_data="k1"),
            InlineKeyboardButton(text="❌", callback_data="❌"),
            InlineKeyboardButton(text="👉", callback_data="a4")
        ]
    ]
)
menujony1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Лилии", callback_data="joy")
        ],
        [
            InlineKeyboardButton(text="Аллея", callback_data="on")
        ],
        [
            InlineKeyboardButton(text="👈", callback_data="b5"),
            InlineKeyboardButton(text="❌", callback_data="❌"),
            InlineKeyboardButton(text="👉", callback_data="a5")
        ]
    ]
)
menutimmati2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Minor",callback_data="tim")
        ],
        [
            InlineKeyboardButton(text="Miyagi   Эндшпиль",callback_data="TIM")
        ],
        [
            InlineKeyboardButton(text="👈", callback_data="h6"),
            InlineKeyboardButton(text="❌", callback_data="❌"),
            InlineKeyboardButton(text="👉", callback_data="a6")
        ]
    ]
)
menusami2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="You Came To Me", callback_data="SAMI")
        ],
        [
            InlineKeyboardButton(text="Allahu allah ifasın…enha Asiq…", callback_data="sami")
        ],
        [
            InlineKeyboardButton(text="👈", callback_data="b7"),
            InlineKeyboardButton(text="❌", callback_data="❌"),
            InlineKeyboardButton(text="👉", callback_data="a7")
        ]
    ]
)
menutolib1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Niye Söndü Eşk", callback_data="TOLIB")
        ],
        [
            InlineKeyboardButton(text="Zhernusi_kurdi_ژێرنووسی_کوردی", callback_data="tolib")
        ],
        [
            InlineKeyboardButton(text="👈", callback_data="b8"),
            InlineKeyboardButton(text="❌", callback_data="❌"),
            InlineKeyboardButton(text="👉", callback_data="a8")
        ]
    ]
)
menuprog = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="أحمد_بوخاطر_نشيد_طويل_الشوق",callback_data="nasheed")
        ],
        [
            InlineKeyboardButton(text="Nasheed", callback_data="1NASHEED")
        ],
        [
            InlineKeyboardButton(text="👈", callback_data="b9"),
            InlineKeyboardButton(text="❌", callback_data="❌"),
            InlineKeyboardButton(text="👉", callback_data="a9")
        ]
    ]
)
menuabu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ya Nabi Salam Alaika",callback_data="gv")
        ],
        [
            InlineKeyboardButton(text="Habibi Muhammad",callback_data="ll")
        ],
        [
            InlineKeyboardButton(text="👈", callback_data="b11"),
            InlineKeyboardButton(text="❌", callback_data="❌"),
            InlineKeyboardButton(text="👉", callback_data="a10")
        ]
    ]
)
menuru1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ya Nabi Salam Alaika", callback_data="russia1")
        ],
        [
            InlineKeyboardButton(text="Nasheed Habibi Muhammad", callback_data="russia2")
        ],
        [
            InlineKeyboardButton(text="👈", callback_data="m1"),
            InlineKeyboardButton(text="❌", callback_data="❌"),
            InlineKeyboardButton(text="👉", callback_data="ho")
        ]
    ]
)
menuozb1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Yure_Yiglama",callback_data="NON")
        ],
        [
            InlineKeyboardButton(text="Ey Tolka",callback_data="mon")
        ],
        [
            InlineKeyboardButton(text="👈", callback_data="uba"),
            InlineKeyboardButton(text="❌", callback_data="❌"),
            InlineKeyboardButton(text="👉", callback_data="abu")
        ]
    ]
)
