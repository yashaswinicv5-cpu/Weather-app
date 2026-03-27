import requests
import json

API_KEY = "e64b56c4b70ae19c69c84bc5f06a6b43"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            weather_info = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"]
            }
            return weather_info
        else:
            return {"error": data.get("message", "Unable to fetch data")}
    except Exception as e:
        return {"error": str(e)}

def main():
    cities = input("Enter city names separated by commas: ").split(",")
    results = []
    
    for city in cities:
        city = city.strip()
        weather = get_weather(city)
        results.append(weather)
        if "error" not in weather:
            print(f"\nCity: {weather['city']}")
            print(f"Temperature: {weather['temperature']}°C")
            print(f"Weather: {weather['description']}")
            print(f"Humidity: {weather['humidity']}%")
            print(f"Wind Speed: {weather['wind_speed']} m/s")
        else:
            print(f"\nError fetching {city}: {weather['error']}")
    
    # Save results to file
    with open("weather_results.json", "w") as f:
        json.dump(results, f, indent=4)

if __name__ == "__main__":
    main()