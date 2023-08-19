from tgbot.bot_app.app import dp, bot
from aiogram import types

from tgbot.bot_app.information.erly_help_text_info.erly_help_general import *
from tgbot.bot_app.keybords.early_help.kb_early_help import markup_erly_help

text1 = "ранняя помощь"
text2 = "общее"
text3 = "нормативно правовые документы, регламентирующие работу системы ранней помощи в российской федерации"
text4 = "учреждения и организации, оказывающие услуги ранней помощи в красноярском крае"
text5 = "кгбу со \"реабилитационный центр для детей и подростков с ограниченными возможностями \"радуга\""
text6 = "региональная общественная организация \"красноярский центр лечебной педагогики\""


@dp.message_handler(lambda message: message.text.lower() == text1)
async def text_erly_help(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text='Ранняя помощь', reply_markup=markup_erly_help)


@dp.message_handler(lambda message: message.text.lower() == text2)
async def text_erly_general(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=text_info_1, reply_markup=markup_erly_help)


@dp.message_handler(lambda message: message.text.lower() == text3)
async def text_erly_general(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=text_info_2, reply_markup=markup_erly_help)


@dp.message_handler(lambda message: message.text.lower() == text4)
async def text_erly_general(message: types.Message):
    chat_id = message.chat.id
    MAX_MESSAGE_LENGTH = 4096
    # Разбить сообщение на куски максимального размера, разрешенного API
    # так как тест ооооочееень большой (
    chunks = [text_info_3[i:i + MAX_MESSAGE_LENGTH] for i in range(0, len(text_info_3), MAX_MESSAGE_LENGTH)]
    # Отправляем каждый кусок текста как отдельное сообщение
    for chunk in chunks:
        await bot.send_message(chat_id, text=chunk, reply_markup=markup_erly_help)


@dp.message_handler(lambda message: message.text.lower() == text5)
async def text_erly_general(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=text_info_4, reply_markup=markup_erly_help)


@dp.message_handler(lambda message: message.text.lower() == text6)
async def text_erly_general(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=text_info_5, reply_markup=markup_erly_help)
