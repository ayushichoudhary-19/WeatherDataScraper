# 🌦️ WeatherScrapy 

Welcome to WeatherScrapy! 
**WeatherScrapy** is a Python application that allows you to fetch and display weather data for selected cities in India. It uses web scraping to obtain weather information from Google search results, providing users with up-to-date weather details for their chosen location.

# 📦 Technologies

- **Python**: The core programming language.
- **Tkinter**: Used for creating the GUI (Graphical User Interface).
- **Beautiful Soup**: A library for pulling data from HTML and XML files.
- **Requests**: A library for making HTTP requests.
- **Google Search**: Utilized for fetching weather data through web scraping.
  
# 🍿 Video
https://www.youtube.com/watch?v=uDze59XidRM

# 🦄 Features

- User-friendly GUI built with **Tkinter**.
  Select a state and city from dropdown menus.
- Dropdown menus **dynamically update** based on the selected state.
- Displays real-time weather data including temperature, wind speed, and precipitation.
- **Error handling** for internet connection issues and other exceptions.
- Easily adaptable to add more states and cities.

# 🚦 Running the Project

1. Make sure you have Python installed on your system.
   If not, install it from: [Python Official Website](https://www.python.org/downloads/)

2. Clone the repository to your local machine:
  ```bash
  git clone https://github.com/yourusername/WeatherScrapy.git
  ```

3. Install the required libraries
     - BeautifulSoup (bs4) 📦
     - Requests 📦
   ```
   pip install beautifulsoup4 requests
   ```
   
4. Run the ` forecastmain.py` file using the command:
   ```
   python forecastmain.py
   ```
   
5. Select a state and city, then click the "Fetch Weather" button.

6. The weather data will be displayed in the GUI window.

# 📚 What I Learned

- Implementing a web scraper using Beautiful Soup and Requests.
- Creating a GUI application with Tkinter.
- Handling exceptions and displaying error messages.
- Dynamically updating dropdown menus based on user input.

# 📈 Overall Growth

This project helped me enhance my skills in web scraping, GUI development, error handling, and Python overall. It provided a practical application of Python in retrieving real-time data from the web and presenting it in a user-friendly interface.

# 💭 How can it be improved?

1. **Enhanced GUI**: Improve the GUI design for a more visually appealing interface.
2. **API Integration**: Consider using a weather API for more reliable and structured data.

## State and City Data 🌍

The application provides a list of states and cities in India. You can customize the city data by updating the `cities` dictionary in the Python script to include additional cities for each state.

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
