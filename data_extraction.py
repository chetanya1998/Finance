import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas.testing as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2000,1,1)
end = dt.datetime(2016,12,31)

df=web.DataReader('AAPL','yahoo',start,end)
print(df.head(10))
print(df.tail(10))
