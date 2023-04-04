import requests
from bs4 import BeautifulSoup

url = "https://www.tabnews.com.br/"

response = requests.get(url)

if response.status_code == 200:
    print("Requisição bem sucedida!")
else:
    print("Requisição mal sucedida!")
    
    
soup = BeautifulSoup(response.text, 'html.parser')
titles = soup.find_all('a', class_='Link__StyledLink-sc-14289xe-0 jgIQPD')

for title in titles:
    print(title.text)