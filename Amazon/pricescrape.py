import requests
from bs4 import BeautifulSoup

def get_amazon_price(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        price = soup.find(id='priceblock_ourprice')  # Update this selector based on Amazon's HTML structure
        if price:
            return price.get_text().strip()
    return 'Price not found'

# URL of the product page on Amazon
asin = "B00X848NW2"
url = "https://www.amazon.com/dp/"+asin

price = get_amazon_price(url)
print(f"The price of the product is: {price}")