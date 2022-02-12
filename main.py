import os

from urllib.parse import unquote, urlsplit

import requests


def download_file(new_file_path, url):
    new_file_name = os.path.split(unquote(urlsplit(url).path))[1]

    if os.path.exists(f'{new_file_path}/{new_file_name}'):
        return

    os.makedirs(new_file_path, exist_ok=True)

    response = requests.get(url)
    response.raise_for_status()

    with open(f'{new_file_path}/{new_file_name}', 'wb') as new_file:
        new_file.write(response.content)
