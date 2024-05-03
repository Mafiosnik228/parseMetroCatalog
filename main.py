import requests
from bs4 import BeautifulSoup

url = 'https://online.metro-cc.ru/category/molochnye-prodkuty-syry-i-yayca/syry?page='
page = 1  

with open('requirements.txt', 'w') as file:
    while True:
        session = requests.Session()
        response = session.get(url + str(page))

        if response.status_code == 200:   
            soup = BeautifulSoup(response.text, 'html.parser')
            items = soup.find_all('div', class_='catalog-2-level-product-card product-card subcategory-or-type__products-item with-prices-drop')
            for item in items:
                
                productid = item.get('id')
                name = item.find('a', class_='product-card-name').get('title')
                price = item.find('span', class_='product-price__sum-rubles').text
                
                file.write(f"Product ID: {productid}\n")
                file.write(f"Наименование: {name}\n")
                file.write(f"Цена товара: {price}\n")
                file.write(f"\n")
            page += 1
        else:
            print('всё')
            break
            
