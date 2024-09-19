import yfinance as yf
import pandas as pd
from datetime import timedelta
from IPython.display import display
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import argrelextrema

stocks = ["INTC", "NKE", "AAPL", "AMZN", "MCD"]

for stock in stocks:   
    df = yf.download(stock,start=pd.to_datetime('today') - timedelta(1), interval='5m')
    
    n = 5

    df['min'] = df.iloc[argrelextrema(df.High.values, np.less_equal, order=n)[0]]['High']
    df['max'] = df.iloc[argrelextrema(df.High.values, np.greater_equal, order=n)[0]]['High']

    plt.scatter(df.index, df['min'], c='r')
    plt.scatter(df.index, df['max'], c='g')
    plt.plot(df.index, df['High'])
    plt.show()

