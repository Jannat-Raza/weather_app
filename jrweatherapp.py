import streamlit as st
import requests

# Function to get weather data from OpenWeatherMap
def get_weather(city):
    api_key = "e04fe1a3e129e8b3b0099eafd589fbdd"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()
st.markdown(
    """
    <style>
    .stApp {
        background-color: lightgray;
        color: brown;
    }
    .title {
        color: white;
    }
    .subtitle {
        color: white;
    }
    .weather-title {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the app
st.title("Weather App")

st.subheader("Get the current weather information for any city!")

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

