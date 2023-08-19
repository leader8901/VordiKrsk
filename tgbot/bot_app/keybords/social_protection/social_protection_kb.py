from aiogram import types


def social_protection_keyboard():
    """Кнопки для главного меню Соц защита"""
    btn1 = types.KeyboardButton('Выплаты')
    btn2 = types.KeyboardButton('Услуги')
    btn3 = types.KeyboardButton('Санаторно-курортное лечение')
    btn4 = types.KeyboardButton('"Социальное такси"')
    btn5 = types.KeyboardButton('Социальная карта')
    btn6 = types.KeyboardButton('ИППСУ')
    btn7 = types.KeyboardButton('Северные территории')
    btn8 = types.KeyboardButton('Обеспечение жильем')
    btn12 = types.KeyboardButton('Главное меню')
    markup_soc_protec = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup_soc_protec.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn12)
    return markup_soc_protec


def social_protection_payments():
    btn1 = types.KeyboardButton('Материальная помощь')
    btn2 = types.KeyboardButton('Единовременная адресная материальная помощь инвалидам-колясочникам,'
                                'проживающим в многоквартирных домах. нуждающимся в преодолении препятствий'
                                'при выходе (входе) в г.Красноярске')
    btn3 = types.KeyboardButton("Единовременная адресная материальная помощь семьям, имеющим "
                                "детей-инвалидов и чей доход, не превышает 1,5-кратную величину прожиточного минимума")
    btn4 = types.KeyboardButton("Адресная материальная помощь при посещении бань")
    btn5 = types.KeyboardButton("Единовременная адресная материальная помощь гражданам, "
                                "находящимся в трудной жизненной ситуации")
    btn6 = types.KeyboardButton("Ежемесячная денежная выплата семьям, состоящим исключительно из "
                                "неработающих инвалидов с детства")
    btn7 = types.KeyboardButton("")
    btn8 = types.KeyboardButton("")
    btn9 = types.KeyboardButton("")
    btn10 = types.KeyboardButton("")
    btn11 = types.KeyboardButton("")
    btn12 = types.KeyboardButton('Главное меню')
    markup_soc_protec_payment = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup_soc_protec_payment.add(btn1, btn2, btn3, btn4, btn5, btn6, btn12)
    return markup_soc_protec_payment


def social_protection_compensation():
    btn1 = types.KeyboardButton('Компенсация расходов в размере 50 % за ЖКУ, найм, кап.ремонт')
    btn2 = types.KeyboardButton('Адресная единовременная материальная помощь на приобретение '
                                'кресла-коляски и слуховые аппараты для ребенка-инвалида родителям (законным '
                                'представителям) детей-инвалидов.')
    btn3 = types.KeyboardButton("Денежная компенсация расходов на проезд к месту проведения "
                                "лечения гемодиализом и обратно")
    btn4 = types.KeyboardButton("Денежная компенсация расходов на оплату проезда к месту проведения "
                                "(обратно) обследования, реабилитации, медико-социальной экспертизы")
    btn5 = types.KeyboardButton("Компенсация затрат родителей (законных представителей) детей-инвалидов, "
                                "обучение которых по основным общеобразовательным программам организовано на"
                                "дому или в форме семейного образования.")
    btn6 = types.KeyboardButton("Компенсация в размере 50 процентов стоимости обучения вождению")
    btn7 = types.KeyboardButton("Компенсации расходов на оплату стоимости проезда проживающим в районах "
                                "Крайнего Севера и приравненных к ним местностях")
    btn8 = types.KeyboardButton("Адресная материальная помощь при посещении бань")
    btn12 = types.KeyboardButton('Главное меню')
    markup_soc_protec_payment = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup_soc_protec_payment.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn12)
    return markup_soc_protec_payment


def social_protection_service():
    """Кнопки для главного меню Соц защита"""
    btn1 = types.KeyboardButton('Путевки в лагеря')
    btn2 = types.KeyboardButton('Предоставление путевок в организации отдыха детей и их оздоровления с полной '
                                'платой их стоимости за счет средств краевого бюджета детям-инвалидам, детям из'
                                'малоимущих семей, детям из многодетных семей')
    btn3 = types.KeyboardButton("""Предоставление бесплатного проезда детям-инвалидам, детям из малоимущих
                                   семей, детям из многодетных семей .....""")
    btn4 = types.KeyboardButton('Организации, оказывающие услуги')
    btn5 = types.KeyboardButton('Рейтинг доступности, отзывы')
    btn12 = types.KeyboardButton('Главное меню')
    markup_soc_protec_service = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup_soc_protec_service.add(btn1, btn2, btn3,btn4, btn5, btn12)
    return markup_soc_protec_service
