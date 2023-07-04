#project
#marina villeneuve

from dotenv import load_dotenv
import os
import requests
#import json
import matplotlib.pyplot as plt

load_dotenv() #take environmental variables from .env

#print(os.getenv("PATH"))
BLS_key = os.getenv("BLS_key")

#url = f"https://api.bls.gov/publicAPI/v2/timeseries/data/?registrationkey={BLS_key}&catalog=true&startyear=2019&endyear=2022&calculations=true &annualaverage=true&aspects=true"
#url = f"https://api.bls.gov/publicAPI/v2/timeseries/data?registrationkey={BLS_key}&catalog=true&startyear=2019&endyear=2022&calculations=true&annualaverage=true&aspects=true"
#url = f"https://api.bls.gov/publicAPI/v2/timeseries/data?registrationkey={BLS_key}&catalog=true&startyear=2019&endyear=2022&calculations=true&annualaverage=true&aspects=true"

private_url = f'https://api.bls.gov/publicAPI/v2/timeseries/data/SMU25000000500000001?startyear=2019&endyear=2022&registrationkey={BLS_key}'

#url = 'https://api.bls.gov/publicAPI/v2/timeseries/data/OEUMA53000000100001?startyear=2019&endyear=2022&registrationkey={BLS_key}'
#print("URL is", url)
#print(BLS_key)
#print(os.getenv("BLS_key"))

response = requests.get(private_url)
data = response.json()
#data.keys()
#print(data)
#print(list(data.values()))

# if response.status_code == 200:
     #data = response.json()
series_data = data['Results']['series'][0]['data']
#Process the returned data as per your requirements
months = []
employment = []
job_may_19 = 0
job_may_23 = 0

for data_point in series_data:
    year = int(data_point['year'])
    period = data_point['period']
    job = float(data_point['value'])
    months.append(year + int(period[1:])/12)  # Combine year and month as a decimal for x-axis
    employment.append(job)

    if period == 'M05' and year == 2019:
        print(f"Private Jobs in May 2019: {job}")
        job_may_19 = job
    elif period == 'M05' and year == 2023:
        print(f"Private Jobs in May 2023: {job}")
        job_may_23 = job

# plt.plot(months, employment)
# plt.xlabel('Year and Month')
# plt.ylabel('Jobs in thousands')
# plt.title('Private Sector Jobs in Massachusetts by Month')
# plt.show()
# else:
#      print('Request failed with status code:', response.status_code)


public_url = f'https://api.bls.gov/publicAPI/v2/timeseries/data/SMU25000009092000001?startyear=2019&endyear=2022&registrationkey={BLS_key}'
response = requests.get(public_url)
data = response.json()
public_data = data['Results']['series'][0]['data']

public_months = []
public_jobs = []
public_job_may_19 = 0
public_job_may_23 = 0

for data_point in public_data:
    public_year = int(data_point['year'])
    public_period = data_point['period']
    public_job = float(data_point['value'])
    public_months.append(public_year + int(public_period[1:]) / 12)  # Combine year and month as a decimal for x-axis
    public_jobs.append(public_job)

    if public_period == 'M05' and public_year == 2019:
        print(f"Public Jobs in May 2019: {public_job}")
        public_job_may_19 = public_job
    elif public_period == 'M05' and public_year == 2023:
        print(f"Public Jobs in May 2023: {public_job}")
        public_job_may_23 = public_job

# plt.plot(public_months, public_jobs)
# plt.xlabel('Year and Month')
# plt.ylabel('Jobs (Thousands)')
# plt.title('Local Govt Jobs in Massachusetts by Month')
# plt.show()

#print(data['year'])

print(job_may_23)
print(job_may_19)
print(public_job_may_23)
print(public_job_may_19)