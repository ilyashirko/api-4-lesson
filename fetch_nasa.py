import os

from urllib.parse import unquote, urlsplit

import requests

from dotenv import load_dotenv
from tqdm import tqdm

from files_processing import download_file, PHOTOS_PATH


def get_daily(token):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': token}

    response = requests.get(url, params=params)
    response.raise_for_status()
    daily_data = response.json()

    if isinstance(daily_data, dict):
        if daily_data['media_type'] == 'image':
            url = daily_data['url']
            _, photo_name = os.path.split(unquote(urlsplit(url).path))
            photo = f'{PHOTOS_PATH}/{photo_name}'
            if not os.path.exists(photo):
                download_file(photo, url)
    elif isinstance(daily_data, list):
        for content in tqdm(daily_data):
            if content['media_type'] == 'image':
                url = content['url']
                _, photo_name = os.path.split(unquote(urlsplit(url).path))
                photo = f'{PHOTOS_PATH}/{photo_name}'
                if not os.path.exists(photo):
                    download_file(photo, url)


def get_epic(token):
    url = 'https://epic.gsfc.nasa.gov/api/natural'
    params = {'api_key': token}

    latest_epic_info = requests.get(url, params=params)
    latest_epic_info.raise_for_status()

    for photo in tqdm(latest_epic_info.json()):
        date = '/'.join(photo['date'].split(' ')[0].split('-'))
        url = (f'https://epic.gsfc.nasa.gov/archive/natural/'
               f'{date}/png/{photo["image"]}.png')
        photo = f'{PHOTOS_PATH}/{photo["image"]}.png'
        if not os.path.exists(photo):
            download_file(photo, url)


if __name__ == '__main__':
    os.makedirs(PHOTOS_PATH, exist_ok=True)
    load_dotenv()
    token = os.getenv('NASA_TOKEN')

    try:
        get_daily(token)
    except requests.exceptions.HTTPError as error:
        print(f'ERROR!\n\n{error}')

    try:
        get_epic(token)
    except requests.exceptions.HTTPError as error:
        print(f'ERROR!\n\n{error}')
