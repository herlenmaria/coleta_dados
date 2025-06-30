
import requests #enquanto estiver cinza nao esta sendo utilizado
from bs4 import BeautifulSoup
import pandas

print('Request: ')
response = requests.get('https://webscraper.io/test-sites/tables/tables-semantically-correct')
print(response.text[:600])

print('BeatifulSoup')
soup = BeautifulSoup(response.text,'html.parser') #classe
print(soup.prettify()[:1000])

print('pandas: ')
url_dados = pandas.read_html('https://webscraper.io/test-sites/tables/tables-semantically-correct')

print(url_dados[0])