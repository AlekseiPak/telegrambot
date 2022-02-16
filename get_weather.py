import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()

def get_weather(city):

	API_key = os.environ.get('OPENWEATHER_API_KEY')

	url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"

	response = requests.get(url)
	print(response)
	dict_response = json.loads(response.text)
	weather = dict_response.get('weather')[0].get('description')
	degrees = dict_response.get('main').get('temp')
	return weather, degrees


