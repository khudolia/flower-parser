import csv
import re
import time
from bs4 import BeautifulSoup
import requests

# Set up the base URL and the page number
base_url = "https://www.etsy.com/shop/ForLoveOfPampas?ref=condensed_trust_header_title_sold"
page = 1

# Set up the empty list to store the items
items = []

# Set up the loop to go through all the pages
while True:
    print(f"{page}")

    # Construct the full URL with the page parameter
    url = f"{base_url}&page={page}#items"

    # Make a request to the website and get the HTML
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    # Find all the items on the page
    item_divs = soup.find_all('div', class_='v2-listing-card')

    for item_div in item_divs:
        # Get the title and price of the item
        title = item_div.find('h3', class_='v2-listing-card__title').text.strip()
        subtotal_price = item_div.find('span', class_='currency-value').text.strip()
        price = item_div.find('p', class_='search-collage-promotion-price').find('span', class_='currency-value').text.strip()
        discount_text = item_div.find('p', class_='wt-text-caption search-collage-promotion-price wt-text-slime wt-text-truncate wt-no-wrap').find_all("span")[-1].text.strip()
        discount = re.sub("[^0-9]", "", discount_text)

        # Add the item to the list
        items.append([title, price, f"{discount}%", subtotal_price, ""])

    li_list = soup.find('nav', attrs={'aria-label': 'Pagination of listings'}).find_all('li', class_="wt-action-group__item-container")

    last_button = li_list[-1]
    a = last_button.find('a')
    if a.has_attr('href'):
        time.sleep(0.1)
    else:
        break

    # Increment the page number
    page += 1


# Write the items to a CSV file
with open('items.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Total Price", "Discount", "Subtotal price", "Sold Out Count"])
    writer.writerows(items)
