from datetime import datetime
import requests

try:
	weather_url = 'https://api.open-meteo.com/v1/forecast?latitude=55.66&longitude=21.16&daily=weathercode,temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,precipitation_hours,precipitation_probability_max,windspeed_10m_max,windgusts_10m_max&windspeed_unit=ms&forecast_days=1&timezone=Europe%2FLondon'

	w_response = requests.get(url=weather_url)
	w_response.raise_for_status()
	print(w_response.json())
	weather = w_response.json()

except Exception as e:
	print("weather request failed: ", e)
else:
	max_temp = weather['daily']['temperature_2m_max'][0]
	apparent_temp_max = weather['daily']['apparent_temperature_max'][0]
	min_temp = weather['daily']['temperature_2m_min'][0]
	apparent_temp_min = weather['daily']['temperature_2m_min'][0]
	rain_and_snow_probability = weather['daily']['precipitation_probability_max'][0]
	windspeed_max = weather['daily']['windspeed_10m_max'][0]
	windgust_max = weather['daily']['windgusts_10m_max'][0]

	print(max_temp)
	print(apparent_temp_max)
	print(min_temp)
	print(apparent_temp_min)
	print(rain_and_snow_probability)
	print(windspeed_max)
	print(windgust_max)


