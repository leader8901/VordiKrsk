from aiogram import types

from tgbot.bot_app.app import dp
from tgbot.bot_app.handlers.navigation import *
from tgbot.bot_app.information.avia_and_rain.text_info_avia import *
from tgbot.bot_app.keybords.kb_avia_rain.keybords_avia_rain import keyboards_for_avia_menu
from tgbot.bot_app.keybords.keyboards_menu import keyboard_beck_menu, menu_main
from tgbot.bot_app.app import storage

kb_back_menu = keyboard_beck_menu()
main_menu = menu_main()
kb_avia = keyboards_for_avia_menu()
# Initialize an empty stack
navigation_stack = []

text = "авиа"
"""-----------"""
text1 = "аэропорт красноярск"
text2 = "парковка личного тс"
text3 = "услуги сопровождения в аэропорту"
text4 = "перевозка кресло-коляски с электрическим приводом"
text5 = "комнаты отдыха, комната матери и ребенка, зал повышенной комфортности"
text6 = "обслуживание на борту"
text7 = "перевозка больного на носилках"
text8 = "перевозка пассажиров с гипсовой повязкой, ортезом, аппаратом илизарова"
text9 = "перевозка собаки-проводника пассажиром с инвалидностью по зрению"
text10 = "перевозка концентратора кислорода"


@dp.message_handler(lambda message: message.text.lower() == text)
async def text_avia(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text='Авиа', reply_markup=kb_avia)


@dp.message_handler(lambda message: message.text.lower() == text1)
async def text_avia_krasnoyarsk(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=AEROPORT_KRASNOYARSK, reply_markup=kb_back_menu)


@dp.message_handler(lambda message: message.text.lower() == text2)
async def text_parking_own_am(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=PARKOVKA_LICNOGO_TC, reply_markup=kb_back_menu)


@dp.message_handler(lambda message: message.text.lower() == text3)
async def text_servics_in_avia(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=USLUGI_SOPROVOJDENIYA_V_AEROPORT, reply_markup=kb_back_menu)


@dp.message_handler(lambda message: message.text.lower() == text4)
async def text_transfer_electro_texnik(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=PEREМOVKA_KRESLO_KOL_S_ELEKTRO_PRIV, reply_markup=kb_back_menu)


@dp.message_handler(
    lambda message: message.text.lower() == text5)
async def text_rest_rooms(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=KOMNATA_MAT_DETYA, reply_markup=kb_back_menu)


@dp.message_handler(lambda message: message.text.lower() == text6)
async def text_service_on_board(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=OBSLUJIVANIYA_NA_BORTU, reply_markup=kb_back_menu)


@dp.message_handler(lambda message: message.text.lower() == text7)
async def text_transportation_patient(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=PEREVOZKA_BOLNOGO_NA_NASILKA, reply_markup=kb_back_menu)


@dp.message_handler(lambda message: message.text.lower() == text8)
async def text_transfer_elizarova(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=PEREVOZKA_S_APARATOM_ILZAROVA, reply_markup=kb_back_menu)


@dp.message_handler(lambda message: message.text.lower() == text9)
async def transportation_dogs_passenger(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=PEREVOZKA_SOBAKI_POVODIR, reply_markup=kb_back_menu)


@dp.message_handler(lambda message: message.text.lower() == text10)
async def transportation_oxygen_concentrator(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=PEREVOZKA_KONCETRAT_KISLOROD, reply_markup=kb_back_menu)


