# API, Data Frame, JSON-fil, CSV, Matplotlib

import requests
import json

#Json-fil

url = 'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=51.5&lon=0'

# Legg til en User-Agent header, som kreves av API-et
headers = {
    'User-Agent': 'Emelia Hult-Tjore - emeliah@stud.ntnu.no'
}
response = requests.get(url, headers=headers)


if response.status_code == 200:
    print(response.json())  # Hvis API-et returnerer JSON-data
    print(type(response))


else:
    print(f"Feil: {response.status_code}")


# Bruke pandas data frame for å lage en tabell med data 

import pandas as pd 

dictr = response.json()

print(dictr)

df = pd.DataFrame(dictr)
print(df)       



import matplotlib.pyplot as plt

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Retrieve the JSON data from the response
    data = response.json()
    
    # Check the structure of the JSON data
    print("Full data from the API:")
    print(data)  # This will print the whole JSON response
    
    # Extract relevant information (timeseries data)
    if 'properties' in data and 'timeseries' in data['properties']:
        timeseries = data['properties']['timeseries']
        
        # Prepare data for DataFrame: Extract time and temperature
        timestamps = []
        temperatures = []
        locations = []
        for entry in timeseries:
            timestamps.append(entry['time'])
            temperature = entry['data']['instant']['details']['air_temperature']
            temperatures.append(temperature)
            locations.append(entry['lat'])

        
        # Create a DataFrame with the extracted data
        df = pd.DataFrame({
            'Time': pd.to_datetime(timestamps),
            'Temperature (°C)': temperatures,
            'Latitude' : locations
        })
        
        # Print the DataFrame
        print("\nData in DataFrame:")
        print(df.head())  # Show the first few rows of the DataFrame
        
        # Visualize the temperature data over time
        plt.figure(figsize=(10, 6))
        plt.plot(df['Time'], df['Temperature (°C)'], marker='o', color='b', label='Temperature')
        plt.title('Temperature', fontsize=14)
        plt.xlabel('Time', fontsize=12)
        plt.ylabel('Temperature (°C)', fontsize=12)
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()

    else:
        print("Error: 'timeseries' data not found in the response.")
else:
    print(f"Error: {response.status_code}")


# Calculate average temp, median etc. 
# Plotte linjediagram, stolpediagram etc. 


#CSV file





