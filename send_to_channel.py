import argparse
import os
import random

from time import sleep
from contextlib import suppress

import telegram

from dotenv import load_dotenv


def send_random_photo(bot, channel_id):
    photo = random.choice(os.listdir('images'))
    with open(f'images/{photo}', 'rb') as photo:
        bot.send_photo(chat_id=channel_id, photo=photo)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=('App send one photo per day (or entered delay) '
                     'as a telegram-bot to telegram channel')
    )

    parser.add_argument(
        'delay',
        type=int,
        nargs='?',
        default=86400,
        help=('enter delay in seconds (default = 86400 sec.)')
    )
    args = parser.parse_args()

    load_dotenv()
    telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    channel_id = os.getenv('CHANNEL_ID')

    bot = telegram.Bot(token=telegram_bot_token)

    while True:
        with suppress(
            telegram.error.NetworkError,
            telegram.error.BadRequest,
            TypeError
        ):
            send_random_photo(bot, channel_id)
            sleep(args.delay)
