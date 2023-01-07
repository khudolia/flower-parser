import csv
import os
import sys
import time
from datetime import datetime
from math import trunc

from bs4 import BeautifulSoup
import requests

# Set up the empty list to store the items
items = []


def main(inp_page):
    # Set up the base URL and the page number
    base_url = "https://www.etsy.com/shop/ForLoveOfPampas/sold"
    page = inp_page
    items_count = 0

    await_time = 0

    # Set up the loop to go through all the pages
    while page <= 944:
        print(f"                            page: {page}")

        # Construct the full URL with the page parameter
        url = f"{base_url}?ref=pagination&page={page}"

        # Make a request to the website and get the HTML
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        # Find all the items on the page
        # item_divs = soup.find_all(class_='v2-listing-card__info')
        item_divs = soup.find_all(
            class_='js-merch-stash-check-listing v2-listing-card wt-position-relative wt-grid__item-xs-6 wt-flex-shrink-xs-1 wt-grid__item-xl-3 wt-grid__item-lg-4 wt-grid__item-md-4 listing-card-experimental-style')

        if item_divs.__len__() > 0:
            for item_div in item_divs:
                # Get the title and price of the item
                title = item_div.find(class_='v2-listing-card__title').get_text().strip()
                id = item_div['data-listing-id']
                print(id)
                # Add the item to the list
                items.append([id, title])
                items_count += 1

            write_csv()
            print(f"length: {item_divs.__len__()}")
            print(f"items_count: {items_count}")
            page += 1
            await_time = 0
            time.sleep(5.0)
        else:
            print(f"Going overtime: {await_time}")
            await_time += 2
            write_csv()
            update(await_time)



def write_csv():
    if items.__len__() == 0:
        print("list is empty!")
    else:
        print("Saved!")
        # Write the items to a CSV file
        writer.writerows(items)
        items.clear()


def update(await_time):
    for i in range(60 * await_time):
        print(f"{trunc(i / 60)}:{i % 60}")
        time.sleep(1.0)


def script_restarter(current_page):
    export_args = current_page
    print("RESTARTING!!!")
    print(sys.argv)

    if sys.argv.__len__() > 1:
        print(sys.argv[1])
        sys.argv[1] = str(int(sys.argv[1]))
    else:
        sys.argv.append(str(export_args))

    os.execv(sys.executable, ['python'] + sys.argv)


if __name__ == "__main__":
    #start_time = datetime.now()

    inp_page = 1
    #if sys.argv.__len__() > 1:
    #    inp_page = int(sys.argv[1])
    isEmpty = True

    with open('solds.csv', 'r', newline='') as csvfile:
        line = csvfile.readline()
        if line != b'':
            isEmpty = False
            print("empty")

    with open('solds.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(["id", "Title"])

        main(inp_page)
