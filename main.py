from bs4 import BeautifulSoup
import requests
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re

# Function to fetch weather data for the selected city and display it in a GUI window
def fetch_weather():
    # Get the selected state and city from the dropdown menus
    selected_state = state_var.get()
    selected_city = city_var.get()

    # Check if a city is selected
    if selected_city == "":
        messagebox.showerror("Error", "Please select a city.")
        return

    # URL for weather data
    url = f"https://www.google.com/search?q=weather+{selected_state}+{selected_city}"

    try:
        # Send a request to the website
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36'})
        page.raise_for_status()

        # Parse the page content
        soup = BeautifulSoup(page.content, 'html.parser')
        
        # Inside the fetch_weather function, when displaying text:
        print(soup.prettify().encode('utf-8').decode('utf-8', 'ignore'))

        # Find the temperature element by ID
        temperature_element = soup.find('span', id='wob_tm')

        # Find the wind speed element by ID
        wind_speed_element = soup.find("span", id="wob_ws")

        # Find the precipitation element by ID
        precipitation_element = soup.find("span", id="wob_pp")

        # Check if the elements exist
        if temperature_element and wind_speed_element and precipitation_element:
            temperature = temperature_element.text
            wind_speed = wind_speed_element.text
            precipitation = precipitation_element.text
        else:
            temperature = "N/A"
            wind_speed = "N/A"
            precipitation = "N/A"

        # Display the weather data in the GUI
        result_text.config(state="normal")
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Temperature: {temperature}°C\nWind Speed: {wind_speed}\nPrecipitation: {precipitation}")
        result_text.config(state="disabled")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", "Failed to fetch weather data. Check your internet connection.")
    except Exception as e:
        messagebox.showerror("Error", "An error occurred while fetching weather data.")
        print(e)


# Create the main application window
root = tk.Tk()
root.title("WeatherScrapy")
root.geometry("600x400")

# Create and configure the state and city dropdown menus
states = ["Assam", "Arunachal Pradesh", "Andhra Pradesh", "Agra", "Ahmedabad", "Amritsar", "Bengaluru", "Bhopal", "Bhubaneswar", "Chandigarh", "Chennai", "Coimbatore", "Dehradun", "Delhi", "Faridabad", "Gandhinagar", "Ghaziabad", "Gurugram", "Guwahati", "Hyderabad", "Imphal", "Indore", "Itanagar", "Jaipur", "Kolkata", "Lucknow", "Mumbai", "Nagpur", "Noida", "Panaji", "Patna", "Pune", "Raipur", "Ranchi", "Shillong", "Shimla", "Srinagar", "Thiruvananthapuram"]
state_var = tk.StringVar()
state_var.set(states[0])
state_label = ttk.Label(root, text="Select State:")
state_label.grid(row=0, column=0)
state_menu = ttk.Combobox(root, textvariable=state_var, values=states)
state_menu.grid(row=0, column=1)

# A dictionary of cities for each state
cities = {
    "Andaman and Nicobar Islands": ["Port Blair"],
    "Andhra Pradesh": ["Visakhapatnam", "Vijayawada", "Tirupati"],
    "Arunachal Pradesh": ["Itanagar", "Tawang", "Naharlagun"],
    "Assam": ["Guwahati", "Silchar", "Dibrugarh"],
    # ... (other states and cities)
}

# Initialize the city variable with the first city of the selected state
initial_state = states[0]
cities_for_state = cities.get(initial_state, [])
city_var = tk.StringVar()
city_var.set(cities_for_state[0] if cities_for_state else "")
city_label = ttk.Label(root, text="Select City:")
city_label.grid(row=1, column=0)
city_menu = ttk.Combobox(root, textvariable=city_var, values=cities_for_state)
city_menu.grid(row=1, column=1)

# Function to update the city dropdown based on the selected state
def update_city_dropdown(event):
    selected_state = state_var.get()
    cities_for_state = cities.get(selected_state, [])
    city_menu['values'] = cities_for_state
    city_var.set(cities_for_state[0] if cities_for_state else "")

# Bind the state menu selection event to the city dropdown update function
state_menu.bind("<<ComboboxSelected>>", update_city_dropdown)

# Create a button to fetch weather data
fetch_button = ttk.Button(root, text="Fetch Weather", command=fetch_weather,
                          style="Custom.TButton")
fetch_button.grid(row=2, columnspan=2)

# Create a custom button style
button_style = ttk.Style()
button_style.configure("Custom.TButton", font=("Arial", 10, "bold"),
                       background="blue",
                       borderwidth=2,
                       padding=7)

# Create a text widget to display the weather data
result_text = tk.Text(root, height=15, width=70, font=("Arial", 10), state="disabled")
result_text.grid(row=3, columnspan=2, padx=10, pady=10)

# Start the GUI application
root.mainloop()
