import requests
from bs4 import BeautifulSoup
import pandas as pd
from decimal import Decimal
from alive_progress import alive_bar

df = pd.read_excel("/Users/henryg/Documents/Business_Spreadsheets/Amazon_Products.xlsx")
asins = (df["ASINS"].dropna())

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
        try: 
            product_price = soup.find('span', {'class': 'a-offscreen'}).text.strip()
            price = product_price.strip("$")

            df.loc[row_index, 'Sale Price Per'] = float(price)

        except:
            pass

counter = 0 

tasin = str(asins.shape[0])

for asin in asins:
    row_index = df.index[df['ASINS'] == asin].tolist()
    
    url = "https://www.amazon.com/dp/"+asin

    callpage()
    
    counter = counter +1

    print(str(counter) + "/" + tasin )
   

print("All ASINS have been screened.")


df["Sale Price Per"].to_excel('/Users/henryg/Documents/Business_Spreadsheets/Amazon_Products_Updated_Prices.xlsx', index=False)

print("Data has succesfully been updated in Excel.")