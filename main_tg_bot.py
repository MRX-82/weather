import telebot
import logistic

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

@bot.message_handler()
def get_user_text(message):
    """
    This function open info in chat
    """
    if message.text == 'INFO':
        bot.send_message(message.chat.id, message, parse_mode='html')
    else:
        bot.send_message(message.chat.id, f'Не корректная команда', parse_mode='html')


bot.polling(non_stop=True)