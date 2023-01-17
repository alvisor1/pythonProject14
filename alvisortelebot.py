# 5965364262:AAFRbO5o3LnpibT7fyx0N4wjPyXmlEa32gI
import telebot
from telebot import types

bot = telebot.TeleBot("***", parse_mode='html')
import datetime
token = '5965364262:AAFRbO5o3LnpibT7fyx0N4wjPyXmlEa32gI'
bot = telebot.TeleBot(token)

def create_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    drink_btn = types.InlineKeyboardButton(text='Хочу пить!', callback_data='1')
    eat_btn = types.InlineKeyboardButton(text='Хочу есть!', callback_data='2')
    game_btn = types.InlineKeyboardButton(text='Хочу гулять!', callback_data='3')
    sleap_btn = types.InlineKeyboardButton(text='Хочу спать!', callback_data='4')
    shutka_btn = types.InlineKeyboardButton(text='Хочу шутку!', callback_data='5')
    pogoda_btn = types.InlineKeyboardButton(text='Прогноз погоды', callback_data='6')
    zavershit = types.InlineKeyboardButton(text='ЗАВЕРШИТЬ!', callback_data='0')
    keyboard.add(drink_btn, eat_btn, game_btn, sleap_btn, shutka_btn, pogoda_btn, zavershit)
    return keyboard

@bot.message_handler(commands=['start'])
def start_bot(message):
    klava = create_keyboard()
    bot.send_message(message.chat.id, 'Добрый день! Выберите. что хотите: ', reply_markup=klava)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == '1':
            img = open('www.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption='Картинка воды',
                reply_markup=create_keyboard()
            )
            img.close()
        if call.data == '2':
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo='https://kartinkin.net/uploads/posts/2022-05/1652236333_2-kartinkin-net-p-kartinki-o-yede-2.jpg',
                caption='Картинка еды',
                reply_markup=create_keyboard()
            )
        if call.data == '3':
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo='https://static.carthrottle.com/workspace/uploads/posts/2018/03/0fe169ac20e5debe10cc067ed63759bc.jpg',
                caption='Картинка игры',
                reply_markup=create_keyboard()
            )
        if call.data == '4':
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo='https://volkovysk.by/uploaded/thumbnails/5ec2494ea1527.jpg',
                caption='Картинка сна',
                reply_markup=create_keyboard()
            )
        if call.data == '5':
            None
        if call.data == '6':
            None
        if call.data == '0':
            exit(0)
bot.polling(non_stop=True)
