from opcode import opname

import requests
import os


def enviar_arquivo():
    # Caminho do arquivo para upload
    caminho = '/home/usuario/teste_upload.txt'

    if not os.path.exists(caminho):
        print('Arquivo não encontrado')
        return

    with open(caminho, 'rb') as arquivo:
      requisicao = requests.post('https://file.io', files={'file': arquivo})

    print('Código de status da resposta: ', requisicao.status_code)
    print('Conteúdo da resposta (texto): ', requisicao.text)


    try:
        saida_requisicao = requisicao.json()
        print('Resposta JSON:', saida_requisicao)
        url = saida_requisicao.get('Link', 'Link não encontrado')
        print('Arquivo enviado! Link para acesso:', url)
    except requests.exceptions.JSONDecodeError:
        print('A resposta não é um JSON VÁLIDO. Pode ter ocorrido um erro no servidor.')

def enviar_arquivo_chave():
    caminho= ''
    chave_acesso = "" #API KEY

    #ENVIAR O ARQUIVO
    requisicao = requests.post(
        'https: // file.io',
        files={'file': open(caminho, 'rb')},
        headers={'Authorization': chave_acesso}
    )
    saida_requisicao = requisicao.json()

    print(saida_requisicao)
    url = saida_requisicao['link']
    print('Arquivo enviado com chave. Link acesso: ', url)


def receber_arquivo(file_url):
    #RECEBER O ARQUIVO
    requisicao = requests.get(file_url)

    #SALVAR O ARQUIVO
    if requisicao.ok:
        with open('arquivo_baixado.xlsx', 'wb') as file:
            file.write(requisicao.content)
        print('Arquivo baixado com sucesso.')
    else:
        print('Erro ao baixar o arquivo:', requisicao.json())



enviar_arquivo()
receber_arquivo()



