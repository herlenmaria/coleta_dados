import requests
from bs4 import BeautifulSoup

url = 'https://realpython.com/tutorials/'
requisicao = requests.get(url)
# requisição GET - BUSCAR DADOS - Fazendo a requisição para o site
extracao = BeautifulSoup(requisicao.text, "html.parser")
# Pega informações de sites automaticamente e extrai dados HTML e XML

# Exibir o texto
print(extracao.text.strip())

# #Filtrar a exibicao pela tag
# soma = 0
# for linha_texto in extracao.find_all('p'):
#     titulo = linha_texto.text.strip()
#     soma +=1
#     print(f'Título: \n', titulo)
#
#
#
# for linha_texto in extracao.find_all('h2'):
#     paragrafo = linha_texto.text.strip()
#     soma +=1
#     print(f'Parágrafo: \n', paragrafo)
#
#
# print(f'Soma p: {soma}')
# print(f'Soma h2: {soma}')

# Exibir tags aninhadas
for titulo in extracao.find_all('h2'):
    print('\n Título: ', titulo.text.strip())
    for link in titulo.find_next_siblings('p'):
        for a in link.find_all('a', href=True):
            print('Texto Link: ', a.text.strip(), ' | URL: ', a["href"])