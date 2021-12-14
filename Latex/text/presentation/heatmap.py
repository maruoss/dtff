# %%
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
# cols and index definition for heatmap
cols = ["FB", "AAPL", "AMZN", "NFLX", "GOOGL"]
dateidx = pd.bdate_range(start="2021-11-01", periods=6).strftime("%d-%m-%Y")

# %%
# daily return data (not real data)
df = pd.DataFrame(([0.015, 0.005, 0.025, 0.031, 0.006]
, [0.006, 0.002, 0.006, 0.012, 0.026]
, [0.052, 0.058, 0.091, 0.043, 0.112]
, [0.033, 0.024, 0.018, 0.043, 0.062]
, [-0.011, -0.041, -0.035, -0.003, -0.021]
, [0.003, -0.010, 0.015, -0.012, -0.045]),
index = dateidx, columns = cols)

# %%
sns.reset_orig()
sns.set(font_scale=1.3)
fig, ax = plt.subplots(figsize = (10, 6))
sns.heatmap(df, cmap="RdBu", center=0, annot=True) #center at 0 return, show returns in heatmap
#cmap options: "RdBu", "coolwarm", etc. see: https://matplotlib.org/stable/tutorials/colors/colormaps.html
plt.title("Daily (fictional) Returns FAANG stocks", fontsize=25)
plt.ylabel("Date", fontsize=20)
plt.xlabel("Ticker", fontsize=20)
plt.show()


# %%
