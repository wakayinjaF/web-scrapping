import requests
from bs4 import BeautifulSoup
import plotly.express as px
import pandas as pd

url = "https://www.jumia.ug/mlp-samsung-weekend-takeover/"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

lists = soup.find_all('div', class_='info')


def CleanPrice(undesiredprice):
    parts = undesiredprice.split()
    if len(parts) >= 2:
        price_with_commas = parts[1]
        clean_price = price_with_commas.replace(',', '')
        value = int(clean_price)
        return value
    return None


# Create a list to store data
data = []

for list in lists:
    prdname = list.find('h3', class_="name").text
    prdprice = list.find('div', class_="prc").text

    cprdprice = CleanPrice(prdprice)

    data.append({'name': prdname, 'price': cprdprice})

# Create a DataFrame
df = pd.DataFrame(data)

# Create an interactive bar graph using Plotly Express
fig = px.bar(df, x='name', y='price', title='Samsung Product Prices')

# Save the graph as an HTML file
fig.write_html('samsung_prices.html')
