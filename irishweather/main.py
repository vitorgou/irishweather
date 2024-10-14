""" Main function"""

from get_weahter_data import get_weather_data

if __name__ == "__main__":
    full_json = get_weather_data()
    print(full_json)