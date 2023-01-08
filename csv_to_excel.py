import pandas as pd

read_file = pd.read_csv(r'/Users/andriikhudolii/PycharmProjects/flowerParser/result.csv')
read_file.to_excel(r'/Users/andriikhudolii/PycharmProjects/flowerParser/result.xlsx', index=None, header=True)

read_file = pd.read_csv(r'/Users/andriikhudolii/PycharmProjects/flowerParser/solds.csv')
read_file.to_excel(r'/Users/andriikhudolii/PycharmProjects/flowerParser/solds.xlsx', index=None, header=True)
