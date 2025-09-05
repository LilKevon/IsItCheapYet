import requests
from bs4 import BeautifulSoup

url = "https://oldnavy.gapcanada.ca/browse/product.do?pid=579351053&vid=1&pcid=3028945&cid=3050027&nav=hamnav%3AMen%3ADeals%3ADeals+%26+Steals#pdp-page-content"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')


#This fetches the title of the webpage
title = soup.title
print(title)

#This fetches all the links of the page
# num_links = len(soup.find_all("a"))
# print(f"There are {num_links} links in this page")

#This fetches all the text from the page
# text = soup.get_text()
# print(text)

all_prices = soup.find_all(class_ = "current-sale-price")


num_prices = []
num_prices_clean = []
print(all_prices)

for price in all_prices:

    price_str = str(price)
    first_dash = price_str.index(">")
    last_dash = price_str.index("</")
    
    real_price = price_str[first_dash+4:last_dash]
    
    
    num_prices.append(real_price)

num_prices.sort()

print(num_prices)

seen = []
for price in num_prices:
    if price in seen:
        pass
    else:
        num_prices_clean.append(price)
        seen.append(price)

print(num_prices_clean)




