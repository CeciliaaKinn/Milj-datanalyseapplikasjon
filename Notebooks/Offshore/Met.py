import requests


import requests

# Define the API endpoint and parameters
url = "https://api.met.no/weatherapi/lightning/1.0/"
params = {
    'lat': 60.472,
    'lon': 8.536,
    'start': '2025-03-01T00:00:00',
    'end': '2025-03-06T00:00:00'
}


# Send GET request with the User-Agent header
headers = {
    "User-Agent": "Emelia Hult-Tjore/1.0 (emeliah@stud.ntnu.no)"
}

response = requests.get(url, params=params, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Data retrieved successfully!")
    # Process your response here
    data = response.json()  # Assuming the response is in JSON format
    print(data)
else:
    print(f"Error: {response.status_code}")
    print(response.text)



