import yfinance as yf
import pandas as pd
from datetime import timedelta
from IPython.display import display
import matplotlib.pyplot as plt

stocks = ["INTC"]

for stock in stocks:   
    df = yf.download(stock,start=pd.to_datetime('today') - timedelta(1), interval='5m')
    plt.plot(df["High"].index.values,df['High'])
    plt.title(stock+" Stock Data")
    plt.legend(["Line"])
    plt.show()

