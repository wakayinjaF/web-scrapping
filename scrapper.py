#python web scrap file


import requests
import csv
from bs4 import BeautifulSoup
from csv import writer
import pandas as pd
import matplotlib.pyplot as plt

url = "https://www.jumia.ug/mlp-samsung-weekend-takeover/"

response = requests.get(url)

soup = BeautifulSoup(response.text,  'html.parser')

lists = soup.find_all('div', class_='info')

def CleanPrice(undesiredprice):
    # Split the input string by spaces
    parts = undesiredprice.split()

    # Check if the split result contains at least two parts
    if len(parts) >= 2:
        # Extract the second part, which should be the price with commas
        price_with_commas = parts[1]

        # Remove commas from the price
        clean_price = price_with_commas.replace(',', '')

        # Convert the cleaned price to an integer (assuming it's an integer value)
        value = int(clean_price)

        return value

    # Return None if the input format is invalid
    return None



#open the csv file
with open('samsung.csv', 'w+', encoding="utf8", newline='') as f:
    thewriter = writer(f)
    # write headers to the csv file
    header = ['name',  'price']
    thewriter.writerow(header)



    for list in lists:
        prdname = list.find('h3', class_="name").text
        prdprice = list.find('div', class_="prc").text

        #prdprice is raw data and we need to clean it using a function


        #cleaning the price
        #cprdprice is cleaned price
        cprdprice = CleanPrice(prdprice)


        

        info = [prdname,  cprdprice]
        thewriter.writerow(info)


# Read the CSV file into a DataFrame
df = pd.read_csv('samsung.csv')

# Create a bar graph
plt.figure(figsize=(10, 6))
plt.bar(df['name'], df['price'])
plt.xlabel('Product Names')
plt.ylabel('Prices')
plt.title('Samsung Product Prices')
plt.xticks(rotation=90)  # Rotate x-axis labels for readability
plt.tight_layout()

# Save or display the graph
plt.savefig('samsung_prices.png')
plt.show()

