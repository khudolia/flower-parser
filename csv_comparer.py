import csv
import pandas as pd

# Open the two CSV files
with open('items.csv', 'r') as items, open('solds.csv', 'r') as solds:
    # Create CSV readers for both files
    items_reader = csv.reader(items)
    solds_reader = csv.reader(solds)

    df = pd.read_csv("result.csv")

    #print(f"start: {df.loc[171, 'Id']}")

    page = 1
    # Iterate over the rows of both files
    for sold in solds_reader:
        row = 0
        items.seek(0)
        for item in items_reader:
            #print(f"compare: {item[0]} : {sold[0]}")
            #print(f"{row} .")
            if item[0] == sold[0]:
                df.loc[row-1, 'Sold Out Count'] = int(df.loc[row-1, 'Sold Out Count']) + 1
                print(f"same: {sold[0]}")
            row += 1

        #print(page)
        page += 1

    df.to_csv("result.csv", index=False)
