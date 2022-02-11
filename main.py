import os
import json

from urllib.parse import unquote, urlsplit

import requests


def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def download_file(new_file_path, url):
    new_file_name = os.path.split(unquote(urlsplit(url).path))[1]
    
    if os.path.exists(f'{new_file_path}/{new_file_name}'):
        return

    create_directory(new_file_path)

    response = requests.get(url)
    response.raise_for_status()

    with open(f'{new_file_path}/{new_file_name}', 'wb') as new_file:
        new_file.write(response.content)
    

def check_response(response):
    try:
        with open('check_response.json', 'w') as chk:
            json.dump(response.json(), chk, indent=4, ensure_ascii=False)
    except:
        with open('check_response.txt', 'w') as chk:
            chk.write(response.text)
