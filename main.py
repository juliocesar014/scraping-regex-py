import requests
from bs4 import BeautifulSoup
import re

# Faz o request da página
url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

nome_produto = "Lenovo"

produtos = soup.find_all('div', class_='thumbnail')
produtos_filtrados = [produto for produto in produtos if re.search(r"\b" + nome_produto + r"\b", produto.text)]

for produto in produtos_filtrados:
    titulo_tag = produto.find('a', class_='title')
    titulo = titulo_tag.get_text()
    preco_tag = produto.find('div', class_='caption')
    preco = preco_tag.find('h4', class_='pull-right price').get_text().strip()
    print(f'TITULO: {titulo} / PREÇO: {preco}')


