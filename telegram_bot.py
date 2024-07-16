import json
import os

import telebot
import requests
from dotenv import load_dotenv

load_dotenv()
bot = telebot.TeleBot(os.getenv("TELEGRAM_BOT_KEY"))


@bot.message_handler(content_types=['text'])
def films(message):
    response = requests.get("http://127.0.0.1:8002/films/")
    if message.text == "/start":
        bot.send_message(message.from_user.id,
                         f"Greetings, {message.from_user.username}. Please send the command /films to get a list of films.")

    if message.text == "/films":
        try:
            data = response.json()
            json_data = json.dumps(data, indent=5, ensure_ascii=False)
            bot.send_message(message.from_user.id, f"{json_data}")
        except ValueError:
            bot.send_message(message.from_user.id, "data error")


bot.polling(none_stop=True, interval=0)
