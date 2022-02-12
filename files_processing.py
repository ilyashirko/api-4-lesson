import os

from urllib.parse import unquote, urlsplit

import requests


def download_file(file_path, url):
    file_name = os.path.split(unquote(urlsplit(url).path))[1]

    if os.path.exists(f'{file_path}/{file_name}'):
        return

    os.makedirs(file_path, exist_ok=True)

    response = requests.get(url)
    response.raise_for_status()

    with open(f'{file_path}/{file_name}', 'wb') as new_file:
        new_file.write(response.content)
