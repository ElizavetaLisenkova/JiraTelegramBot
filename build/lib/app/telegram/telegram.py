import telebot
from telebot import types
# from .. import secret
from .. import jira
telegram_token = '6133746261:AAHpNiQ6uFQZlDJlWNsHmVKkL_US8tMYsfY'

api_token = telegram_token
bot = telebot.TeleBot(api_token)
bot.remove_webhook()

@bot.message_handler(commands=['start', 'restart'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("❓ Задать вопрос")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я бот для jira".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "👋 Поздороваться"):
        bot.send_message(message.chat.id, text=get_request())
    # elif(message.text == "❓ Задать вопрос"):
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     btn1 = types.KeyboardButton("Как меня зовут?")
    #     btn2 = types.KeyboardButton("Что я могу?")
    #     back = types.KeyboardButton("Вернуться в главное меню")
    #     markup.add(btn1, btn2, back)
    #     bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
    
    # elif(message.text == "Как меня зовут?"):
    #     bot.send_message(message.chat.id, "У меня нет имени..")
    
    # elif message.text == "Что я могу?":
    #     bot.send_message(message.chat.id, text="Поздороваться с читателями")
    
    # elif (message.text == "Вернуться в главное меню"):
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     button1 = types.KeyboardButton("👋 Поздороваться")
    #     button2 = types.KeyboardButton("❓ Задать вопрос")
    #     markup.add(button1, button2)
    #     bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    # else:
    #     bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")

bot.polling(none_stop=True)