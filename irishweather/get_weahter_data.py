""" Get the weather data from the national weather service"""

import requests
def get_weather_data():
    """ Get the weather data from the national weather service"""
    data_ext_path = "https://www.met.ie/Open_Data/json/National.json"
    # Curl data from the link and return the json object
    response = requests.get(data_ext_path, timeout=10)
    json_data = response.json()
    return json_data