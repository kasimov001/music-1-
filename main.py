from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, \
    InlineKeyboardMarkup, CallbackQuery
from aiogram import executor
from config import dp, bot
from inline import *


@dp.message_handler(commands="start")
async def Start(msg: Message):
    img = open("image/Без названия.jpg", "rb")
    text = f"Assalomu Alekum {msg.from_user.full_name},\n Music bot ga Hush Kelibsiz"
    # text = "kerakli tugmani bosing"
    await bot.send_photo(msg.chat.id, img, caption=text, reply_markup=menuStart)


# @dp.message_handler(text="help")
# async def help(msg: Message, msg):
#     text = f"yorgam uchun https://t.me/Kasimov_oo1 ga yozning"
#     await msg.answer(f"salom")


@dp.message_handler(text="Uzbek music")
async def uzb(msg: Message):
    await msg.answer(f"kerakli bolimni tanglangi!", reply_markup=menuuzbek)


@dp.message_handler(text="bass music")
async def uzb(msg: Message):
    await msg.answer(f"kerakli bolimni tanglangi!", reply_markup=menubass)


@dp.message_handler(text="Rus Music")
async def uzb(msg: Message):
    await msg.answer(f"kerakli bolimni tanglangi!", reply_markup=menurus)


@dp.message_handler(text="Turk Music")
async def uzb(msg: Message):
    await msg.answer(f"kerakli bolimni tanglangi!", reply_markup=menuturk)


@dp.message_handler(text="Nasheedlar")
async def uzb(msg: Message):
    await msg.answer(f"kerakli bolimni tanglangi!", reply_markup=menuNasheed)


@dp.message_handler(text="Trend")
async def uzb(msg: Message):
    await msg.answer(f"kerakli bolimni tanglangi!", reply_markup=menutrend)


@dp.message_handler(text="Uzbek music")
async def uzb(msg: Message):
    await msg.answer(f"Yorqinxoja Umarov", reply_markup=menuuzbek)


@dp.message_handler(text="Yorqinxoja Umarov")
async def uzb(msg: Message):
    await msg.answer_photo(open("image/m1000x1000.png", "rb"), f"kerakli bolimni tanglangi!", reply_markup=menuummon)


@dp.message_handler(text="Uzbek music")
async def uzb(msg: Message):
    await msg.answer(f"Munisa Rizaayev", reply_markup=menuuzbek)


@dp.message_handler(text="Munisa Rizaayev")
async def uzb(msg: Message):
    await msg.answer_photo(open("image/Без названия (2).jpg", "rb"), f"kerakli bolimni tanglangi!",
                           reply_markup=menushox)


@dp.message_handler(text="bass music")
async def uzb(msg: Message):
    await msg.answer("avto bass", reply_markup=menubass)


@dp.message_handler(text="avto bass")
async def uzb(msg: Message):
    await msg.answer_photo(open("image/Без названия (3).jpg", "rb"), f"kerakli bolimni tanglangi!",
                           reply_markup=menuavto)


@dp.message_handler(text="bass music")
async def uzb(msg: Message):
    await msg.answer("quloqchin bass", reply_markup=menubass)


@dp.message_handler(text="quloqchin bass")
async def uzb(msg: Message):
    await msg.answer_photo(open("image/Без названия.jpg", "rb"), f"kerakli bolimni tanglangi!",
                           reply_markup=menuquloqchin)


@dp.message_handler(text="Rus Music")
async def uzb(msg: Message):
    await msg.answer("Jony", reply_markup=menurus)


@dp.message_handler(text="Jony")
async def uzb(msg: Message):
    await msg.answer_photo(open("image/images.jpg", "rb"), f"kerakli bolimni tanglangi!", reply_markup=menujony)


@dp.message_handler(text="Rus Music")
async def uzb(msg: Message):
    await msg.answer("Miyagi", reply_markup=menurus)


@dp.message_handler(text="Miyagi")
async def uzb(msg: Message):
    await msg.answer_photo(open("image/Без названия (4).jpg", "rb"), f"kerakli bolimni tanglangi!",
                           reply_markup=menutimmati)


@dp.message_handler(text="Turk Music")
async def uzb(msg: Message):
    await msg.answer("Sami Yusuf", reply_markup=menuturk)


