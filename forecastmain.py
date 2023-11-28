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
        
        # Find the temperature element by attribute
        temperature_element = soup.find('span', {'data-c': True, 'data-f': True})

        # Extract only the numeric value from the temperature element
        temperature = temperature_element.find('span', {'jsname': 'wcyxJ'}).text if temperature_element else "N/A"

        # Find the precipitation element
        precipitation_parent_div = soup.find('div', class_='mPUmSe')
        precipitation_elements = precipitation_parent_div.find_all('span', {'aria-hidden': 'true'})

        # Check if the second span exists and get its text
        precipitation = precipitation_elements[1].text if len(precipitation_elements) > 1 else "N/A"

        # Find the wind speed element by attribute
        wind_speed_element = soup.find('div', {'data-c': True, 'data-f': True, 'jsaction': 'rcuQ6b:npT2md', 'jscontroller': 'ZWq8q'})
        wind_speed = wind_speed_element.text if wind_speed_element else "N/A"

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
root.configure(bg="#E0E3E2")

# Load and display an image
image_path = "weather.png"  # Change this to the actual path of your image file
try:
    original_image = tk.PhotoImage(file=image_path)

    # Calculate the new width and height for resizing to 20%
    new_width = int(original_image.width() * 0.2)
    new_height = int(original_image.height() * 0.2)

    # Resize the image
    resized_image = original_image.subsample(5, 5)  # Adjust the values to achieve 20% size

    weather_image_label = tk.Label(root, image=resized_image, background="#E0E3E2")
    weather_image_label.grid(row=0, column=0, pady=10 )
except tk.TclError:
    print("Image file not found or not in a supported format!")


# Add a heading at the top
heading_label = ttk.Label(root, text="Weather Data Web Scraper", font=("Arial", 16, "bold"), background="#E0E3E2")
heading_label.grid(row=0, column=1,columnspan=2, pady=10)



# Create and configure the state and city dropdown menus
states = [
    "Andaman and Nicobar Islands",
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chandigarh",
    "Chhattisgarh",
    "Dadra and Nagar Haveli and Daman and Diu",
    "Delhi",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Ladakh",
    "Lakshadweep",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Puducherry",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal",
]
state_var = tk.StringVar()
state_var.set(states[0])
state_label = ttk.Label(root, text="Select State:", background="#E0E3E2")
state_label.grid(row=2, column=0, pady=(0, 5))
state_menu = ttk.Combobox(root, textvariable=state_var, values=states)
state_menu.grid(row=2, column=1, pady=(0, 5))

# A dictionary of cities for each state
cities = {
    "Andaman and Nicobar Islands": ["Port Blair"],
    "Andhra Pradesh": ["Visakhapatnam", "Vijayawada", "Tirupati"],
    "Arunachal Pradesh": ["Itanagar", "Tawang", "Naharlagun"],
    "Assam": ["Guwahati", "Silchar", "Dibrugarh"],
    "Bihar": ["Patna", "Gaya", "Bhagalpur"],
    "Chandigarh": ["Chandigarh"],
    "Chhattisgarh": ["Raipur", "Bhilai", "Bilaspur"],
    "Dadra and Nagar Haveli and Daman and Diu": ["Daman", "Diu", "Dadra"],
    "Delhi": ["New Delhi", "Gurgaon", "Noida"],
    "Goa": ["Panaji", "Vasco da Gama", "Margao"],
    "Gujarat": ["Ahmedabad", "Surat", "Vadodara"],
    "Haryana": ["Chandigarh", "Faridabad", "Gurgaon"],
    "Himachal Pradesh": ["Shimla", "Manali", "Dharamshala"],
    "Jharkhand": ["Ranchi", "Jamshedpur", "Dhanbad"],
    "Karnataka": ["Bengaluru", "Mysuru", "Hubli"],
    "Kerala": ["Thiruvananthapuram", "Kochi", "Kozhikode"],
    "Ladakh": ["Leh", "Kargil"],
    "Lakshadweep": ["Kavaratti", "Agatti", "Andrott"],
    "Madhya Pradesh": ["Bhopal", "Indore", "Jabalpur"],
    "Maharashtra": ["Mumbai", "Pune", "Nagpur"],
    "Manipur": ["Imphal", "Thoubal", "Bishnupur"],
    "Meghalaya": ["Shillong", "Tura", "Jowai"],
    "Mizoram": ["Aizawl", "Lunglei", "Saiha"],
    "Nagaland": ["Kohima", "Dimapur", "Mokokchung"],
    "Odisha": ["Bhubaneswar", "Cuttack", "Rourkela"],
    "Puducherry": ["Puducherry", "Karaikal", "Yanam"],
    "Punjab": ["Chandigarh", "Ludhiana", "Amritsar"],
    "Rajasthan": ["Jaipur", "Udaipur", "Jodhpur"],
    "Sikkim": ["Gangtok", "Namchi", "Mangan"],
    "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai"],
    "Telangana": ["Hyderabad", "Warangal", "Nizamabad"],
    "Tripura": ["Agartala", "Udaipur", "Dharmanagar"],
    "Uttar Pradesh": ["Lucknow", "Kanpur", "Agra"],
    "Uttarakhand": ["Dehradun", "Haridwar", "Rishikesh"],
    "West Bengal": ["Kolkata", "Howrah", "Durgapur"],
}


# Initialize the city variable with the first city of the selected state
initial_state = states[0]
cities_for_state = cities.get(initial_state, [])
city_var = tk.StringVar()
city_var.set(cities_for_state[0] if cities_for_state else "")
city_label = ttk.Label(root, text="Select City:" , background="#E0E3E2")
city_label.grid(row=3, column=0, pady=(0, 5))
city_menu = ttk.Combobox(root, textvariable=city_var, values=cities_for_state)
city_menu.grid(row=3, column=1, pady=(0, 5))

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
fetch_button.grid(row=4, columnspan=2, pady=10, padx=10)


# Create a custom button style
button_style = ttk.Style()
button_style.configure("Custom.TButton", font=("Arial", 11),
                       border_width=0,
                       corner_radius=8,
                       padding=5)



# Create a text widget to display the weather data
result_text = tk.Text(root, height=8, width=53, font=("Arial", 15), state="disabled")
result_text.grid(row=5, columnspan=2, padx=5, pady=10, sticky="nsew")

# Start the GUI application
root.mainloop()

