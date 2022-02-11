made by [@IlyaShirko](https://github.com/ilyashirko/)  

# send SpaseX & NASA photos to telegram channel
This programm fetch and send photos to telegram channel via telegram bot at the specified frequency.

## install app
1. clone repository and go to the root folder:
```
$ git clone https://github.com/ilyashirko/api-4-lesson
$ cd api-4-lesson
```
2. activate virtual environment via venv or virtualenv, activate it:
```
$ python3 -m venv env
$ source /env/bin/activate
```
3. install dependencies using pip or pip3:
```
pip3 install -r requirements.txt
```
4. get [NASA token](https://api.nasa.gov/) for downloading photos. It looks like `234251245ji1h245hg24h5b12j4h5b12hj45bj12h`
6. create [telegram bot](https://t.me/BotFather), you will take special token for your bot. It looks like `78686876876:9sd8f7sd98sd7f98sd7f9s8d7f987s9d8f7`.
7. create [telegram channel](https://web.telegram.org/k/), you will need its ID.
8. create file `.env` in root folder of programm and write you tokens and ID there:
```
NASA_TOKEN=234251245ji1h245hg24h5b12j4h5b12hj45bj12h
TELEGRAM_BOT_TOKEN=78686876876:9sd8f7sd98sd7f98sd7f9s8d7f987s9d8f7
CHANNEL_ID=YOUR_CHANNEL_ID
```

## launch app
there is 2 scripts for downloading photos, you can run it in tern:
```
$ python3 fetch_nasa.py
$ python3 fetch_spacex.py
```
**fetch_nasa.py** collect last daily photo and last epic photos.  
**fetch_spacex.py** collect all available photos from all SpaceX launches.  
All photos, you'd already downloaded, won't be downloaded again.

to run telegram bot:
```
python3 send_to_channel.py delay
```
*delay* should be a natural number which tell programm delay (in seconds) between photos send.  
you can dont write delay, in this case it will be default - 86400 (one day)
