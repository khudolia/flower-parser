import csv
import time
from multiprocessing import process

from bs4 import BeautifulSoup
import requests

# Set up the base URL and the page number
base_url = "https://www.etsy.com/shop/ForLoveOfPampas/sold"
page = 1

# Set up the empty list to store the items
items = []

# Set up the loop to go through all the pages
while page <= 10:
    print(f"{page}")

    # Construct the full URL with the page parameter
    url = f"{base_url}?ref=pagination&page={page}"

    # Make a request to the website and get the HTML
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    # Find all the items on the page
    #item_divs = soup.find_all(class_='v2-listing-card__info')
    item_divs = soup.find_all(class_='js-merch-stash-check-listing v2-listing-card wt-position-relative wt-grid__item-xs-6 wt-flex-shrink-xs-1 wt-grid__item-xl-3 wt-grid__item-lg-4 wt-grid__item-md-4 listing-card-experimental-style')

    for item_div in item_divs:
        # Get the title and price of the item
        title = item_div.find(class_='v2-listing-card__title').get_text().strip()
        id = item_div['data-listing-id']

        # Add the item to the list
        items.append([id, title])

    page += 1
    time.sleep(0.1)

# Write the items to a CSV file
with open('solds.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["id", "Title"])
    writer.writerows(items)