@dp.message_handler(text="Sami Yusuf")
async def uzb(msg: Message):
    await msg.answer_photo(open("image/Без названия (5).jpg", "rb"), f"kerakli bolimni tanglangi!",
                           reply_markup=menusami)


@dp.message_handler(text="Turk Music")
async def uzb(msg: Message):
    await msg.answer("Zeyneb", reply_markup=menuturk)


@dp.message_handler(text="Zeyneb")
async def uzb(msg: Message):
    await msg.answer_photo(open("image/Без названия.jpg", "rb"), f"kerakli bolimni tanglangi!", reply_markup=menutolib)


@dp.message_handler(text="Nasheedlar")
async def uzb(msg: Message):
    await msg.answer("arabic", reply_markup=menuNasheed)


@dp.message_handler(text="Nasheed")
async def uzb(msg: Message):
    await msg.answer_photo(open("image/Без названия.jpg", "rb"), f"kerakli bolimni tanglangi!", reply_markup=menuarab)


@dp.message_handler(text="Nasheedlar")
async def uzb(msg: Message):
    await msg.answer("arabic 1", reply_markup=menuNasheed)


@dp.message_handler(text="Nasheed 1")
async def uzb(msg: Message):
    await msg.answer_photo(open("image/Без названия.jpg", "rb"), f"kerakli bolimni tanglangi!", reply_markup=menuarab1)


@dp.message_handler(text="Trend")
async def uzb(msg: Message):
    await msg.answer("uzb", reply_markup=menutrend)


@dp.message_handler(text="uzb")
async def uzb(msg: Message):
    await msg.answer_photo(open("image/Без названия.jpg", "rb"), f"kerakli bolimni tanglangi!", reply_markup=menuuzb)


@dp.message_handler(text="Trend")
async def uzb(msg: Message):
    await msg.answer("rus", reply_markup=menuNasheed)


@dp.message_handler(text="rus")
async def uzb(msg: Message):
    await msg.answer_photo(open("image/Без названия.jpg", "rb"), f"kerakli bolimni tanglangi!", reply_markup=menuru)


@dp.message_handler(text="Ortga")
async def uzb(msg: Message):
    await msg.answer(f"kerakli tugmani tanglan!", reply_markup=menuStart)


@dp.callback_query_handler(text="Yorqinxoja Umarov")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(open("music/Yorqinxoja Umarov _ Bir kunlik.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="YORQINXOJA UMAROV")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/yorqinxoja-umarov-yomgir.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="Munisa Rizaayev")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/4_5974192662834579783.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="mirunisa rizayeva")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/Munisa_Rizayeva_Yomg'ir_Www.Yangilar.uz.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="avto bass")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/Miyagi   Andy Panda - Minor [bass. by dendy]     Bass Music.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="AVTO BASS")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/Jbl music 🎶 bass boosted 💥🔥.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="quloqchin bass")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/Я люблю тебя давно.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="QULOQ")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/Rauf_Faik_-_Detstvo.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


# @dp.callback_query_handler(text_contains="QULOQ")
# async def sample(call: CallbackQuery):
#     await call.message.answer_audio(
#         open("music/Rauf_Faik_-_Detstvo.mp3", "rb"), f"Dostlarga Ulashamiza!")
#     await call.message.delete()


@dp.callback_query_handler(text="Jony")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/JONY - Комета(MP3_160K)_1.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="Jony ft Gafur")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/Lolipop .mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="Miyagi")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/Miyagi  и  Andy Panda - Патрон.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="MIYAGI")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/Моя дикая Касандра [remix]   Miyagi.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="Sami Yusuf")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/001_-_Sami_Yusuf_Ollohu_Olloh_(Kach.me).mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="sami yusuf")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/Sami Yusuf - Hasbi Rabbi.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="Zeyneb")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/Talıb Tale & Zeynəb Həsəni - Səbr Elə (Akustik).mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="ZEYNEB")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/Mod - Mustafa Sandal, Zeynep Bastık.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="arabic")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/Нашид - Лабайк.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="ARABIC")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/2_5195080630357986535.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="uf")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/russkiy_perevod_nasheed_kuntu_maytan_sulim_akharshaev_ibragim_saypuev.mp3", "rb"),
        f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="ok")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/music.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="uzb")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/yorqinxoja-umarov-yomgir.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="UZ")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/Akbarshokh- Salom Farishta (Official Audio).mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="rus")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/zulayha.m4a", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="RU")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/JONY - Комета(MP3_160K)_1.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


