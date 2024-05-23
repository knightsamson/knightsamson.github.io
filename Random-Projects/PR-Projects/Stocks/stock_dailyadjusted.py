import requests
import pandas as pd
from tabulate import tabulate
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=TSLA&apikey=C3IQDAOANXQL94CB'
r = requests.get(url)
data = r.json()

#extract the daily data from the response
time_series = data['Time Series (Daily)']

#Convert the data into a pandas DataFrame
df = pd.DataFrame.from_dict(time_series, orient='index')
df.reset_index(inplace=True)
df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Adjusted Close', 'Volume', 'Dividend Amount', 'Split Coefficient',]

#format the dataframe as a table
table = tabulate(df, headers='keys', tablefmt='psql')

#Display the DataFrame
print(table)


with open('stock_adjusted.csv', 'w') as file:
    file.write(table)
print("Data saved to stock_data.csv")