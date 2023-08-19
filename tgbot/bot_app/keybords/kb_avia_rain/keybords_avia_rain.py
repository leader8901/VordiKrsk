from aiogram import types


def keyboard_for_avia_railways():
    markup_avia_rain = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Авиа')
    btn2 = types.KeyboardButton('ЖД')
    btn4 = types.KeyboardButton('Главное меню')
    markup_avia_rain.add(btn1, btn2, btn4)
    return markup_avia_rain


def keyboards_for_avia_menu():
    """Кнопки для главного меню Авиа"""
    markup_avia = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('Аэропорт Красноярск')
    btn2 = types.KeyboardButton('Парковка личного ТС')
    btn3 = types.KeyboardButton('Услуги сопровождения в аэропорту')
    btn4 = types.KeyboardButton('Перевозка кресло-коляски с электрическим приводом')
    btn5 = types.KeyboardButton('Комнаты отдыха, комната матери и ребенка, зал повышенной комфортности')
    btn6 = types.KeyboardButton('Обслуживание на борту')
    btn7 = types.KeyboardButton('Перевозка больного на носилках')
    btn8 = types.KeyboardButton('Перевозка пассажиров с гипсовой повязкой, ортезом, аппаратом Илизарова')
    btn9 = types.KeyboardButton('Перевозка собаки-проводника пассажиром с инвалидностью по зрению')
    btn10 = types.KeyboardButton('Перевозка концентратора кислорода')
    btn11 = types.KeyboardButton('Назад')
    btn12 = types.KeyboardButton('Главное меню')
    markup_avia.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11)
    return markup_avia


def keyboard_for_railways_menu():
    """Кнопки для меню ЖД"""
    markup_railways = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('Железнодорожный вокзал Красноярска')
    btn2 = types.KeyboardButton('Парковка личного ТС ЖД')
    btn3 = types.KeyboardButton('Услуги сопровождения на ЖД вокзале')
    btn4 = types.KeyboardButton('Комнаты длительного отдыха, комната матери и ребенка, зал отдыха')
    btn5 = types.KeyboardButton('Специализированные вагоны')
    btn6 = types.KeyboardButton('Условия оформления билетов на специализированные места')
    btn7 = types.KeyboardButton('4-х местное специализированное купе в поездах дальнего следования')
    btn8 = types.KeyboardButton('Скидки при покупке билетов')
    btn9 = types.KeyboardButton('Услуги камер хранения')
    btn10 = types.KeyboardButton('Видеоконсультация для инвалидов по слуху')
    btn11 = types.KeyboardButton('Назад')
    btn12 = types.KeyboardButton('Главное меню')
    markup_railways.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12)
    return markup_railways
