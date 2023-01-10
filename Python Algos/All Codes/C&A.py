import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import math

url = 'https://www.cea.com.br/moda-feminina/colecoes/?order=OrderByTopSaleDESC'

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit / 537.36 \ "
           "(KHTML, like Gecko) Chrome / 105.0.0.0 Safari / 537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
qtd_itens = soup.find('div', class_=re.compile(
    'cea-search-result-1-x-total-products')).get_text().strip()

index = qtd_itens.find(' ')
qtd = qtd_itens[:index]
qtd2 = int(qtd.replace(".", ""))
print(index)
print(qtd2)

ultima_pagina = math.ceil(int(qtd2)/24)

dic_produtos = {'marca': [], 'preço': []}

for i in range(1, ultima_pagina+1):
    url_pag = f'https://www.cea.com.br/moda-feminina/colecoes/?order=OrderByTopSaleDESCpage={i}'
    site = requests.get(url_pag, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    produtos = soup.find_all('div', class_=re.compile(
        'cea-search-result-1-x-gallery__item'))

    for produto in produtos:
        marca = produto.find('span', class_=re.compile(
            'brandName')).get_text().strip()
        preço = produto.find('section', itemprop_=re.compile(
            'price')).get_text().strip()

        print(marca, preço)

df = pd.DataFrame(dic_produtos)

#today = date.today()

today = 1

df.to_csv(f'C:/Users/felipe.leal/Desktop/Monitor de preços - CEA' +
          str(today) + '.csv', encoding='utf-8', sep=';')
