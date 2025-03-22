import requests
import pandas as pd
## from collections import defaultdict # Helps sort the data in preferable order

class GetData:
    def __init__(self):
        """
        Initializes the GetData class with a fixed client ID.
        """
        self.client_id = 'b66cad58-f5a0-49b6-939e-df2b157a3ea4'
        self.endpoint = 'https://frost.met.no/observations/v0.jsonld'

    def _make_request(self, parameters):
        """
        Makes an HTTP GET request to the Frost API with the specified parameters.
        :param parameters: The parameters to pass to the API.
        :return: JSON data from the API response.
        """
        response = requests.get(self.endpoint, parameters, auth=(self.client_id, ''))
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error! Returned status code {response.status_code}")
            print(f"Message: {response.json()['error']['message']}")
            print(f"Reason: {response.json()['error']['reason']}")
            return None

    def get_json_data(self, elements, referencetime):
        """
        Retrieves data in JSON format from the API based on the given parameters.
        :param elements: List of elements to fetch, e.g., precipitation, temperature, etc.
        :param referencetime: Date range for the data (e.g., '2020-01-01/2020-12-31').
        :param timeoffsets: Time offset for the data (default is 'PT0H').
        :return: JSON data for the requested elements.
        """
        parameters = {
            'sources': 'SN18700',  # Example: Weather station on Ekofisk
            'elements': ','.join(elements),  # Combine the list of elements into a single string
            'referencetime': referencetime,  # Example: '2010-01-01/2010-12-31'
        }

        return self._make_request(parameters)

    def get_monthly_data_json(self, elements, referencetime):
        """
        Retrieves and processes data for the specified elements with monthly aggregation.
        Handles different time offsets and aggregation methods (mean or sum).
        :param elements: List of elements to fetch (e.g., 'mean(air_temperature P1M)', 'sum(precipitation P1M)', etc.)
        :param referencetime: Date range for the data (e.g., '2010-01-01/2010-12-31').
        :return: A DataFrame with monthly data for the specified elements.
        """
        data = self.get_json_data(elements, referencetime)
        
        # Dictionary to store the data, using the formatted date as the key
        monthly_data = {}

        if data:
            for item in data['data']:
                # Get formatted date (year-month)
                formatted_date = pd.to_datetime(item['referenceTime']).strftime('%Y-%m')

                # Initialize data structure for the specific month if not already present
                if formatted_date not in monthly_data:
                    monthly_data[formatted_date] = {}

                for observation in item['observations']:
                    # Check if the observation's elementId is in the requested elements
                    element_id = observation['elementId']
                    value = observation['value']
                    unit = observation['unit']

                    # Store the data based on the element type
                    if 'air_temperature' in element_id :  # Temperature
                        monthly_data[formatted_date]['Temp'] = value
                        if unit == 'degC':
                            monthly_data[formatted_date]['Unit_T'] = '°C'
                        else:
                            monthly_data[formatted_date]['Unit_T'] = unit

                    elif 'wind_speed' in element_id:  # Wind speed
                        monthly_data[formatted_date]['Wind'] = value
                        monthly_data[formatted_date]['Unit_W'] = unit

                    elif 'air_pressure' in element_id:  # Air pressure
                        monthly_data[formatted_date]['Pressure'] = value
                        monthly_data[formatted_date]['Unit_Pres'] = unit
                        
                    elif 'precipitation' in element_id:  # Precipitation
                        monthly_data[formatted_date]['Precipitation'] = value
                        monthly_data[formatted_date]['Unit_Precip'] = unit
                    
                    
            # Convert the dictionary to a DataFrame
            df = pd.DataFrame.from_dict(monthly_data, orient='index')

            # Reset the index to get a proper 'Date' column
            df.reset_index(inplace=True)
            df.rename(columns={'index': 'Date'}, inplace=True)

            return df

        return None

    def display_monthly_avg_json(self, elements, referencetime):
        """
        Displays the monthly averages or sums for the specified elements.
        :param elements: List of elements to fetch (e.g., 'mean(air_temperature P1M)', 'sum(precipitation P1M)', etc.)
        :param referencetime: Date range for the data (e.g., '2010-01-01/2010-12-31').
        :param timeoffsets: Time offset for the data (default is 'PT0H').
        :return: A DataFrame with monthly averages or sums for the specified elements.
        """
        df_monthly = self.get_monthly_data_json(elements, referencetime)
        if df_monthly is not None:
            print(df_monthly)
        else:
            print("No data found.")


    def get_csv_data(self, elements, referencetime):
        """
        Retrieves data in CSV format from the API and saves it to a file.
        :param elements: List of elements to fetch (e.g., 'mean(air_temperature P1M)', 'sum(precipitation P1M)', etc.)
        :param referencetime: Date range for the data (e.g., '2010-01-01/2010-12-31').
        :param timeoffsets: Time offset for the data (default is 'PT0H').
        :return: None. Saves the data to a CSV file.
        """
        data = self.get_json_data(elements, referencetime)
        
        if data:
            # Create a list to store the structured data for DataFrame conversion
            structured_data = []

            # Process the data and structure it as needed
            for item in data['data']:
                for observation in item['observations']:

                    # Check if the element is precipitation (which has a different aggregation)
                    if 'precipitation' in observation['elementId']:
                        timeOffset = 'PT6H'  # Measured every 6th hour
                    else:
                        timeOffset = 'TP0H'  # Measured once every day at 00:00

                    structured_data.append({
                        'Date': item['referenceTime'],
                        'Element': observation['elementId'],
                        'Value': observation['value'],
                        'Unit': observation['unit'],
                        'TimeOffset': timeOffset
                    })

            # Convert to DataFrame
            df = pd.DataFrame(structured_data)

            # Save to CSV
            df.to_csv('weather_data.csv', index=False)
            print("Data saved to 'weather_data.csv'")

    ## def get_monthly_data_cvs(self, elements, referencetime):
        """
        Retrieves and processes data for the specified elements with monthly aggregation.
        Handles different time offsets and aggregation methods (mean or sum).
        :param elements: List of elements to fetch (e.g., 'mean(air_temperature P1M)', 'sum(precipitation P1M)', etc.)
        :param referencetime: Date range for the data (e.g., '2010-01-01/2010-12-31').
        :return: A DataFrame with monthly data for the specified elements.
        """
        data = self.get_json_data(elements, referencetime)
        
        monthly_data = []

        if data:
            for item in data['data']:
                for observation in item['observations']:

                    # Check if the element is precipitation (which has a different aggregation)
                    if 'precipitation' in observation['elementId']:
                        aggregation_method = 'sum'  # Sum for precipitation
                        timeOffset = 'PT6H'  # Measured every 6th hour
                    else:
                        aggregation_method = 'mean'  # Mean for other elements
                        timeOffset = 'TP0H'  # Measured once every day at 00:00

                    monthly_data.append({
                        'Date': pd.to_datetime(item['referenceTime']).strftime('%Y-%m'), # Format: yyyy-mm ## For Jan, Feb,… use %b
                        'Element': observation['elementId'],
                        'Value': observation['value'],
                        'Aggregation': aggregation_method,
                        'Unit': observation['unit'],
                        'TimeOffset': timeOffset
                    })

            # Convert to DataFrame
            df = pd.DataFrame(monthly_data)

            # Reorder and return the DataFrame
            df = df[['Date', 'Element', 'Value', 'Aggregation', 'Unit', 'TimeOffset']]
            return df

        return None
    