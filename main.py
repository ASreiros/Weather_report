from datetime import datetime
import requests
import os
import telepot


flag = True
try:
	weather_url = 'https://api.open-meteo.com/v1/forecast?latitude=55.66&longitude=21.16&daily=weathercode,temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,precipitation_hours,precipitation_probability_max,windspeed_10m_max,windgusts_10m_max&windspeed_unit=ms&forecast_days=1&timezone=Europe%2FLondon'

	w_response = requests.get(url=weather_url)
	w_response.raise_for_status()
	print(w_response.json())
	weather = w_response.json()
	# weather = {'latitude': 55.663193, 'longitude': 21.15715, 'generationtime_ms': 1.2379884719848633, 'utc_offset_seconds': 3600, 'timezone': 'Europe/London', 'timezone_abbreviation': 'BST', 'elevation': 14.0, 'daily_units': {'time': 'iso8601', 'weathercode': 'wmo code', 'temperature_2m_max': '°C', 'temperature_2m_min': '°C', 'apparent_temperature_max': '°C', 'apparent_temperature_min': '°C', 'precipitation_hours': 'h', 'precipitation_probability_max': '%', 'windspeed_10m_max': 'm/s', 'windgusts_10m_max': 'm/s'}, 'daily': {'time': ['2023-06-14'], 'weathercode': [3], 'temperature_2m_max': [27.5], 'temperature_2m_min': [14.2], 'apparent_temperature_max': [25.8], 'apparent_temperature_min': [11.9], 'precipitation_hours': [0.0], 'precipitation_probability_max': [32], 'windspeed_10m_max': [5.0], 'windgusts_10m_max': [10.2]}}

except Exception as e:
	print("weather request failed: ", e)
	flag = False
else:
	weathercode = weather['daily']['weathercode'][0]
	max_temp = weather['daily']['temperature_2m_max'][0]
	apparent_temp_max = weather['daily']['apparent_temperature_max'][0]
	min_temp = weather['daily']['temperature_2m_min'][0]
	apparent_temp_min = weather['daily']['apparent_temperature_min'][0]
	rain_and_snow_probability = weather['daily']['precipitation_probability_max'][0]
	windspeed_max = weather['daily']['windspeed_10m_max'][0]
	windgust_max = weather['daily']['windgusts_10m_max'][0]

	print(weathercode)



	weather_info = f"------{datetime.now().strftime('%Y-%m-%d')}---- \n"
	if flag:
		weather_info += f"Температура воздуха {max_temp}, ощущается как {apparent_temp_max} \n"
		weather_info += f"Ветер  {windspeed_max}м/с"
		if windgust_max - windgust_max > 2:
			weather_info += f", порывами до {windgust_max} м/с"
		weather_info += ". \n"
		weather_info += f"Шанс осадков {rain_and_snow_probability}%. \n"
		weather_info += "---------------------- \n"
		weather_info += f"Температура воздуха ночью {min_temp}, ощущается как {apparent_temp_min} \n"
	else:
		weather_info = "Данных нет. Ошибка программы"

	weather_image = {
		"0": 'sunny.png',
		"1": 'overcast.png',
		"2": 'overcast.png',
		"3": 'overcast.png',
		'45': 'fog.png',
		'48': 'fog.png',
		'51': 'drizzle.png',
		'53': 'drizzle.png',
		'55': 'drizzle.png',
		'56': 'fdrizzle.png',
		'57': 'fdrizzle.png',
		'61': 'rain.png',
		'63': 'rain.png',
		'65': 'rain.png',
		'66': 'rain.png',
		'67': 'rain.png',
		'71': "snow.jpg",
		'73': "snow.jpg",
		'75': "snow.jpg",
		'77': "snow.jpg",
		'80': 'heavyrain.png',
		'81': 'heavyrain.png',
		'82': 'heavyrain.png',
		'85': "snow.jpg",
		'86': "snow.jpg",
		'95': "thunderstorm.jpg",
		'96': "thunderstorm.jpg",
		'99': "thunderstorm.jpg",
	}

	bot = telepot.Bot(os.environ.get("BOT_TOKEN"))
	chat = "-903822745"
	# chat = "-972102355"
	if str(weathercode) in weather_image:
		bot.sendPhoto(chat, photo=open(f'./img/{weather_image[str(weathercode)]}', 'rb'))
	else:
		bot.sendMessage(chat, weathercode)
	bot.sendMessage(chat, weather_info)




