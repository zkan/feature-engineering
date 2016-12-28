# http://machinelearningmastery.com/moving-average-smoothing-for-time-series-forecasting-python/

from pandas import Series
from matplotlib import pyplot


series = Series.from_csv('data/daily-total-female-births-in-cal.csv', header=1)
print(series.head())
print(series.tail())
series = series.drop(series.index[-1])
print(series.tail())
series.plot()
pyplot.show()

# Tail-rolling average transform
rolling = series.rolling(window=3)
rolling_mean = rolling.mean()
print(rolling_mean.head(10))
# plot original and transformed dataset
series.plot()
rolling_mean.plot(color='red')
pyplot.show()
