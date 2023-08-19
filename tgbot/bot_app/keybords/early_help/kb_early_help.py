from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

"""Кнопки для главного меню Ранняя помощь"""
btn1 = KeyboardButton('Общее')
btn2 = KeyboardButton(
    'Нормативно правовые документы, регламентирующие работу системы ранней помощи в Российской Федерации')
btn3 = KeyboardButton('Учреждения и организации, оказывающие услуги ранней помощи в Красноярском крае')
btn4 = KeyboardButton('КГБУ СО "Реабилитационный центр для детей и подростков с ограниченными возможностями "Радуга"')
btn5 = KeyboardButton('Региональная общественная организация "Красноярский центр лечебной педагогики"')
btn6 = KeyboardButton('Назад')
btn7 = KeyboardButton('Главное меню')
markup_erly_help = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
markup_erly_help.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
