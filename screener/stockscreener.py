import yfinance as yf
import pandas as pd
from datetime import timedelta
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import argrelextrema

stocks = ["BTC-USD", "ETH", "SOL", "TRX"]

for stock in stocks:   
    df = yf.download(stock,start=pd.to_datetime('today') - timedelta(6), interval='1m')

    #I don't know how this works, but it returns the right things.
    #I lifted this from stack overflow, link below
    #https://stackoverflow.com/questions/48023982/pandas-finding-local-max-and-min
    #  <3

    #the higher n is, the less local min/max it will find.
    
    n = 15

    df['min'] = df.iloc[argrelextrema(df.High.values, np.less_equal, order=n)[0]]['High']
    df['max'] = df.iloc[argrelextrema(df.High.values, np.greater_equal, order=n)[0]]['High']

    max = df[(df['max']>0)].select_dtypes(include=['datetime'])
    min = df[(df['min']>0)].select_dtypes(include=['datetime'])

    maxlist = max.index.tolist()
    minlist = min.index.tolist()
    
    
    file = open("data/"+stock+'(max).txt', 'w')
    for item in maxlist:
        file.write(str(item)+'\n')
    file.close()
    file = open("data/"+stock+'(min).txt', 'w')
    for item in minlist:
        file.write(str(item)+'\n')
    file.close()
    
    


    plt.title(stock+" Stock Data")
    plt.scatter(df.index, df['min'], c='r')
    plt.scatter(df.index, df['max'], c='g')
    plt.plot(df.index, df['High'])
    plt.show()
    
    