#doesnt fucking work

import requests
from bs4 import BeautifulSoup
import csv
import time
from datetime import datetime

PRODUCT_URL = "https://www.bestbuy.com/site/searchpage.jsp?st=rtx+4070&_dyncharset=UTF-8&_dynSessConf=&id=pcat17071&type=page&sc=Global&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
}

def get_product_price(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    price_element = soup.find("div", class_="priceView-customer-price")
    if price_element is None:
        print("Unable to find the price element.")
        return None
    price = price_element.find("span", class_="sr-only")
    if price is None:
        print("Unable to find the price.")
        return None
    price = price.next_sibling.strip()
    price = float(price.replace("$", "").replace(",", ""))
    return price

def save_price_to_file(price):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("bestbuy_price.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, price])

def track_price(url, interval_minutes):
    while True:
        price = get_product_price(url)
        if price is not None:
            save_price_to_file(price)
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Price: ${price:.2f}")
        time.sleep(interval_minutes * 60)

if __name__ == "__main__":
    track_price(PRODUCT_URL, interval_minutes=60)


"""
Chatgpt

1. Importing the required libraries:
- requests library is used to send HTTP requests to the Best Buy website.
- BeautifulSoup from the bs4 module is used for parsing HTML content.
- csv module is used for reading and writing CSV files.
- time module is used for adding a delay between price checks.

2. Defining constants:
- PRODUCT_URL: This is the URL of the product on the Best Buy website that you want to track.
- HEADERS: These are the headers sent with the HTTP request. It includes the User-Agent header, which helps simulate a web browser.

3. get_product_price(url): This function takes a URL as input, sends an HTTP request to the provided URL with the specified headers, and retrieves the price of the product from the response. It uses BeautifulSoup to parse the HTML content and extract the price element. It then cleans up the price text by removing the dollar sign and comma, converts it to a float, and returns the price.

4. save_price_to_file(price): This function takes a price as input and saves it to a CSV file along with a timestamp. It opens the CSV file in append mode, creates a CSV writer object, and writes a row containing the timestamp and the price.

5. track_price(url, interval_minutes): This function continuously tracks the price of the product at the specified URL. It runs in an infinite loop and repeatedly calls get_product_price() to fetch the current price. It then calls save_price_to_file() to save the price to the CSV file and prints the current price along with the timestamp. After that, it waits for the specified interval (in minutes) using time.sleep() before checking the price again.

6. if __name__ == "__main__": This is the entry point of the program. It calls the track_price() function with the PRODUCT_URL and the desired interval_minutes to start tracking the price.

Explaination: The program will continuously run and periodically check the price of the specified product on the Best Buy website. It saves the prices with timestamps to a CSV file and displays the current price in the console. You can adjust the interval between price checks by changing the interval_minutes parameter in the track_price() function.


"""

#chatgpt