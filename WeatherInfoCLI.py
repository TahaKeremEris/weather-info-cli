import argparse
import requests

# API URL and key information
API_URL = "http://api.openweathermap.org/data/2.5/weather"
API_KEY = "7d26b24f638f195666bda78c11578c7c"  # Your API key from OpenWeatherMap

def get_weather(city_name):
    """
    Fetches the weather information for the given city.
    """
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric',  # To get the temperature in Celsius
        'lang': 'en'        
    }

    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        data = response.json()

        # Extract the required information
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        return {
            'weather': weather,
            'temperature': temperature,
            'humidity': humidity,
            'wind_speed': wind_speed
        }
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the API request: {e}")
        return None

def main():
    """
    Accepts city name from the command line and displays weather information.
    """
    parser = argparse.ArgumentParser(description="Retrieve weather information for a city.")
    parser.add_argument('--city', type=str, required=True, help="Name of the city to fetch the weather information for.")
    args = parser.parse_args()

    city_name = args.city
    weather_info = get_weather(city_name)

    if weather_info:
        print(f"\nWeather information for {city_name}:")
        print(f"Weather: {weather_info['weather']}")
        print(f"Temperature: {weather_info['temperature']}°C")
        print(f"Humidity: {weather_info['humidity']}%")
        print(f"Wind Speed: {weather_info['wind_speed']} m/s\n")
    else:
        print("Unable to fetch weather information. Please try again.")

if __name__ == "__main__":
    main()
