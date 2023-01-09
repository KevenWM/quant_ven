import os
import requests
import csv
import time

# Definir mês

data_id = "072022"

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}


def baixar_arquivo(url, endereco):
    # faz requisição ao servidor
    requests.adapters.DEFAULT_RETRIES = 5
    resposta = requests.get(url, headers=headers)
    # time.sleep(1)
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
            novo_arquivo.write(resposta.content)
        print("'{}',".format(endereco))
    else:
        print("ERRO")
        resposta.raise_for_status()


with open("ipe_cia_aberta_2022.csv", "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=";")

    for i, linha in enumerate(arquivo_csv):

        n = 0

        if i == 0:
            index_li = linha.index('Link_Download')
            index_dt = linha.index('Data_Referencia')
            index_tp = linha.index('Tipo')
            index_nm = linha.index('Codigo_CVM')

        else:
            link = linha[index_li]
            data = linha[index_dt]
            tipo = linha[index_tp]
            nome = linha[index_nm]

            data = data.split("-")
            data_month = data[1]
            data_year = data[0]

            data_total = data_month+data_year

            if (data_total == data_id) and (tipo == "Posição Consolidada"):

                if __name__ == "__main__":
                    BASE_URL = str(link)
                    OUTPUT_DIR = 'output'
                    nome_arquivo = os.path.join(
                        OUTPUT_DIR, 'CVM358_{}.pdf').format(nome)
                    baixar_arquivo(BASE_URL, nome_arquivo)
        n = n+1
