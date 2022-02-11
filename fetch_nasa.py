import os

from datetime import datetime

import requests

from tqdm import tqdm
from dotenv import load_dotenv

from main import download_file


def get_daily(token):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': token}

    response = requests.get(url, params=params)
    response.raise_for_status()
    response = response.json()

    if isinstance(response, dict):
        if response['media_type'] == 'image':
            download_file(f'images/nasa/daily/{datetime.today().date()}', response['url'])
    elif isinstance(response, list):
        for content in response:
            if content['media_type'] == 'image':
                download_file(f'images', content['url'])


def get_epic(token):
    latest_epic_info = 'https://epic.gsfc.nasa.gov/api/natural'
    params = {'api_key': token}

    latest_epic_info = requests.get(latest_epic_info, params=params)
    latest_epic_info.raise_for_status()

    for photo in tqdm(latest_epic_info.json()):
        date = '/'.join(photo['date'].split(' ')[0].split('-'))
        url = f'https://epic.gsfc.nasa.gov/archive/natural/{date}/png/{photo["image"]}.png'
        download_file(f'images', url)


if __name__ == '__main__':
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
