import datetime as dt
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

stocks = ["AMZN", "MSFT", "META", "GOOG"]
start = dt.datetime.today()-dt.timedelta(3650)
end = dt.datetime.today()
cl_price = pd.DataFrame()
ohlcv_data = {}

for ticker in stocks:
    cl_price[ticker] = yf.download(ticker, start, end)["Adj Close"]

# filling NaN values
cl_price.dropna(axis=0, how='any', inplace=True)

daily_return = cl_price.pct_change()

fig, ax = plt.subplots()
ax.set(title="Mean Daily Return of Stocks", xlabel = "Stocks", ylabel = "Mean Returns")
plt.bar(x=daily_return.columns, height = daily_return.mean())
plt.show()