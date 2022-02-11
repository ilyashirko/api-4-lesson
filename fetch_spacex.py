import requests

from tqdm import tqdm

from main import download_file


def main():
    url = 'https://api.spacexdata.com/v3/launches/latest'

    response = requests.get(url)
    response.raise_for_status()

    for url in tqdm(response.json()['links']['flickr_images']):
        download_file(f'images/spacex/{response.json()["flight_number"]}', url)

if __name__ == '__main__':
    try:
        main()
    except requests.exceptions.HTTPError as error:
        print(f'ERROR!\n\n{error}')