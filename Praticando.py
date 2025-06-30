import requests
from bs4 import BeautifulSoup
''' BeautifulSoup: é uma biblioteca que 
LÊ e INTERPRETA faz o "parser" de um conteúdo HTML/XML
Parser: "Parsear" signifia transformar o texto HTML 
em uma estrutura que o Python consegue entender 
'''
#exemplo básico
html = "<h1>Olá Herlen!"
extrair = BeautifulSoup(html, "html.parser")

print(extrair.h1.text)

#exemplo de um html real

url = 'https://quotes.toscrape.com'
requisicao = requests.get(url)
extrair = BeautifulSoup(requisicao.text, "html.parser")

for quote in extrair.find_all('div', class_='quote'):
    texto = quote.find('span', class_='text').text
    autor = quote.find('small', class_='author').text
    tags = [tag.text for tag in quote.find_all('a', class_='tag')]

    print(f'Frase: {texto}')
    print(f'Autor: {autor}')
    print(f'Tags: {", ".join(tags)}\n')