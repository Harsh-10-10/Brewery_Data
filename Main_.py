import requests
import pandas as pd
import json


url = "https://api.openbrewerydb.org/v1/breweries"
params = {
    "per_page": 200,
    "page": 1
}

#Disabling SSL verification (not recommended for production)
response = requests.get(url, params=params, verify=False)

if response.status_code == 200:
    data = response.json()

    # Save JSON file
    with open("open_breweries.json", "w") as f:
        json.dump(data, f, indent=2)
    print("Data saved to open_breweries.json")

    # Normalize and save as CSV
    df = pd.json_normalize(data)

    df = df[[
        'id', 'name', 'brewery_type', 'street', 'city', 'state',
        'postal_code', 'country', 'longitude', 'latitude',
        'phone', 'website_url'
    ]]

    df.to_csv("open_breweries.csv", index=False)
    print("Data saved to open_breweries.csv")

elif response.status_code == 400:
    print("Bad Request")
else:
    print(f" Request failed with status code: {response.status_code}")

print("Status Code:", response.status_code)
