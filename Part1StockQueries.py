import requests
import json
import csv

"""
Programming Challenge:
Write a Python script to accomplish the following tasks. The program should run correctly.
- Use https://finnhub.io/ free stock price API to query stock prices for specific tech stocks.
- Get the latest price for Apple, Amazon, Netflix, Facebook, Google.
- Between Apple, Amazon, Netflix, Facebook, Google : find the stock that moved the most percentage points from yesterday. Call this stock most_volatile_stock.
- Save the following information for the most_volatile_stock to a CSV file with the
following rows. Please also include the header in the CSV file: 

Example:
stock_symbol,percentage_change,current_price,last_close_price
AAPL, 13.2, 120.5, 150


Solution Steps:
     Loop over given list of stocks.

     Build URL and make GET request to stock API.

     Return response.

     :param: list of stock appreviation.

     Getting specific values by specifying the keys(c = current price, pc = Previous close price).

     Define a header then create a CSV file called "most_volatile_stock.csv" to write the stock data in it.

     Define percentage change formula (C = x2 - x1 / x1), where C=relative change, x1=initial value, and x2=final value.

     Using if statement to compare between the stocks' percent change.

     After getting the most volatile stock's value, then we do a get request by destructuring the URL with the new value and select its values from its list(current_price, previous_close_price)

     Write the data row in CSV file.

"""

list_of_stocks = ["AAPL", "AMZN", "NFLX", "META", "GOOGL"]

def get_stocks(stocks: list):

     most_volatile_stock = None
     max_percent_change = 0
     
     for stock in stocks:
          url = f"https://finnhub.io/api/v1/quote?symbol={stock}&token=ceihoq2ad3i3rvm4imfgceihoq2ad3i3rvm4img0"
          response = requests.request(
               method='GET', url = url
               )
          
          if response.status_code == 200:
               json_response = response.json()
               current_price = json_response['c']
               previous_close_price = json_response['pc']
               percent_change = ((current_price - previous_close_price) / previous_close_price)
               if abs(percent_change) > max_percent_change:
                    max_percent_change = abs(percent_change)
                    most_volatile_stock = stock
               # print(percent_change)

     print(most_volatile_stock)

     url = f"https://finnhub.io/api/v1/quote?symbol={most_volatile_stock}&token=ceihoq2ad3i3rvm4imfgceihoq2ad3i3rvm4img0"
     res = requests.request(
               method='GET', url = url
               )
     json_response = res.json()
     current_price= json_response['c']
     previous_close_price = json_response['pc']
     percent_change = round(((current_price - previous_close_price) / previous_close_price) * 100, 2)
          

                    
     csv_column_names = (['Stock_Symbol', 'Current_Price', 'Last_Close_Price', 'Percentage_Change'])
     with open('most_volatile_stock.csv', 'w', newline='') as file:
          writer= csv.writer(file)
          writer.writerow(csv_column_names)
          writer.writerow([most_volatile_stock, current_price, previous_close_price, percent_change])
          file.close()

     print('CSV File Was Generated Successfully')

get_stocks(list_of_stocks)