import numpy as np
import pandas_datareader.data as web
import datetime

start = datetime.datetime(2018, 2, 1)
end = datetime.datetime(2018, 7, 31)

f = web.DataReader("AAPL", "google", start, end)

print(f.head())
