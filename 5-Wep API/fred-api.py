## libraries
from matplotlib import pyplot
import os
import requests
from fredapi import Fred

# Source https://lvngd.com/blog/fred-api-python/
individual_fred_key = "abc123" # fake api key
#individual_fred_key = os.environ['fredApiKey'] # valid api key

# Answer Question 2
ROOT_URL = "https://api.stlouisfed.org"

# Answer Question 3
ENDPOINT = "/fred/series/observations"

# Answer Question 4
params = {
    'api_key': individual_fred_key,
    'series_id': 'UNRATE',
    'file_type': 'json', # or xml
    'observation_start': '2020-01-01'
}

# Send request to the Fred server & receive a response
resp = requests.get(f"{ROOT_URL}{ENDPOINT}", params = params)

# resp == 400 (failed) with fake api key, but resp == 200 with valid key
print(resp) 

# Alternatively: use wrapper by mortdata
# Source https://github.com/mortada/fredapi, https://pypi.org/project/fredapi/
fred = Fred(api_key = individual_fred_key)
unRateSeries = fred.get_series('UNRATE', '2020-01-01') # returns pandas Series

# timeseries plot
unRateSeries.plot()
pyplot.show()

# density plot
unRateSeries.plot(kind='kde')
pyplot.show()

