import requests

from tqdm import tqdm

from files_processing import download_file


def get_latest_launch():
    url = 'https://api.spacexdata.com/v4/launches/latest'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()['flight_number']


def get_photos(launch_num):
    launch_url = f'https://api.spacexdata.com/v3/launches/{launch_num}'
    response = requests.get(launch_url)
    response.raise_for_status()
    for url in tqdm(response.json()['links']['flickr_images']):
        download_file('images/', url)


if __name__ == '__main__':
    latest_flight = get_latest_launch()
    for flight_num in range(1, latest_flight + 1):
        print(f'Checking {flight_num} flight...')
        try:
            get_photos(flight_num)
        except requests.exceptions.HTTPError as error:
            print(error)
