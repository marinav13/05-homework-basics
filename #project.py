#project
#marina villeneuve

from dotenv import load_dotenv
import os
import requests

load_dotenv() #take environmental variables from .env

#print(os.getenv("PATH"))
BLS_key = os.getenv("BLS_key")

#url = f"https://api.bls.gov/publicAPI/v2/timeseries/data/?registrationkey={BLS_key}&catalog=true&startyear=2019&endyear=2022&calculations=true &annualaverage=true&aspects=true"
url = 'https://api.bls.gov/publicAPI/v2/timeseries/data/OEUMA53000000100001?startyear=2019&endyear=2022&registrationkey={BLS_key}'
print("URL is", url)
print(BLS_key)
print(os.getenv("BLS_key"))

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # Process the returned data as per your requirements
else:
    print('Request failed with status code:', response.status_code)

print(response.keys())
