# WeatherScrapy 🌦️

**WeatherScrapy** is a Python application that allows you to fetch and display weather data for selected cities in India. It uses web scraping to obtain weather information from Google search results, providing users with up-to-date weather details for their chosen location.

## Live Demo ▶️
https://youtu.be/uDze59XidRM

## Features 🌟

- User-friendly GUI built with **Tkinter**.
- Select a state and city from dropdown menus.
- Displays temperature, wind speed, and precipitation data.
- Error handling for network issues and unexpected errors.
- Easily adaptable to add more states and cities.

## Prerequisites 📋

Make sure you have the following Python libraries installed:

- BeautifulSoup (bs4) 📦
- Requests 📦
- Tkinter 📦

You can install these libraries using pip:

```bash
pip install beautifulsoup4 requests
```

## Usage 🚀

1. Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/WeatherScrapy.git
```

2. Run the application:

```bash
python forecastmain.py
```

3. Select a state and city, then click the "Fetch Weather" button.

4. The weather data will be displayed in the GUI window.

## State and City Data 🌍

The application provides a list of states and cities in India. You can customize the city data by updating the `cities` dictionary in the Python script to include additional cities for each state.

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
