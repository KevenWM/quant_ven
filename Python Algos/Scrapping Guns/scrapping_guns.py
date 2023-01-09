import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import math
import pathlib


url = 'https://www.gricegunshop.com/firearms/handguns.html'

headers = {'User-Agent':
           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
qnt_itens = soup.find('p', id='toolbar-amount').get_text().strip()

index = qnt_itens.find('of')
qtd = qnt_itens[index:]
index = qtd.find(' ')
qtd2 = int(qtd[index:].strip())

x = math.ceil(int(qtd2/12))

dic_produtos = {'marca': [], 'preco': []}

for i in range(1, x + 1):
    url_pag = f'https://www.gricegunshop.com/firearms/handguns.html?p={i}'
    site = requests.get(url_pag, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')

    produtos = soup.find_all('div', class_=re.compile('product-item-info'))

    for produto in produtos:

        marca = produto.find('a', class_=re.compile(
            'product-item-link')).get_text().strip()
        price = produto.find('span', class_=re.compile(
            'price')).get_text().strip()

        index2 = price.find(' ')

        price = price[index2:].strip().replace('.', ',')

        dic_produtos['marca'].append(marca)
        dic_produtos['preco'].append(price)

    print(i)


df = pd.DataFrame(dic_produtos)

path = str(pathlib.Path().resolve())

df.to_csv(path + '/guns.csv',
          encoding='utf-8', sep=',')
