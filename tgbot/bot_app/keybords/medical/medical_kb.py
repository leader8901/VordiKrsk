from aiogram import types


def social_protection_keyboard():
    """Кнопки для главного меню Соц защита"""
    btn1 = types.KeyboardButton('Оказание мед.помощи')
    btn2 = types.KeyboardButton('')
    btn3 = types.KeyboardButton('')
    btn4 = types.KeyboardButton('')
    btn5 = types.KeyboardButton('')
    btn6 = types.KeyboardButton('')
    btn7 = types.KeyboardButton('')
    btn8 = types.KeyboardButton('')
    btn12 = types.KeyboardButton('Главное меню')
    markup_medical = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup_medical.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn12)
    return markup_medical


def social_protection_keyboard():
    """Кнопки для главного меню Соц защита"""
    btn1 = types.KeyboardButton('Общее')
    btn2 = types.KeyboardButton('Сроки оказания мед.помощи')
    btn3 = types.KeyboardButton('Права при оказании мед.помощи')
    btn4 = types.KeyboardButton('Право выбора мед. организации и врача')
    btn5 = types.KeyboardButton('Право на получение информации о состоянии здоровья')
    btn6 = types.KeyboardButton('Право на отказ от медицинского вмешательства;')
    btn7 = types.KeyboardButton('Обслуживание вне очереди')
    btn8 = types.KeyboardButton('Совместная госпитализация с ребенком-инвалидом, недееспособным')
    btn12 = types.KeyboardButton('Главное меню')
    markup_medical = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup_medical.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn12)
    return markup_medical
"""
1.3 
1.3.1 
1.3.2 
1.3.3 
1.3.4 
1.4 
1.5 Посещение родственника в условиях ОРиТ
1.6 Обслуживание лиц с инвалидностью на дому.
1.7. Реабилитация медицинская
1.7.1 Общее
1.7.2 НПА
1.7.3 Санаторно-курортное лечение
1.7.4 Реабилитации и восстановительное лечение для детей в счет ОМС в
Красноярском крае
1.7.5 Реабилитации и восстановительное лечение для детей в счет ОМС за пределами
края
1.7.5.1  Федеральный научный центр реабилитации инвалидов им Г.А. Альбрехта  .
1.7.5.2 Государственное бюджетное учреждение здравоохранения  Областной
Соль-Илецкий центр медицинской реабилитации 
1.7.5.3 ФГБУ  Евпаторийский военный детский клинический санаторий имени Е.П.
Глинки  Минобороны России
1.7.5.4 Федеральное государственное бюджетное учреждение Российский
реабилитационный центр  Детство 
1.7.5.5 СКК  Вулан, научно-клинический филиал ФГБУ  НМИЦ РК  Минздрава России
1.7.5.6 ФГБУ НИИДИ ФМБА РОССИИ
1.7.5.7 Другие
1.7.6 Реабилитации и восстановительное лечение для инвалидов 18+ в счет ОМС за
пределами региона
1.7.6.1 Реабилитационный центр  Янтарь 
1.7.6.2 Другое
1.7.7 Комплексная реабилитация в условиях организаций социального обслуживания
для детей-инвалидов в Красноярском крае
1.7.7.1 КГБУ СО  Реабилитационный центр  Радуга , Красноярск
1.7.7.2 КГАУ СО "РЦДПсОВ", Ачинск
1.7.7.3 КГБУ СО "Реабилитационный центр для детей "Виктория" , Норильск
1.7.7.4 КГАУ СОЦ "Жарки", Рыбинский район
1.7.7.5 КГАУ СОЦ "Тесь , Минусинск
1.7.7.6 ДРЦ  Виктория  , Минусинск
1.7.8 Частные реабилитационные и физкультурные оздоровительные центры
1.7.8.1 Красноярск
1.7.8.2 Другое
1.8 ВМП
1.9 Получение мед.помощи в другом регионе
1.10 Условия для оплаты проезда"""