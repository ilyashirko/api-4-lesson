import argparse
import os

from random import randint
from time import sleep

import telegram

from dotenv import load_dotenv


def send_random_photo(bot, channel_id):
    photos = os.listdir('images')
    photo = photos[randint(0, len(photos)-1)]
    with open(f'images/{photo}', 'rb') as photo:
        bot.send_photo(chat_id=channel_id, photo=photo)
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='App send one photo per day (or entered delay) as a telegram-bot to telegram channel')
    parser.add_argument('delay', type=int, nargs='?', default=86400, help=('enter delay in seconds (default = 86400 sec.)'))
    args = parser.parse_args()

    load_dotenv()
    telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    channel_id=os.getenv('CHANNEL_ID')

    bot = telegram.Bot(token=telegram_bot_token)

    while True:
        try:
            send_random_photo(bot, channel_id)
            sleep(args.delay)
        except telegram.error as error:
            print(error)
        except TypeError:  # if user put in 'images' non-photo file
            pass
    