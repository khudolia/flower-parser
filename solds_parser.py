import csv
import time
from bs4 import BeautifulSoup
import requests

# Set up the base URL and the page number
base_url = "https://www.etsy.com/shop/ForLoveOfPampas/sold"
page = 1

# Set up the empty list to store the items
items = []

# Set up the loop to go through all the pages
while True:
    # Construct the full URL with the page parameter
    url = f"{base_url}&page={page}#items"

    # Make a request to the website and get the HTML
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    # Find all the items on the page
    item_divs = soup.find_all(class_='v2-listing-card__info')

    print(html)
    for item_div in item_divs:
        # Get the title and price of the item
        title = item_div.find(class_='v2-listing-card__title').get_text()

        # Add the item to the list
        items.append([title])
        print(title)

    # Increment the page number
    page += 1
    #print(f"{page}")

    #li_list = soup.find_all(class_="btn-group-md list-unstyled text-left")#.find_all('li', class_="wt-action-group__item-container")

   # print(li_list)
    #last_button = li_list[-1]
    #a = last_button.find('a')
    if page <= 10:
        break
    else:
        break


# Write the items to a CSV file
with open('solds.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title"])
    writer.writerows(items)
