from aiogram import types
import json
from tgbot.bot_app.app import dp
from tgbot.bot_app.information.avia_and_rain.text_info_avia import *
from tgbot.bot_app.information.avia_and_rain.text_info_rain import *

from tgbot.bot_app.app import db
from tgbot.bot_app.keybords.kb_avia_rain.keybords_avia_rain import *
from tgbot.bot_app.keybords.keyboards_menu import keyboard_beck_menu, menu_main

avia_railways = keyboard_for_avia_railways()
railways_kb_menu = keyboard_for_railways_menu()
back_kb = keyboard_beck_menu()
main_menu = menu_main()


@dp.message_handler(lambda message: message.text.lower() == "авиа и жд")
async def text_avia_rain(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text='Авиа и ЖД', reply_markup=avia_railways)
    # user_data = {"menu_stack": ["user_text_avia_rain"]}
    # user_data_json = json.dumps(user_data)
    # db.add_user_state(user_data_json, chat_id)


@dp.message_handler(lambda message: message.text.lower() == "жд", )
async def text_rain(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text='ЖД', reply_markup=railways_kb_menu)
    # user_data = {"menu_stack": ["user_text_avia_rain", "user_text_avia_rain", "text_rain"]}
    # await update_user_data(user_data, chat_id)


"""<--------ЖД меню------->"""


@dp.message_handler(lambda message: message.text.lower() == "железнодорожный вокзал красноярска")
async def text_rain_krasnoyars(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=Railway_station_of_Krasnoyarsk, reply_markup=back_kb)
    # user_data = {
    # "menu_stack": ["user_text_avia_rain", "user_text_avia_rain", "text_rain", "text_avia_krasnoyars", "text_parking_own_am"]}
    # await update_user_data(user_data, chat_id)


@dp.message_handler(lambda message: message.text.lower() == "парковка личного тс жд")
async def text_parking_own_am_rain(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=Parking_own_car, reply_markup=back_kb)
    # user_data = {
    # "menu_stack": ["user_text_avia_rain", "user_text_avia_rain", "text_rain", "text_avia_krasnoyars", "text_parking_own_am"]}
    # await update_user_data(user_data, chat_id)


@dp.message_handler(lambda message: message.text.lower() == "услуги сопровождения на жд вокзале")
async def text_service_rainway(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=Services_railway_station, reply_markup=back_kb)
    # user_data = {
    # "menu_stack": ["user_text_avia_rain", "user_text_avia_rain", "text_rain", "text_avia_krasnoyars", "text_parking_own_am"]}
    # await update_user_data(user_data, chat_id)


@dp.message_handler(
    lambda message: message.text.lower() == "комнаты длительного отдыха, комната матери и ребенка, зал отдыха")
async def text_rooms_long_recreation(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=rooms_mother_child_room, reply_markup=back_kb)
    # user_data = {
    # "menu_stack": ["user_text_avia_rain", "user_text_avia_rain", "text_rain", "text_avia_krasnoyars", "text_parking_own_am"]}
    # await update_user_data(user_data, chat_id)


@dp.message_handler(lambda message: message.text.lower() == "специализированные вагоны")
async def text_specialized_wagons(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=specialized_wagons, reply_markup=back_kb)
    # user_data = {
    # "menu_stack": ["user_text_avia_rain", "user_text_avia_rain", "text_rain", "text_avia_krasnoyars", "text_parking_own_am"]}
    # await update_user_data(user_data, chat_id)


@dp.message_handler(lambda message: message.text.lower() == "условия оформления билетов на специализированные места")
async def text_uslugi_oformleniya_mest(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=Conditions_issuing_ticket_seats, reply_markup=back_kb)
    # user_data = {
    # "menu_stack": ["user_text_avia_rain", "user_text_avia_rain", "text_rain", "text_avia_krasnoyars", "text_parking_own_am"]}
    # await update_user_data(user_data, chat_id)


@dp.message_handler(
    lambda message: message.text.lower() == "4-х местное специализированное купе в поездах дальнего следования")
async def specialized_kupe_wagons(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=seater4_specialized_compartment_long_distance, reply_markup=back_kb)
    # user_data = {
    # "menu_stack": ["user_text_avia_rain", "user_text_avia_rain", "text_rain", "text_avia_krasnoyars", "text_parking_own_am"]}
    # await update_user_data(user_data, chat_id)


@dp.message_handler(lambda message: message.text.lower() == "скидки при покупке билетов")
async def diskond_buying_ticket(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=Discounts_buying_tickets, reply_markup=back_kb)
    # user_data = {
    # "menu_stack": ["user_text_avia_rain", "user_text_avia_rain", "text_rain", "text_avia_krasnoyars", "text_parking_own_am"]}
    # await update_user_data(user_data, chat_id)


@dp.message_handler(lambda message: message.text.lower() == "услуги камер хранения")
async def luggage_storage_services(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=Luggage_storage_services, reply_markup=back_kb)
    # user_data = {
    # "menu_stack": ["user_text_avia_rain", "user_text_avia_rain", "text_rain", "text_avia_krasnoyars", "text_parking_own_am"]}
    # await update_user_data(user_data, chat_id)


@dp.message_handler(lambda message: message.text.lower() == "видеоконсультация для инвалидов по слуху")
async def video_consultation_impaired(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text=Video_consultation_hearing_impaired, reply_markup=back_kb)
    # user_data = {
    # "menu_stack": ["user_text_avia_rain", "user_text_avia_rain", "text_rain", "text_avia_krasnoyars", "text_parking_own_am"]}
    # await update_user_data(user_data, chat_id)


@dp.message_handler(lambda message: message.text.lower() == "главное меню")
async def back_main_menu(message: types.Message):
    chat_id = message.chat.id
    await message.reply(text='Главное меню', reply_markup=main_menu)





"""text_avia_krasnoyars", "text_parking_own_am",
"text_servics_in_avia", "text_transfer_electro_texnik", "text_rest_rooms",
"text_service_on_board", "text_transportation_patient", "text_transfer_elizarova",
"transportation_dogs_passenger", "transportation_oxygen_concentrator"""

"""
import sqlite3
import json
conn.commit()

# define user_data
user_data = {"menu_stack": ["menu1", "menu2"]}

# serialize user_data as JSON string
user_data_json = json.dumps(user_data)

# save user_data in database
user_id = 123
cursor.execute("INSERT OR REPLACE INTO user_states (user_id, user_data) VALUES (?, ?)", (user_id, user_data_json))
conn.commit()
"""
