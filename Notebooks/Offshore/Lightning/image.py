import requests

# Define the URL to get the image data
url = 'https://api.met.no/weatherapi/offshoremaps/1.0/helicopterlightningobservations?area=western_norway'

# Add the User-Agent header, which is required by the API
headers = {
    'User-Agent': 'Emelia Hult-Tjore - emeliah@stud.ntnu.no'
}

# Send GET request to the API
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Check if the content is an image (based on the content type header)
    content_type = response.headers['Content-Type']
    if 'image' in content_type:
        # Save the image content to a file (in this case, PNG)
        with open('helicopter_lightning_observation.png', 'wb') as f:
            f.write(response.content)
        print("Image saved as 'helicopter_lightning_observation.png'")
    else:
        print(f"Unexpected content type: {content_type}")
else:
    print(f"Error: {response.status_code}")
