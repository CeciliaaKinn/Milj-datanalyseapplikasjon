# API

import requests
import json


url = "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=51.5&lon=0"


response = requests.get(url)

if response.status_code == 200:
    print(response.json())  # Hvis API-et returnerer JSON-data
else:
    print(f"Feil: {response.status_code}")

##

# Bruke pandas data frame for å lage en tabell med data 



#test


