from question1 import get_city_weather

def get_city_weather(city):
  temperature = get_city_temperature(city)
  if temperature is not None:
    sky_condition = None
    if city == "Sao Paulo":
      sky_condition = "cloudy"
    elif city == "New York":
      sky_condition = "rainy"
    
    return f"{temperature} degrees and {sky_condition}" if sky_condition is not None else f"{temperature} degrees"
  else:
    return "City not found"  # Or handle the error accordingly.
