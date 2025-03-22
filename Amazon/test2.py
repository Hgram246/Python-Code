import requests
import time
from bs4 import BeautifulSoup
import pandas as pd
url = "https://www.amazon.com/dp/B0B3BVWJ6Y"
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'
    }

def callpage():
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')
    if soup.find('span', {'class': 'a-offscreen'}) is None:
        callpage()
    else: 
        product_price = soup.find('span', {'class': 'a-offscreen'}).text.strip()
        print(product_price)
    

    

    
    
    
        

    
callpage()