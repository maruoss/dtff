# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas_datareader import data # pip install pandas-datareader

# to cache query
from pandas_datareader.yahoo.headers import DEFAULT_HEADERS
import datetime
import requests_cache
from seaborn.rcmod import plotting_context # pip install requests-cache


# %%

# Caching setup
expire_after = datetime.timedelta(days=3) # until SQLite file expires -> can still use it?
session = requests_cache.CachedSession(cache_name='cache', backend='sqlite', expire_after=expire_after)
session.headers = DEFAULT_HEADERS

# get stock data via pandas-datareader query
start = '2020-11-08'
end = '2021-11-08'
source = 'yahoo'

stocks = pd.DataFrame(columns=["Date","Close","Volume"])
stock_list = ["FB", "AAPL", "AMZN", "NFLX", "GOOGL"]
for stock in stock_list:
    df = data.DataReader(stock, start=start ,end=end, 
                         data_source=source,
                         session=session).reset_index() # get date index into "Date" column
                         # session uses cached sqlite file from above
    df["Stock"] = stock # add stock name to row-wise data
    df = df[["Date","Close","Volume", "Stock"]]
    stocks = pd.concat([stocks, df], ignore_index=True) 
    # ignore index to not get (n_stocks X n_obs) index but 0,..., n-1 index
stocks.head()

# %%
# calulate returns
stocks["DailyReturn"] = stocks["Close"].groupby(stocks["Stock"]).pct_change()

# %%
# drop na rows and reset integer index
stocks = stocks.fillna(0).reset_index(drop=True)
# %%
# compute cumulative returns
stocks["CumReturn"] = (1 + stocks["DailyReturn"]).groupby(stocks["Stock"]).cumprod()

# %%
sns.reset_orig() # reset sns settings (if sns.set changed default)
sns.set(style="whitegrid") # increase all fonts
# sns.set(rc={"axes.grid": True}) # show grid on y and x axis
fig, ax = plt.subplots(figsize = (10, 6))
sns.lineplot(data=stocks, x="Date", y="CumReturn", 
hue="Stock", style="Stock", size="Stock", palette="colorblind", dashes=True)
# hue, style and size control what visual semantics are used to indetify subsets of
# the data.  Using redundant semantics (i.e. both hue and style for the same variable) 
# can be helpful for making graphics more accessible.
# plt.legend(title="Stocks")
# plt.title("Cumulative Returns FAANG stocks")
plt.ylabel("Cumulative Returns")
plt.xlabel(None)
ax.grid(axis="x") # axis to activate BUT if sns.set used: axis to deactive.
plt.show()

# %%