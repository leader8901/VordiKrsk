from aiogram import types
from tgbot.bot_app.app import dp
from tgbot.bot_app.information.text_social_protection_info.text_social_protection_info import *
from tgbot.bot_app.keybords.keyboards_menu import keyboard_beck_menu
from tgbot.bot_app.keybords.social_protection import *

# text = "соц.защита"
from tgbot.bot_app.keybords.social_protection.social_protection_kb import *

text = "соц.защита"
text1 = "выплаты"
text2 = "услуги"
text3 = "санаторно-курортное лечение"
text4 = '"социальное такси"'
text5 = "социальная карта"
text6 = "иппсу"
text7 = "северные территории"
text8 = "обеспечение жильем"
text9 = ""
text10 = ""
text11 = ""

text12 = "материальная помощь"
text13 = "компенсации"

text14 = "путевки в лагеря"
text15 = "предоставление услуг сурдопереводчиков инвалидам по слуху"
text16 = "обеспечение компьютерной техникой инвалидов...."
text17 = ""
text18 = ""
text19 = ""
text20 = ""
text21 = ""

markup_soc_protec = social_protection_keyboard()
payments_protection = social_protection_payments()
keyboard_beck = keyboard_beck_menu()
social_service = social_protection_service()


@dp.message_handler(lambda message: message.text.lower() == text)
async def text_avia(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=text, reply_markup=markup_soc_protec)


@dp.message_handler(lambda message: message.text.lower() == text1)
async def text_avia(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=text1, reply_markup=payments_protection)


@dp.message_handler(lambda message: message.text.lower() == text2)
async def text_avia(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=text2, reply_markup=social_service)


@dp.message_handler(lambda message: message.text.lower() == text3)
async def text_avia(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=text3, reply_markup=keyboard_beck)


@dp.message_handler(lambda message: message.text.lower() == text4)
async def text_avia(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=text4, reply_markup=keyboard_beck)


@dp.message_handler(lambda message: message.text.lower() == text5)
async def text_avia(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=text5, reply_markup=keyboard_beck)


@dp.message_handler(lambda message: message.text.lower() == text6)
async def text_avia(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=text6, reply_markup=keyboard_beck)


@dp.message_handler(lambda message: message.text.lower() == text7)
async def text_avia(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=text7, reply_markup=keyboard_beck)


@dp.message_handler(lambda message: message.text.lower() == text8)
async def text_avia(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=text8, reply_markup=keyboard_beck)


@dp.message_handler(lambda message: message.text.lower() == text9)
async def text_avia(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=text9, reply_markup=keyboard_beck)


@dp.message_handler(lambda message: message.text.lower() == text10)
async def text_avia(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=text10, reply_markup=keyboard_beck)


@dp.message_handler(lambda message: message.text.lower() == text11)
async def text_avia(message: types.Message):
    await message.reply(text=text11, reply_markup=keyboard_beck)


@dp.message_handler(lambda message: message.text.lower() == text12)
async def text_avia(message: types.Message):
    await message.reply(text=Material_aid, reply_markup=keyboard_beck)


@dp.message_handler(lambda message: message.text.lower() == text13)
async def text_avia(message: types.Message):
    await message.reply(text=Compensation, reply_markup=keyboard_beck)


@dp.message_handler(lambda message: message.text.lower() == text14)
async def text_avia(message: types.Message):
    await message.reply(text=Vouchers_to_the_camps, reply_markup=keyboard_beck)
