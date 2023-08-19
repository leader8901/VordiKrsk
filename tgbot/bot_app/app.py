# import environ
from aiogram import Bot, types
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
# from connect_db.condb import SQLighter
from aiogram.dispatcher.storage import BaseStorage

from tgbot.bot_app.config import TOKEN

# env = environ.Env()
# environ.Env.read_env()

# TOKEN = env('TOKEN')
from tgbot.bot_app.conndb.sglighter import SQLighter

db = SQLighter('vordi_db.db')
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)











"""
# create states
class MyStates(StatesGroup):
    STATE_ONE = State()
    STATE_TWO = State()

# create menus
MAIN_MENU = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Menu 1'),
            KeyboardButton(text='Menu 2'),
        ]
    ],
    resize_keyboard=True
)

MENU_1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Submenu 1'),
            KeyboardButton(text='Submenu 2'),
        ],
        [
            KeyboardButton(text='Back')
        ]
    ],
    resize_keyboard=True
)

MENU_2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Option 1'),
            KeyboardButton(text='Option 2'),
        ],
        [
            KeyboardButton(text='Back')
        ]
    ],
    resize_keyboard=True
)

# handler for /start command
@dp.message_handler(commands=['start'])
async def handle_start(message: Message):
    # clear menu history
    storage.set_data(user=message.from_user.id, data={'menu_history': []})
    await message.answer('Welcome to the main menu!', reply_markup=MAIN_MENU)
    # update state in database
    storage.set_state(message.from_user.id, 'STATE_ONE')
    await MyStates.STATE_ONE.set()

# handler for STATE_ONE state
@dp.message_handler(state=MyStates.STATE_ONE)
async def handle_state_one(message: Message):
    # get current menu history
    menu_history = storage.get_data(user=message.from_user.id).get('menu_history', [])

    if message.text == 'Menu 1':
        # add current menu to menu history
        menu_history.append(MENU_1)
        # update menu history in database
        storage.set_data(user=message.from_user.id, data={'menu_history': menu_history})
        await message.answer('You are in Menu 1!', reply_markup=MENU_1)
    elif message.text == 'Menu 2':
        # add current menu to menu history
        menu_history.append(MENU_2)
        # update menu history in database
        storage.set_data(user=message.from_user.id, data={'menu_history': menu_history})
        await message.answer('You are in Menu 2!', reply_markup=MENU_2)
    else:
        await message.answer('Invalid input!')

# handler for MENU_1 menu
@dp.message_handler(lambda message: message.text in ['Submenu 1', 'Submenu 2'], state=MyStates.STATE_ONE)
async def handle_submenu(message: Message):
    # get current menu history
    menu_history = storage.get_data(user=message.from_user.id).get('menu_history', [])

    if message.text == 'Back':
        # remove current menu from menu history
        if len(menu_history) > 0:
            menu_history.pop()
        # update menu history in database
        storage.set_data(user=message.from_user.id,"""
