import requests

My_location_lat = 16.043859

My_location_lng = 120.335190



parameters = {
    "lat": My_location_lat,
    "lng": My_location_lng,
    "formatted":0
}

response = requests.get("https://api.sunrise-sunset.org/json?lat=16.043859&lng=120.335190", params=parameters)
response.raise_for_status()

data = response.json()
print(data)