import math
import re
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import date

url = 'https://www.nike.com.br/nav/genero/masculino/tipodeproduto/vestuario'

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
qtd_itens = soup.find('span', class_='itemCountHdl').get_text().strip()
qtd_itens2 = qtd_itens.replace("(","").replace(")","")
index = qtd_itens2.find(' ')
qtd = qtd_itens2[:index]
ultima_pagina = math.ceil(int(qtd)/12)

dic_produtos = {'marca':[], 'nome': [], 'preco':[]}

for i in range(1, ultima_pagina+1):
    url_pag = f'https://www.brownells.com/firearms/handguns/index.htm?f_a={(i*12)+1}'
    site = requests.get(url_pag, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')

    produtos = soup.find_all('div', class_=re.compile('media listing'))

    for produto in produtos:
        marca = produto.find('p', class_=re.compile('mfr')).get_text().strip()
        nome = produto.find('div', class_=re.compile('group1')).get_text().strip()
        preco = produto.find('span', itemprop=re.compile('lowPrice')).get_text().strip()

        preco = preco.strip().replace('$', '').replace(',', '').replace('.', ',')

        print(marca, nome, preco)

        dic_produtos['marca'].append(marca)
        dic_produtos['preco'].append(preco)
        dic_produtos['nome'].append(nome)

    print(url_pag)

df = pd.DataFrame(dic_produtos)

today = date.today()

df.to_csv(f'C:/Users/felipe.leal/Desktop/Monitor de preços - Nike' + str(today) + '.csv', encoding='utf-8', sep=';')


