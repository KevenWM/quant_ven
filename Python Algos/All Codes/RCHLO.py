import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import math

url = 'https://www.riachuelo.com.br/feminino/colecao-feminino'

headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit / 537.36 \ "
                          "(KHTML, like Gecko) Chrome / 105.0.0.0 Safari / 537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
qtd_itens = soup.find('div', class_='MuiTypography-body2').get_text().strip()

index = qtd_itens.find(' ')
qtd = qtd_itens[:index]
qtd2 = int(qtd.replace(".",""))
print(index)
print(qtd2)

ultima_pagina = math.ceil(int(qtd2)/48)

dic_produtos ={'marca':[], 'preço':[]}

for i in range(1, qtd2):
    url_pag = f'https://www.riachuelo.com.br/feminino/colecao-feminino'
    site = requests.get(url_pag, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    produtos = soup.find_all('li', class_=re.compile('MuiGrid-root MuiGrid-item MuiGrid-grid-xs-6 MuiGrid-grid-md-3'))

    for produto in produtos:
        marca = produto.find('h3', class_=re.compile('MuiTypography-root jss153 MuiTypography-body2')).get_text().strip()
        preço = produto.find('div', class_=re.compile('jss161')).get_text().strip()

        print(marca, preço)

        dic_produtos['marca'].append(marca)
        dic_produtos['preço'].append(preço)



df =pd.DataFrame(dic_produtos)
df.to_csv('C:/Users/felipe.leal/Desktop/Monitor de preços - Centauro/Riachuelo.csv' + '.csv', encoding='utf-8', sep=';')

