import telebot
from telebot import types
import logistic
import weather

token = logistic.Bot()
my_token = token.token

bot = telebot.TeleBot(my_token)

@bot.message_handler(commands=['start'])
def start(message):
    """
    This is start telebot
    """
    mess = f'Добрый дзен! <b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['help'])
def website(message):
    """
    This is function for button in telegrambot
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton('веб сайт')
    start = types.KeyboardButton('Start')
    markup.add(website, start)
    bot.send_message(message.chat.id, "Zdras'te", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text=='Dneska')
def handle_start(message):
    """
    This button write weather on today
    """
    pogoda = weather_today()
    bot.send_message(message.chat.id, f'{pogoda}')

def weather_today():
    weather_now_today = weather.wea_day()
    return weather_now_today


@bot.message_handler(func=lambda message: message.text == 'веб сайт')
def handle_start(message):
    """
    This button write weather on 5 day
    """
    pogoda = weather_five_day()
    bot.send_message(message.chat.id, f'{pogoda}')


def weather_five_day():
    weather_now_today = weather.wea_five_day()
    return weather_five_day


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    """
    This function open info in chat
    """
    if message.text == 'INFO':
        bot.send_message(message.chat.id, message, parse_mode='html')
    else:
        bot.send_message(message.chat.id, f'Не корректная команда', parse_mode='html')


@bot.message_handler(content_types=['sticker'])
def get_user_sticker(message):
    bot.send_message(
        message.chat.id, f"А я смотрю, ты шутник <b>{message.from_user.first_name}</b>. "
                         f"Это же додуматься, боту стикер отправить. Гениально!",
        parse_mode='html')





bot.polling(non_stop=True)