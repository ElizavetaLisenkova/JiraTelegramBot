import telebot
from telebot import types
import requests
import secret
telegram_token = secret.telegram_token
bot = telebot.TeleBot(telegram_token)
bot.remove_webhook()


import requests
from requests.auth import HTTPBasicAuth
import json

url = secret.testUrl
email = secret.email
testToken = secret.testToken

auth = HTTPBasicAuth( email, testToken)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))