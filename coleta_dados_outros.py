from sqlalchemy import create_engine
import pymysql
import pandas as pd

def conexao_mysql(host, user, password, db, table):
    #CRIAR CONEXÃO
    conn = pymysql.connect(
        host=host,
        user= user,
        password=password,
        db=db)

    cursor = conn.cursor()

    #EXECUTAR CONSULTA
    query = f'SELECT * FROM  {table} LIMIT 10'
    cursor.execute(query)

    #BUSCAR RESULTADOS
    resultados = cursor.fetchall()

    #EXIBIR OS RESULTADOS
    print('Table MySQL: ')
    for linha in resultados:
        print(linha)

    #FECHAR A CONEXÃO
    cursor.close()
    conn.close()

def df_conexao_mysql(host, user, password, db, table):
    #CRIAR CONEXAO
    conn = create_engine('mysql+pymysql://' + user + ':' + password + '@' + host + '/' + db)
# quando for usar dataframe utilize esse modo de conexão

    #EXECUTAR CONSULTA E SALVAR EM UM DATAFRAME
    query = f'SELECT * FROM {table}'
    df = pd.read_sql(query, conn)

    #EXIBIR RESULTADOS
    print('Tabela MySQL com DataFrame: \n', df.head())

    #FECHAR A CONEXÃO
    conn.dispose()
    return df

def conexao_excel(path):
    #LER ARQUIVO EXCEL
    df = pd.read_excel(path)
    print('Dados Excel: \n', df.head())

    #Escrever arquivos CSV
    df.to_csv('dados.csv', index=False)

def conexao_csv(path):
    #LER ARQUIVO CSV
    df = pd.read_csv(path)
    print('Dados CSV: \n', df.head())

    #ESCREVER ARQUIVO JSON
    df.to_json('dados.json', orient='records', index=False)



conexao_mysql('127.0.0.1', 'root', 'hfp1993', 'loja_informatica', 'cliente')


df_cliente = df_conexao_mysql('127.0.0.1','root', 'hfp1993', 'loja_informatica', 'cliente')
df_cliente.to_excel('dados.xlsx', index=False)

conexao_excel('dados.xlsx')
conexao_csv('dados.csv')