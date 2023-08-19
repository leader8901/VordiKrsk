from aiogram import types

"""Кнопки для главного меню Адаптивный спорт"""
btn1 = types.KeyboardButton('Спорт слепых')
btn2 = types.KeyboardButton('Спорт глухих')
btn3 = types.KeyboardButton('Сорт ПОДА (поражение опорно-двигательного аппарата)')
btn4 = types.KeyboardButton('Теннис на колясках')
btn5 = types.KeyboardButton('Следж хоккей')
btn6 = types.KeyboardButton('Спорт ЛИН (лиц с интеллектуальными нарушениями)')
btn7 = types.KeyboardButton('Футбол')
btn8 = types.KeyboardButton('АФК (адаптивно-физическая культура)')
btn9 = types.KeyboardButton('Аква ОВЗ')
btn10 = types.KeyboardButton('Шаг за шагом к мечте')
btn11 = types.KeyboardButton('Назад')
btn12 = types.KeyboardButton('Главное меню')
markup_adaptiv_sport = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
markup_adaptiv_sport.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn11, btn12)
