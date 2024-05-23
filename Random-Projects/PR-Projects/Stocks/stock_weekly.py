# C3IQDAOANXQL94CB

import requests
import csv
from tabulate import tabulate


# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=TSLA&apikey=C3IQDAOANXQL94CB'
r = requests.get(url)
data = r.json()

time_series = data['Weekly Time Series']

table_data = []
for date, values in time_series.items():
    row = [date, values['1. open'], values['2. high'], values['3. low'], values['4. close'], values['5. volume']]
    table_data.append(row)

table = tabulate(table_data, headers=['Date', 'Open', 'High', 'Low', 'Close', 'Volume'], tablefmt='psql')

print(table)

CSV_FILE = 'stock_weekly.csv'
with open(CSV_FILE, 'w', newline='') as csvfile:
    csvfile.write(table)
    #writer = csv.writer(csvfile)
    #writer.writerow(['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])
    #writer.writerows(table_data)

print(f"Data saved in '{CSV_FILE}' for viewing")