# 2 ======================================================================================================


@dp.callback_query_handler(text="Yorqinxoja")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/2_5215394502818140372.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="yorqinxoja")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/Sog indim yomon   Yorqinxo ja Umarov ft Afruza.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text='a1')
async def x(call: CallbackQuery):
    await call.message.answer_photo(open("image/m1000x1000.png", "rb"), reply_markup=menuummon2)
    await call.message.delete()

#----------------------------------------------------------------------------------------------------------------

@dp.callback_query_handler(text="munisa")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/CTOA1LH9WQXHZXTD4T.m4a", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="MUNISA")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/2_5278533077574883149.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text='a2')
async def x(call: CallbackQuery):
    await call.message.answer_photo(open("image/Без названия (2).jpg", "rb"), reply_markup=menushox2)
    await call.message.delete()

#----------------------------------------------------------------------------------------------------------------

@dp.callback_query_handler(text="AVTO")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/Miyagi  и  Andy Panda - Патрон.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="avto")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/Jbl music 🎶 bass boosted 💥🔥.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text='a3')
async def x(call: CallbackQuery):
    await call.message.answer_photo(open("image/Без названия (3).jpg", "rb"), reply_markup=menuavto2)
    await call.message.delete()

#----------------------------------------------------------------------------------------------------------------

@dp.callback_query_handler(text="quluq bass")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/Ты Расскажи Ка Мне.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="QULOQ")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/CJ - WHOOPTY (ERS Remix) Baby Driver.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text='a4')
async def x(call: CallbackQuery):
    await call.message.answer_photo(open("image/Без названия.jpg", "rb"), reply_markup=menuquloqchin2)
    await call.message.delete()

#-----------------------------------------------------------------------------------------------------------------

@dp.callback_query_handler(text="on")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/Лилии.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="joy")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/Аллея (www.mp3erger.ru) 2019   JONY.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text='a5')
async def x(call: CallbackQuery):
    await call.message.answer_photo(open("image/images.jpg", "rb"), reply_markup=menujony1)
    await call.message.delete()

#------------------------------------------------------------------------------------------------------------------

@dp.callback_query_handler(text="tim")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/YAMAKASI CD 1 TRACK 7 (320).mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="TIM")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/peacebass]   Miyagi   Эндшпиль.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text='a6')
async def x(call: CallbackQuery):
    await call.message.answer_photo(open("image/Без названия (4).jpg", "rb"), reply_markup=menutimmati2)
    await call.message.delete()

#--------------------------------------------------------------------------------------------------------------------

@dp.callback_query_handler(text="SAMI")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/2_5406592526847053717.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="sami")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/Sami_Yusuf_Allahu_allah_ifasında.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text='a7')
async def x(call: CallbackQuery):
    await call.message.answer_photo(open("image/Без названия (5).jpg", "rb"), reply_markup=menusami2)
    await call.message.delete()

#--------------------------------------------------------------------------------------------------------------------

@dp.callback_query_handler(text="TOLIB")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/Ayten Resul - Niye Söndü Eşk.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="tolib")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/Ayaz_erdoğan_hep_mı_ben_slowed+reverbZhernusi_kurdi_ژێرنووسی_کوردی.mp3", "rb"),
        f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text='a8')
async def x(call: CallbackQuery):
    await call.message.answer_photo(open("image/Без названия.jpg", "rb"), reply_markup=menutolib1)
    await call.message.delete()

#---------------------------------------------------------------------------------------------------------------

@dp.callback_query_handler(text="nasheed")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/Nasheed_Taweel_Alshawq_Ahmed_Bukhatir_أحمد_بوخاطر_نشيد_طويل_الشوق.mp3", "rb"),
        f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="1NASHEED")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/Nasheed.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text='a9')
async def x(call: CallbackQuery):
    await call.message.answer_photo(open("image/Без названия.jpg", "rb"), reply_markup=menuprog)
    await call.message.delete()

#-----------------------------------------------------------------------------------------------------------------

