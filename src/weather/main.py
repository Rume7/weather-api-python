import sys

def get_weather(city):
    # This is a mock function to simulate an API call
    # In a real app, you'd use the 'requests' library here
    data = {
        "London": "15°C and Cloudy",
        "New York": "22°C and Sunny",
        "Lisbon": "25°C and Clear"
        "Paris": "22°C and Cloudy"
    }
    return data.get(city, "Weather data not available for this city.")

def run():
    print("--- Weather API CLI ---")
    if len(sys.argv) < 2:
        print("Usage: weather-check <city_name>")
    else:
        city = sys.argv[1]
        result = get_weather(city)
        print(f"City: {city}")
        print(f"Result: {result}")

if __name__ == "__main__":
    run()
