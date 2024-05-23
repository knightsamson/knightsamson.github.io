
import requests
import csv
from tabulate import tabulate

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=TSLA&interval=5min&apikey=C3IQDAOANXQL94CB'
CSV_FILE = 'stock_intraday.csv'
response = requests.get(url)
data = response.json()


#Extract relevant data
time_series = data['Time Series (5min)']
time_points = list(time_series.keys())

#print data rows
table_data = []
for time_point in time_points:
        open_price = time_series[time_point]['1. open']
        high_price = time_series[time_point]['2. high']
        low_price = time_series[time_point]['3. low']
        close_price = time_series[time_point]['4. close']
        volume = time_series[time_point]['5. volume']

        table_data.append([time_point, open_price, high_price, low_price, close_price, volume])

table = tabulate(table_data, headers=['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume'], tablefmt='psql')

print(table)

#open csv file for writing
with open(CSV_FILE, 'w', newline='') as csvfile:
    csvfile.write(table)

print(f"Data saved in '{CSV_FILE}' for viewing.")

