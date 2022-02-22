from dotenv import load_dotenv 
import os
import telebot
from valuta import valut

load_dotenv()
token = os.environ.get('VALUTE_TOKEN')
print(token)
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start (message):
	bot.send_message(message.chat.id,'Привет. Я бот валюты-Введите валюту!')

@bot.message_handler(content_types=['text'])
def show_valut (message):
	try:
		new_str = valut(message.text)
		bot.send_message(message.chat.id, 'Ваша валюта' + message.text + str(new_str))
	except TypeError:
		bot.send_message(message.chat.id,"ОШИБКА!!!Введите другую Валюту")
bot.polling()