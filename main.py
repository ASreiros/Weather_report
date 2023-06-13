from datetime import datetime
import requests
import os
import telepot

try:
	weather_url = 'https://api.open-meteo.com/v1/forecast?latitude=55.66&longitude=21.16&daily=weathercode,temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,precipitation_hours,precipitation_probability_max,windspeed_10m_max,windgusts_10m_max&windspeed_unit=ms&forecast_days=1&timezone=Europe%2FLondon'

	w_response = requests.get(url=weather_url)
	w_response.raise_for_status()
	print(w_response.json())
	weather = w_response.json()

except Exception as e:
	print("weather request failed: ", e)
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
	print(max_temp)
	print(apparent_temp_max)
	print(min_temp)
	print(apparent_temp_min)
	print(rain_and_snow_probability)
	print(windspeed_max)
	print(windgust_max)

	weather_info = f"------{datetime.now().strftime('%Y-%m-%d')}---- \n"
	weather_info += f"Температура воздуха {max_temp}, ощущается как {apparent_temp_max} \n"
	weather_info += f"Ветер  {windspeed_max}м/с"
	if windgust_max - windgust_max > 2:
		weather_info += f", порывами до {windgust_max} м/с"
	weather_info += ". \n"
	weather_info += f"Шанс осадков {rain_and_snow_probability}%. \n"
	weather_info += "---------------------- \n"
	weather_info += f"Температура воздуха ночью {min_temp}, ощущается как {apparent_temp_min} \n"

	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	# chat = "-903822745"
	chat = "-972102355"
	url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={chat}&text={weather_info}"
	requests.get(url).json()



