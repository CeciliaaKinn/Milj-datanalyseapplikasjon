import sys
import os

# Find the absolute path to the project root
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the src folder to sys.path
sys.path.append(os.path.join(project_root, 'src'))

# Now import GetData from GetData located in Utilities/Class
from Utilities.Class.GetData import GetData 

# Instantiate the GetData class
data_fetcher = GetData()

# Elements to retrieve (monthly mean temperature, wind speed, air pressure and monthly sum precipitation)
# Can use any number and combination of the four
elements = ['mean(air_temperature P1M)', 'mean(wind_speed P1M)', 'sum(precipitation_amount P1M)', 'mean(air_pressure_at_sea_level P1M)']

# Date range
referencetime = '2010-01-01/2010-12-31'  # Example

# Get the data in JSON format
json_data = data_fetcher.get_json_data(elements, referencetime)

## # Get the data in CSV format
## data_fetcher.get_csv_data(elements, referencetime)

# Display the monthly averages or sums for the requested elements

data_fetcher.display_monthly_avg_json(elements, referencetime)

