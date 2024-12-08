
# Weather data 
weather_data = {
    "London": {"temp": "15°C", "condition": "Cloudy", "wind": "5 km/h", "humidity": "80%"},
    "New York": {"temp": "20°C", "condition": "Sunny", "wind": "10 km/h", "humidity": "50%"},
    "Tokyo": {"temp": "18°C", "condition": "Rainy", "wind": "7 km/h", "humidity": "90%"},
    "Sydney": {"temp": "22°C", "condition": "Windy", "wind": "15 km/h", "humidity": "60%"},
    "Paris": {"temp": "17°C", "condition": "Foggy", "wind": "3 km/h", "humidity": "85%"},
    "Berlin": {"temp": "12°C", "condition": "Partly Cloudy", "wind": "6 km/h", "humidity": "70%"},
    "Cape Town": {"temp": "25°C", "condition": "Clear", "wind": "20 km/h", "humidity": "45%"},
    "Los Angeles": {"temp": "28°C", "condition": "Sunny", "wind": "8 km/h", "humidity": "40%"},
    "Dubai": {"temp": "35°C", "condition": "Hot and Sunny", "wind": "5 km/h", "humidity": "30%"},
    "Moscow": {"temp": "-5°C", "condition": "Snowy", "wind": "12 km/h", "humidity": "85%"},
    "Denver": {"temp": "30°C", "condition": "Humid", "wind": "14 km/h", "humidity": "75%"},
    "Chicago": {"temp": "10°C", "condition": "Overcast", "wind": "9 km/h", "humidity": "80%"},
    "Walsall": {"temp": "32°C", "condition": "Thunderstorms", "wind": "25 km/h", "humidity": "95%"},
    "Torino": {"temp": "16°C", "condition": "Clear", "wind": "6 km/h", "humidity": "65%"},
    "Bacau": {"temp": "30°C", "condition": "Hot", "wind": "15 km/h", "humidity": "20%"}
}

#how to store json data in mysql
# Greet and visual design
print("Welcome to my weather app!")
print("-*-" * 12)
print("Available cities:", *weather_data.keys())
print("-*-" * 12)

# City input 
city_input = input("Enter the city name: ").lower()

# Check if the city is listed in weather_data
for city in weather_data:
    if city.lower() == city_input:
        print("\nWeather in " + city + ":")
        print("Temperature: " + weather_data[city]["temp"])
        print("Condition: " + weather_data[city]["condition"])
        print("Wind: " + weather_data[city]["wind"])
        print("Humidity: " + weather_data[city]["humidity"])
        break
else:
    print("The city you chose is not in the list. Please try again.")

print("\nThank you for using the app. Hope you enjoyed it!")
# a bit of design
print(" " * 5 + "*")
print(" " * 4 + "* *")
print(" " * 3 + "* * *")
print(" " * 2 + "* * * *")
print(" " * 1 + "* * * * *")
print("* * * * * *")
print(" " * 1 + "* * * * *")
print(" " * 2 + "* * * *")
print(" " * 3 + "* * *")
print(" " * 4 + "* *")
print(" " * 5 + "*")

