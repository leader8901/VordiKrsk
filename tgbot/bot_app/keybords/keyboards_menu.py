from aiogram import types


def menu_main():
    # Create the keyboard for menu 2
    """Кнопки для главного меню после старта"""
    markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Соц.защита')
    btn2 = types.KeyboardButton('Ранняя помощь')
    btn3 = types.KeyboardButton('Образование')
    btn4 = types.KeyboardButton('Медицина')
    btn5 = types.KeyboardButton('Трудовые льготы')
    btn6 = types.KeyboardButton('МСЭ и ТСР')
    btn7 = types.KeyboardButton('Доступная среда')
    btn8 = types.KeyboardButton('Недееспособность')
    btn9 = types.KeyboardButton('Соц.реабилитация')
    btn10 = types.KeyboardButton('Пенсия, налоги')
    btn11 = types.KeyboardButton('Адаптивный спорт')
    btn12 = types.KeyboardButton('Авиа и ЖД')
    btn13 = types.KeyboardButton('Семейные приёмные')
    markup_menu.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13)
    return markup_menu


def keyboard_beck_menu():
    btn1 = types.KeyboardButton('Назад')
    btn2 = types.KeyboardButton('Главное меню')
    markup_back_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup_back_menu.add(btn1, btn2)
    return markup_back_menu
