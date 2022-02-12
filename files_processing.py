import requests

PHOTOS_PATH = 'images'


def download_file(path, url):
    response = requests.get(url)
    response.raise_for_status()
    with open(path, 'wb') as new_file:
        new_file.write(response.content)
