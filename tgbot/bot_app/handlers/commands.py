from tgbot.bot_app import bot

from tgbot.bot_app.app import dp
from tgbot.bot_app.keybords.keyboards_menu import menu_main

main_keyboard = menu_main()


@dp.message_handler(commands=['start'])
async def start_message(message):
    chat_id = message.chat.id
    info_mes = f'Приветствуем Вас в информационном чате, созданном РО ВОРДИ Красноярского края.\n' \
               f'\n' \
               f'Для Вашего удобства мы собрали и разделили всю информацию по темам.\n' \
               f'Выбирайте интересующий Вас раздел ⬇️ и приступайте к изучению.\n' \
               f'Если не найдёте ответ или Вам потребуется помощь, ' \
               f'оставьте обращение в семейные приёмные - \n' \
               f'\n' \
               f'help.vordi.org'
    await message.answer(info_mes, reply_markup=main_keyboard)
