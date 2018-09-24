import inline as inline
from pandas_datareader import data as web
import datetime
from matplotlib import pylab as plt
import numpy as np
from scipy import stats
import seaborn
from matplotlib.pylab import rcParams
import statsmodels.api as sm
import pandas

rcParams['figure.figsize'] = 15, 6
# getting nikkei225 and Dow jones by python
# https:/qiita.com/akichikn/items/782033e746c7ee6832f5

start = datetime.date(2010, 5, 16)
end = datetime.date(2018, 7, 18)
df = web.DataReader(["NIKKEI225","WILLREITIND"], "fred", start, end)

df_diff = df.pct_change()

# US REITの分析
# https://www.mazarimono.net/entry/2018/07/20/pandas_datareader

df_diff_2 = df_diff.rolling(20).std() * np.sqrt(365)
df_diff_2 = df_diff_2.dropna()
df_diff_2.plot()
plt.show()
