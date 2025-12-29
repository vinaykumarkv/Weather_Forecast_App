# Weather Forecast App
A simple web application that retrieves and visualizes weather data for a specified location over a selected number of days.

## Features

- Retrieve forecast data via Open-Meteo API for temperature or relative humidity.
- Allow user input for location, forecast duration (1-5 days), and data type to display.
- Display a line chart using Plotly Express to show the time series of weather conditions.
- Use Streamlit for easy web development with a simple, intuitive interface.

## Setup

1. Install required Python packages:
   - streamlit
   - plotly
   - requests
   - dotenv (for loading API key from environment variable)

2. Obtain an API key from [geocode.maps.co](https://geocode.maps.co/). Store it as `LOC_API_KEY` in your local `.env` file.

3. Run the app using `streamlit run main.py`

4. Open a web browser and navigate to `http://localhost:8501` to interact with the application.

## Usage

1. Enter a location in the "Place" text field.
2. Adjust the number of forecast days using the slider.
3. Select the data type (temperature or relative humidity) from the dropdown menu.
4. The app will retrieve and display the corresponding weather data for the specified duration, updating the chart accordingly.

*There is scope of adding lot of other features but I have tp proceed and focus on other important projects*