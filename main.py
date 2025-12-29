import streamlit as st
import plotly.express as px
import os
import dotenv
import requests
import time


dotenv.load_dotenv()
api_key = os.getenv("LOC_API_KEY")

def get_weather_data(p="Bengaluru", d=1 ,op="relative_humidity_2m"):
    if p == "":
        p = "Bengaluru"
    if d == "":
        d = 1
    if op == "":
        op = "relative_humidity_2m"
    time.sleep(1)
    url = f"https://geocode.maps.co/search?q={p}&api_key={api_key}" # apikey was gathered from https://geocode.maps.co/
    location = requests.get(url)
    longitude = location.json()[0]["lon"]
    latitude = location.json()[0]["lat"]
    r = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly={op}&forecast_days={d}")
    st.success("weather data retrieved", icon="✅")
    dates = r.json()["hourly"]["time"]
    t = r.json()["hourly"][op]
    return dates, t

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days: ", min_value=1, max_value=5, value=1, help="Select the number of days to forecast")
option = st.selectbox("Select data to view",
                      ("temperature_2m", "relative_humidity_2m")) #additional attributes can be gathered from https://open-meteo.com/en/docs
st.subheader(f"{option} for the next {days} days in {place}")
date, temperatures = get_weather_data(place,days,option)
figure = px.line(x=date,y=temperatures,labels={'x':'Date','y':f'{option.title()}'})
st.plotly_chart(figure)