@dp.callback_query_handler(text="gv")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/Ya Nabi Salam Alaika _ Maher Zain _ Arabic _ Without Music.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="ll")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/Nasheed Habibi Muhammad, Mishary Rashid Alafasy.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="a10")
async def x(call: CallbackQuery):
    await call.message.answer_photo(open("image/Без названия.jpg", "rb"), reply_markup=menuabu)
    await call.message.delete()


@dp.callback_query_handler(text="NON")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/Green_71_Yure_Yiglama_Primiera_UzRap.medium.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="mon")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/DJ Green - Ey Tyolka @dj_green_channel.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="y2")
async def x(call: CallbackQuery):
    await call.message.answer_photo(open("image/Без названия.jpg", "rb"), reply_markup=menuozb1)
    await call.message.delete()


@dp.callback_query_handler(text="russia1")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/Ya Nabi Salam Alaika _ Maher Zain _ Arabic _ Without Music.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="russia2")
async def sample(call: CallbackQuery):
    await call.message.answer_audio(
        open("music/Nasheed Habibi Muhammad, Mishary Rashid Alafasy.mp3", "rb"), f"Dostlarga Ulashamiza!")
    await call.message.delete()


@dp.callback_query_handler(text="o1")
async def x(call: CallbackQuery):
    await call.message.answer_photo(open("image/Без названия.jpg", "rb"), reply_markup=menuru1)
    await call.message.delete()

#--------------------------------------------------------------------------------------------------------------------

@dp.callback_query_handler(text='b1')
async def x(call: CallbackQuery):
    await call.message.answer_photo(open("image/m1000x1000.png", "rb"), reply_markup=menuummon)
    await call.message.delete()


@dp.callback_query_handler(text='b2')
async def x(call: CallbackQuery):
    await call.message.answer_photo(open("image/Без названия (2).jpg", "rb"), reply_markup=menushox)
    await call.message.delete()


@dp.callback_query_handler(text='b3')
async def x(call: CallbackQuery):
    await call.message.answer_photo(open("image/Без названия (3).jpg", "rb"), reply_markup=menuavto)
    await call.message.delete()


@dp.callback_query_handler(text='k1')
async def x(call: CallbackQuery):
    await call.message.answer_photo(open("image/Без названия.jpg", "rb"), reply_markup=menuquloqchin)
    await call.message.delete()

@dp.callback_query_handler(text='b5')
async def x(call: CallbackQuery):
    await call.message.answer_photo(open("image/images.jpg", "rb"), reply_markup=menujony)
    await call.message.delete()

@dp.callback_query_handler(text='h6')
async def x(call: CallbackQuery):
    await call.message.answer_photo(open("image/Без названия (4).jpg", "rb"), reply_markup=menutimmati)
    await call.message.delete()

@dp.callback_query_handler(text='b7')
async def x(call: CallbackQuery):
    await call.message.answer_photo(open("image/Без названия (5).jpg", "rb"), reply_markup=menusami)
    await call.message.delete()

@dp.callback_query_handler(text='b8')
async def x(call: CallbackQuery):
    await call.message.answer_photo(open("image/Без названия.jpg", "rb"), reply_markup=menutolib)
    await call.message.delete()

@dp.callback_query_handler(text='b9')
async def x(call: CallbackQuery):
    await call.message.answer_photo(open("image/Без названия.jpg", "rb"), reply_markup=menuarab)
    await call.message.delete()

@dp.callback_query_handler(text='b11')
async def x(call: CallbackQuery):
    await call.message.answer_photo(open("image/Без названия.jpg", "rb"), reply_markup=menuarab1)
    await call.message.delete()

@dp.callback_query_handler(text='m1')
async def x(call: CallbackQuery):
    await call.message.answer_photo(open("image/Без названия.jpg", "rb"), reply_markup=menuru)
    await call.message.delete()

@dp.callback_query_handler(text='uba')
async def x(call: CallbackQuery):
    await call.message.answer_photo(open("image/Без названия.jpg", "rb"), reply_markup=menuuzb)
    await call.message.delete()




@dp.callback_query_handler(text='❌')
async def x(call: CallbackQuery):
    await call.message.delete()


if __name__ == "__main__":
    executor.start_polling(dp)
