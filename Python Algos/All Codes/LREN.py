import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import math


url = 'https://www.lojasrenner.com.br/c?s_icid=20220318_HOME-FEMININO_CATEGORIA_FEM&toggleOmni=false&sortBy=productSells&page=1'
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit / 537.36 \ "
           "(KHTML, like Gecko) Chrome / 105.0.0.0 Safari / 537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
qtd_itens = soup.find(
    'span', class_='ResultListToolbar_numberOfResultsHighlighted__DaLyL').get_text()

index = qtd_itens.find(' ')
qtd = qtd_itens[:index]

ultima_pagina = math.ceil(int(qtd)/48)

dic_produtos = {'marca': [], 'preço': []}

for i in range(1, ultima_pagina+1):
    url_pag = f'https://www.lojasrenner.com.br/c?s_icid=20220318_HOME-FEMININO_CATEGORIA_FEM&toggleOmni=false&sortBy=productSells&page={i}'
    site = requests.get(url_pag, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    produtos = soup.find_all('a', class_=re.compile('ProductBox_productBox'))

    for produto in produtos:
        marca = produto.find('div', class_=re.compile(
            'ProductBox_productInfo_')).get_text().strip()
        preco = produto.find('div', class_=re.compile(
            'ProductBox_price')).get_text().strip()

        print(marca, preco)

        dic_produtos['marca'].append(marca)
        dic_produtos['preco'].append(preco)

df = pd.DataFrame(dic_produtos)
df.to_csv('C:/Users/felipe.leal/Desktop/Monitor de preços - Centauro/LREN.csv' +
          '.csv', encoding='utf-8', sep=';')

df = pd.DataFrame(dic_produtos)

#today = date.today()
today = 1

df.to_csv(f'C:/Users/felipe.leal/Desktop/Monitor de preços - LREN' +
          str(today) + '.csv', encoding='utf-8', sep=';')
