import streamlit as st
import requests

# Function to get weather data from OpenWeatherMap
def get_weather(city):
    api_key = "1946b06024c3c638abb63576ee063d11"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

# Title of the app
st.title("Simple Weather App")

# Input for city name
city = st.text_input("Enter city name")

if city:
    # Get weather data
    weather_data = get_weather(city)

    if weather_data.get("cod") != 200:
        st.error("City not found!")
    else:
        # Extract relevant information
        city_name = weather_data["name"]
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]

        # Display weather information
        st.subheader(f"Weather in {city_name}")
        st.write(f"Temperature: {temperature} °C")
        st.write(f"Description: {description.capitalize()}")

