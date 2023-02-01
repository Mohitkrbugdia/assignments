# question 1
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time


options = Options()
options.headless = True


driver = webdriver.Chrome(options=options)


url1 = "https://www.amazon.in/s?k=bags&page="


data = []

for i in range(1, 21):

    url = url1 + str(i)

    
    driver.get(url)

    time.sleep(2)

    html = driver.page_source

    soup = BeautifulSoup(html, "html.parser")

    products = soup.find_all("div", class_="s-result-item")


    for product in products:
        product_url = product.find("a", class_="a-link-normal")["href"]


        name = product.find("h2").text.strip()


        price = product.find("span", class_="a-offscreen").text.strip()


        rating = product.find("span", class_="a-icon-alt")
        rating = rating.text.strip() if rating else None


        num_reviews = product.find("span", class_="a-size-base")
        num_reviews = num_reviews.text.strip() if num_reviews else None
        
        data.append([product_url, name, price, rating, num_reviews])
driver.quit()
for item in data:
    print(item)
    
    
    
    
# question 2
import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []

for url in product_urls:
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    description = soup.find('div', {'id': 'productDescription'}).text
    asin = soup.find('td', {'class': 'a-size-medium a-text-bold'}).text.replace('ASIN:', '').strip()
    product_description = soup.find('div', {'id': 'feature-bullets'}).text
    manufacturer = soup.find('a', {'id': 'bylineInfo'}).text

    # Storing in dictionary
    product_data = {
        'description': description,
        'asin': asin,
        'product_description': product_description,
        'manufacturer': manufacturer
    }

    data.append(product_data)

df = pd.DataFrame(data)
df.to_csv('product_data.csv', index=False)
