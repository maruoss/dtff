# downstream.py
import pandas as pd
from connect import DATAPATH

def get_fx_data(start_dt, end_dt):
  """ e.g. start_dt = 2016-10-04 """
  filename = DATAPATH + "fx.ftr"

  data = pd.read_feather(filename)

  date_column = 'Date'
  manipulate = (data[date_column] >= start_dt) & (data[date_column] <= end_dt)
  data = data.loc[manipulate]

  return data

