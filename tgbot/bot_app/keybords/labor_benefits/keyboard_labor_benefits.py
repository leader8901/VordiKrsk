from aiogram import types


def labor_benefits():
    """Кнопки для главного меню Адаптивный спорт"""
    btn1 = types.KeyboardButton('Для родителей детей-инвалидов')
    btn2 = types.KeyboardButton('Для работника с инвалидностью 1 группы')
    btn3 = types.KeyboardButton('Для работника с инвалидностью 2 группы')
    btn4 = types.KeyboardButton('Для работника с инвалидностью 3 группы')
    #btn5 = types.KeyboardButton('Назад')
    btn6 = types.KeyboardButton('Главное меню')
    markup_trudoviye = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup_trudoviye.add(btn1, btn2, btn3, btn4, btn6)
    return markup_trudoviye
