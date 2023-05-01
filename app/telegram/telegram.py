import telebot
from .. import secret


api_token = secret.telegram_token
bot = telebot.TeleBot(api_token)
bot.remove_webhook()

@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, text=f"{message.text}")






bot.polling(none_stop=True)