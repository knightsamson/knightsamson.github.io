# C3IQDAOANXQL94CB API KEY

import csv
import requests
from tabulate import tabulate

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=TSLA&interval=15min&slice=year1month1&apikey=C3IQDAOANXQL94CB'
CSV_FILE = 'stock_extendedhistory.csv'

with requests.Session() as s:
    download = s.get(CSV_URL)
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    headers = my_list[0]
    data = my_list[1:]


table = tabulate(data, headers=headers, tablefmt = 'grid')

with open(CSV_FILE, 'w') as file:
    file.write(table)

print(f"Data saved in '{CSV_FILE}' for viewing.")

#chatgpt