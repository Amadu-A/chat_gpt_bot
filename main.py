import time

import telebot
import openai
from environs import Env


env = Env()
env.read_env()

BOT_TOKEN = env.str('BOT_TOKEN')
API_KEY = env.str('API_KEY')
ADMIN_ID = env.list('ADMIN_ID')
IP = env.str('IP')

bot = telebot.TeleBot(BOT_TOKEN)
openai.api_key = API_KEY


@bot.message_handler(content_types=['text'])
def handle_text(message):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=f'{message.text}',
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    bot.send_message(message.chat.id, response.choices[0].text)


bot.polling()

# if __name__ == '__main__':
#     while True:
#         try:
#             bot.polling(none_stop=True, interval=0)
#         except Exception as e:
#             time.sleep(10)