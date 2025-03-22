import pandas as pd
import requests
from bs4 import BeautifulSoup
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'}
url='https://www.amazon.in/gp/bestsellers/books/1318158031/ref=zg_bs_nav_books_1'
req = requests.get(url,headers=headers)
print(req)
soup = BeautifulSoup(req.text, 'lxml')
books = soup.find("div", class_="p13n-gridRow _cDEzb_grid-row_3Cywl").find_all("div", id="gridItemRoot")
    
for book in books:
    rank = book.find("div", class_="aok-float-left").span.text.split("#")[1]
    name = book.find("div", class_="zg-grid-general-faceout").span.div
    name=name.text if name else None
    author = book.find("div", class_="a-row a-size-small").div.text
    rating = book.find("span", class_="a-icon-alt")
    rating=rating.text if rating else None
    price = book.select_one(".a-size-base.a-color-price span").text
    #price=price.text if price else None
    print(price)