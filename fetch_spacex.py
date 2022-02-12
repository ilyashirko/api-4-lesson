import os

from urllib.parse import unquote, urlsplit
from contextlib import suppress

import requests

from tqdm import tqdm

from files_processing import download_file, PHOTOS_PATH


def get_launches():
    url = 'https://api.spacexdata.com/v4/launches'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


if __name__ == '__main__':
    os.makedirs(PHOTOS_PATH, exist_ok=True)
    launches = get_launches()
    for launch in launches:
        with suppress(KeyError):
            for url in tqdm(launch['links']['flickr']['original']):
                _, photo_name = os.path.split(unquote(urlsplit(url).path))
                photo = f'{PHOTOS_PATH}/{photo_name}'
                if not os.path.exists(photo):
                    download_file(photo, url)
