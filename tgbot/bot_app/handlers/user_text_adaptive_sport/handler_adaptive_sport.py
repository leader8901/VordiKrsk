from aiogram import types
from tgbot.bot_app.app import dp
from tgbot.bot_app.handlers.navigation import Handler

from tgbot.bot_app.information.adaptive_info_text.text_info_adaptive_sport import *
from tgbot.bot_app.keybords.adaptive_sports.adaptive_sports_kb import markup_adaptiv_sport
from tgbot.bot_app.keybords.keyboards_menu import keyboard_beck_menu

text = "адаптивный спорт"
"""-----------"""
text1 = "спорт слепых"
text2 = "спорт глухих"
text3 = "сорт пода (поражение опорно-двигательного аппарата)"
text4 = "теннис на колясках"
text5 = "следж хоккей"
text6 = "спорт лин (лиц с интеллектуальными нарушениями)"
text7 = "футбол"
text8 = "афк (адаптивно-физическая культура)"
text9 = "иппотерапия"
text10 = "аква ОВ3"
text11 = "шаг за шагом к мечте"
kb_back_btn = keyboard_beck_menu()
handler = Handler


@dp.message_handler(lambda message: message.text.lower() == text)
async def text_adaptiv_sport(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=text, reply_markup=markup_adaptiv_sport)


@dp.message_handler(lambda message: message.text.lower() == text1)
async def text_sport_of_the_blind(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=sport_of_the_blind, reply_markup=kb_back_btn)


@dp.message_handler(lambda message: message.text.lower() == text2)
async def text_avia(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=sports_of_the_deaf, reply_markup=kb_back_btn)


@dp.message_handler(lambda message: message.text.lower() == text3)
async def text_avia(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=sort_poda, reply_markup=kb_back_btn)


@dp.message_handler(lambda message: message.text.lower() == text4)
async def text_avia(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=tennis_na_kolesax, reply_markup=kb_back_btn)


@dp.message_handler(lambda message: message.text.lower() == text5)
async def text_avia(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=skedj_xokkey, reply_markup=kb_back_btn)
    Handler.display_menu(text5)


@dp.message_handler(lambda message: message.text.lower() == text6)
async def text_avia(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=sport_lin, reply_markup=kb_back_btn)
    Handler.display_menu(text6)


@dp.message_handler(lambda message: message.text.lower() == text7)
async def text_avia(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=futbool, reply_markup=kb_back_btn)
    Handler.display_menu(text7)


@dp.message_handler(lambda message: message.text.lower() == text8)
async def text_avia(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=afk, reply_markup=kb_back_btn)
    Handler.display_menu(text8)


@dp.message_handler(lambda message: message.text.lower() == text9)
async def text_avia(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=ippoterapia, reply_markup=kb_back_btn)
    Handler.display_menu(text9)


@dp.message_handler(lambda message: message.text.lower() == text10)
async def text_avia(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=akva_ob3, reply_markup=kb_back_btn)
    Handler.display_menu(text10)


@dp.message_handler(lambda message: message.text.lower() == text11)
async def text_avia(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=step_by_step, reply_markup=kb_back_btn)
    Handler.display_menu(text11)


@dp.message_handler(lambda message: message.text.lower() == 'назад')
async def back_button_handler(message: types.Message):
    Handler.handle_message(message)
    # chat_id = message.chat.id
    # previous_option = Handler.handle_message() # Get the previous menu option from the navigation stack
    # if previous_option is not None:
    #     pop_menu_option()  # Remove the current menu option from the navigation stack
    #     if previous_option == text1:
    #         await message.reply(text=text, reply_markup=markup_adaptiv_sport)
    #     elif previous_option == text2:
    #         await message.reply(text=text, reply_markup=markup_adaptiv_sport)
    #     elif previous_option == text3:
    #         await message.reply(text=text, reply_markup=markup_adaptiv_sport)
    #     elif previous_option == text4:
    #         await message.reply(text=text, reply_markup=markup_adaptiv_sport)
    #     elif previous_option == text5:
    #         await message.reply(text=text, reply_markup=markup_adaptiv_sport)
    #     elif previous_option == text5:
    #         await message.reply(text=text, reply_markup=markup_adaptiv_sport)
    #     elif previous_option == text6:
    #         await message.reply(text=text, reply_markup=markup_adaptiv_sport)
    #     elif previous_option == text7:
    #         await message.reply(text=text, reply_markup=markup_adaptiv_sport)
    #     elif previous_option == text8:
    #         await message.reply(text=text, reply_markup=markup_adaptiv_sport)
    #     elif previous_option == text9:
    #         await message.reply(text=text, reply_markup=markup_adaptiv_sport)
    #     elif previous_option == text10:
    #         await message.reply(text=text, reply_markup=markup_adaptiv_sport)
    #     elif previous_option == text11:
    #         await message.reply(text=text, reply_markup=markup_adaptiv_sport)
    # Add more conditions for other menu options...
