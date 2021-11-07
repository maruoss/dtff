# 01.11.2021, Digital Tools for Finance, web-api, BINANCE API exercise
# This file contains a function that retrieves n observations/trades for a 
# specific currencypair for a given frequency from a specific start date from the
# Binance API

#%%
import requests
import datetime
# import json
import pandas as pd
import time


#%% Setting global variables
# Answer question 1:
ROOT_URL = "https://api.binance.com"
# Answer question 2:
ENDPOINT = "/api/v3/klines"

# %%
# Answer question 3:
specific_date = '15/06/2021'
# Convert date to UNIX milliseconds (-> multiply seconds by 1000, Binance API expects date in milliseconds)
specific_time = 1000 * int(time.mktime(datetime.datetime.strptime(specific_date, '%d/%m/%Y').timetuple()))

# Construct request URL
request_string = "{root_url}{endpoint}?symbol={currencypair}&interval={interval}&startTime={startTime}&limit={limit}" \
        .format(root_url=ROOT_URL,
                endpoint=ENDPOINT,
                currencypair="BTCUSDT",
                interval="1m", # m = minutes, h, d, w, M
                startTime=specific_time, # CEST
                #  endTime=endTime,
                limit=75
        )
print(request_string)

# Send request to the Binance server & receive a response
resp = requests.get(request_string)
print(resp) # successful if response == <Response [200]>, bad if number >= 400, =<500

# Convert to DataFrame, resp yielded 12 values -> need to label 12 columns
data = pd.DataFrame.from_records(
        resp.json(),
        columns=["Open time", "Open", "High", "Low", "Close", "Volume", "Close time", 
        "Quote asset vol.", "Number of trades", "Taker buy base asset vol.", "Taker buy quote asset vol.", "Ignore" 
        ]
    )
# Take time as datetime index
data.index = data.pop("Open time").map(lambda x: datetime.datetime.fromtimestamp(x/1000))
print(data)

# %%
# Answer question 4:
def get_trades(currencypair: str, startdate: str, interval="1m", n_observations=75) -> pd.DataFrame:
    '''Function that takes in currency pair and startdate and returns n_observations (default 75)
    trades in the given intervals (frequency) in a pandas.DataFrame'''
# Convert date to UNIX milliseconds (-> multiply seconds by 1000, Binance API expects date in milliseconds)
    startTime = 1000 * int(time.mktime(datetime.datetime.strptime(startdate, '%d/%m/%Y').timetuple()))
    # endTime = startTime+74*60000

    # Construct request URL
    reqt = "{root_url}{endpoint}?symbol={currencypair}&interval={interval}&startTime={startTime}&limit={limit}" \
        .format(root_url=ROOT_URL,
                endpoint=ENDPOINT,
                currencypair=currencypair,
                interval=interval, # m = minutes, h, d, w, M
                startTime=startTime, # CEST
                #  endTime=endTime,
                limit=n_observations
        )
    print(reqt)

    # Send request to the Binance server & receive a response
    resp = requests.get(reqt)
    print(resp)

    # Convert to DataFrame, resp yielded 12 values -> need to label 12 columns
    data = pd.DataFrame.from_records(
        resp.json(),
        columns=["Open time", "Open", "High", "Low", "Close", "Volume", "Close time", 
        "Quote asset vol.", "Number of trades", "Taker buy base asset vol.", "Taker buy quote asset vol.", "Ignore" 
        ]
    )
    data.index = data.pop("Open time").map(lambda x: datetime.datetime.fromtimestamp(x/1000))
    return data

if __name__ == "__main__":
    # Using the same input as above
    hist_start = '15/06/2021'
    trades_df = get_trades("BTCUSDT", hist_start)
    print(trades_df)
# %%
