#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import csv
from datetime import date
import math

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

url_list = []

dic_notas = {}

Datas = []

today = date.today()

# Cria a Lista de URLs a partir do excel de URLs

with open("C:/Users/lucas.costa/Desktop/Goal 2022/PlayStore/Nova Lista play.csv", "r") as arquivo:
    arquivo_csv_link = csv.reader(arquivo)

    for link in (arquivo_csv_link):
        up = str(link[0])
        url_list.append(up)
print(url_list)

n = len(url_list)


# In[2]:


# Cria a Lista de Datas (com 'cias')(mudar nome da variavel) passadas a partir da primeira linha do arquivo principal

with open("C:/Users/lucas.costa/Desktop/Goal 2022/PlayStore/PlayStore.csv", "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=";")

    for i in (arquivo_csv):

        test_num = i[0]

        if test_num == "":

            n_datas = len(i)-1

            for x in range(n_datas):

                Datas.append(i[x+1])

    print(n_datas)


# In[3]:


with open("C:/Users/lucas.costa/Desktop/Goal 2022/PlayStore/PlayStore.csv", "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=";")

# Constroi chaves do dicionario a partir da listas de Datas criada Passar esse for para cima do with

for y in range(n_datas):
    dic_notas[Datas[y]] = []

# Constroi series das chaves do dicionario a partir das linhas a partir da segunda pra baixo do arquivo principal

for j in (arquivo_csv):

    test = j[0]

    if test != "":
        for x in range(n_datas):
            f = j[x + 1]
            dic_notas[Datas[x]].append(f)

# mede numero de cias do dicionario contruido ate agora para comparar com lista de URL atualizada

n_cias = (len(dic_notas['cias']))

print(n_cias)


# Cria nova chave do dia de hoje

dic_notas[today] = []


# In[4]:


# Preenche dados faltantes referente a data de hoje a novas empresas adicionadas

for i in range(n):
    print(i)
    url = url_list[i]

    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')

# Preenche novas linhas com empresas que ainda não estavam na planilha

    if i > n_cias-1:

        nome_comp = soup.find('div', class_='Vbfug auoIOc').get_text().strip()
        dic_notas['cias'].append(nome_comp)
        # Esse dic_notas de baixo é pra deixar tudo no dicionario do mesmo tamanho. Da pra automatizar fazendo um for em dic_notas
        for l in range(n_datas):
            if l != 0:
                dic_notas[Datas[l]].append("")

# Preenche todas as notas da data de hoje

    Nota = soup.find('div', class_='TT9eCd').get_text().strip()
    Nota = Nota[:3]
    dic_notas[today].append(Nota)


print(dic_notas)


# In[ ]:


# TESTE
url = url_list[0]

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

print(soup)


# In[5]:


df = pd.DataFrame(dic_notas)
df.to_csv('C:/Users/lucas.costa/Desktop/Goal 2022/PlayStore/PlayStore.csv',
          encoding='utf-8', sep=';')


# In[ ]:
