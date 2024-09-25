import yfinance as yf
import pandas as pd
from datetime import timedelta 
from datetime import date
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import argrelextrema

stocks = ['AAPL','INTC','NVDA',]
today = date.today()
yesterday = date.today() - timedelta(1)
formatted_date = today.strftime("%Y-%m-%d")

for stock in stocks:   
    df = yf.download(stock, start=today,interval='1d')

    todayschange = ((df.at[formatted_date,'Close']/df.at[formatted_date,'Open'])-1)*100
    if todayschange < 0:
        print(stock +' stock decreased by ' +str(todayschange)+"%")
    elif todayschange > 0:
        print(stock +' stock increased by +' +str(todayschange)+"%")
    else: print(stock +' stock did not change')

    plt.plot(df.index, df['High'])
    plt.show()


    
    
    