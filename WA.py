import requests

# Step 1: Define API Key and Base URL
API_KEY = "d22e35c41797f6a48ea537a83162925c"  # Replace with your OpenWeatherMap API Key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Step 2: Get City Input from User
city = input("Enter the name of the city: ")

# Step 3: Build the API Request URL
params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"  # Use "imperial" for Fahrenheit
}

# Step 4: Make the API Request
response = requests.get(BASE_URL, params=params)

# Step 5: Parse the Response
if response.status_code == 200:
    data = response.json()
    
    # Extract weather details
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather_condition = data["weather"][0]["description"]

    # Display the weather information
    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {weather_condition}")
else:
    print("City not found. Please check the city name and try again.")
