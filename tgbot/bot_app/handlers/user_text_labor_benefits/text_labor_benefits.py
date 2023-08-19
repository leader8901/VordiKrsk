from aiogram import types
from tgbot.bot_app.app import dp
from tgbot.bot_app.information.labor_benefits.labor_benefits_info import *
from tgbot.bot_app.keybords.keyboards_menu import keyboard_beck_menu
from tgbot.bot_app.keybords.labor_benefits.keyboard_labor_benefits import labor_benefits

menu_labor_benefits = labor_benefits()
kb_back_btn = keyboard_beck_menu()
text = "Трудовые льготы"

text1 = "Для родителей детей-инвалидов"
text2 = "Для работника с инвалидностью 1 группы"
text3 = "Для работника с инвалидностью 2 группы"
text4 = "Для работника с инвалидностью 3 группы"


@dp.message_handler(lambda message: message.text == text)
async def text_avia(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=text, reply_markup=menu_labor_benefits)


@dp.message_handler(lambda message: message.text == text1)
async def text_avia(message: types.Message):
    chat_id = message.chat.id
    MAX_MESSAGE_LENGTH = 4096
    # Разбить сообщение на куски максимального размера, разрешенного API
    # так как тест ооооочееень большой (
    chunks = [for_parents_of_disabled_children[i:i + MAX_MESSAGE_LENGTH] for i in
              range(0, len(for_parents_of_disabled_children), MAX_MESSAGE_LENGTH)]
    # Отправляем каждый кусок текста как отдельное сообщение
    for chunk in chunks:
        await message.reply(text=chunk, reply_markup=kb_back_btn)


@dp.message_handler(lambda message: message.text == text2)
async def text_avia(message: types.Message):
    chat_id = message.chat.id
    MAX_MESSAGE_LENGTH = 4096
    # Разбить сообщение на куски максимального размера, разрешенного API
    # так как тест ооооочееень большой (
    chunks = [for_an_employee_with_a_disability1[i:i + MAX_MESSAGE_LENGTH] for i in
              range(0, len(for_an_employee_with_a_disability1), MAX_MESSAGE_LENGTH)]
    # Отправляем каждый кусок текста как отдельное сообщение
    for chunk in chunks:
        await message.reply(text=chunk, reply_markup=kb_back_btn)


@dp.message_handler(lambda message: message.text == text3)
async def text_avia(message: types.Message):
    chat_id = message.chat.id
    MAX_MESSAGE_LENGTH = 4096
    # Разбить сообщение на куски максимального размера, разрешенного API
    # так как тест ооооочееень большой (
    chunks = [for_an_employee_with_a_disability2[i:i + MAX_MESSAGE_LENGTH] for i in
              range(0, len(for_an_employee_with_a_disability2), MAX_MESSAGE_LENGTH)]
    # Отправляем каждый кусок текста как отдельное сообщение
    for chunk in chunks:
        await message.reply(text=chunk, reply_markup=kb_back_btn)


@dp.message_handler(lambda message: message.text == text4)
async def text_avia(message: types.Message):
    chat_id = message.chat.id
    MAX_MESSAGE_LENGTH = 4096
    # Разбить сообщение на куски максимального размера, разрешенного API
    # так как тест ооооочееень большой (
    chunks = [for_an_employee_with_a_disability3[i:i + MAX_MESSAGE_LENGTH] for i in
              range(0, len(for_an_employee_with_a_disability3), MAX_MESSAGE_LENGTH)]
    # Отправляем каждый кусок текста как отдельное сообщение
    for chunk in chunks:
        await message.reply(text=chunk, reply_markup=kb_back_btn)
