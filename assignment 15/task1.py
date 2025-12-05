import requests
import json
import sys
import time

# --- OpenWeatherMap API Connector ---

def get_weather_data(city_name, api_key):
    """
    Retrieves and displays current weather data for a given city from the
    OpenWeatherMap API.

    NOTE: This function intentionally lacks robust error handling as requested,
    meaning it will fail gracefully if the city is not found, the API key is
    invalid, or there are network issues.

    Args:
        city_name (str): The name of the city to query.
        api_key (str): Your personal OpenWeatherMap API key.
    """
    # Base URL for the current weather data API
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Construct the full API call URL
    complete_url = f"{base_url}appid={api_key}&q={city_name}&units=metric"

    print(f"\n-> Attempting to fetch data for: {city_name}...")

    # Send the GET request to the API endpoint
    response = requests.get(complete_url)

    # Convert the response to a Python dictionary
    data = response.json()

    # --- Displaying the Output ---

    # Pretty-print the JSON response. 
    # The 'indent=4' parameter formats the JSON with 4 spaces for readability.
    print("\n--- Raw API Response (Formatted JSON) ---")
    pretty_json_output = json.dumps(data, indent=4)
    print(pretty_json_output)
    print("----------------------------------------\n")


# --- Main Execution Block ---

# IMPORTANT: Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key.
API_KEY = "YOUR_API_KEY"

# Ensure the user has updated the placeholder key
if API_KEY == "YOUR_API_KEY":
    print("--- Setup Error ---")
    print("Please replace 'YOUR_API_KEY' in the script with your actual API key from OpenWeatherMap.")
    print("The program cannot proceed without a valid key.")
    sys.exit(1)

# Ask the user for the city name
try:
    city = input("Enter city name (e.g., London, Tokyo, Paris): ")
    if not city.strip():
        print("City name cannot be empty. Exiting.")
        sys.exit(0)

    # Call the function to retrieve and display the weather data
    get_weather_data(city, API_KEY)

except KeyboardInterrupt:
    print("\n\nOperation interrupted by the user. Exiting.")
except Exception as e:
    # A catch-all for unexpected issues, though we are not implementing robust error handling
    print(f"\nAn unexpected error occurred: {e}")