#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import csv
from datetime import date
import math


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

url_list = []

dic_notas = {}

Datas = []

today = date.today()

with open("C:/Users/lucas.costa/Desktop/Goal 2022/Reclame Aqui/Nova Lista Reclame Aqui.csv", "r") as arquivo:
    arquivo_csv_link = csv.reader(arquivo)

    for link in (arquivo_csv_link):
        up = str(link[0])
        url_list.append(up)
print(url_list)

n = len(url_list)


with open("C:/Users/lucas.costa/Desktop/Goal 2022/Reclame Aqui/Reclame11.csv", "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=";")


    for i in (arquivo_csv):

        test_num = i[0]


        if test_num == "":

            n_datas = len(i)-1

            for x in range(n_datas):

                 Datas.append(i[x+1])

with open("C:/Users/lucas.costa/Desktop/Goal 2022/Reclame Aqui/Reclame11.csv", "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=";")


    for y in range(n_datas):
        dic_notas[Datas[y]]=[]

    for j in (arquivo_csv):

        test = j[0]

        if test != "":
          for x in range(n_datas):
             
             f=j[x + 1]
             dic_notas[Datas[x]].append(f)


n_cias= (len(dic_notas['cias']))

print(n_cias)

dic_notas[today]=[]

for i in range(n):
   print(i)
   url = url_list[i]

   site = requests.get(url, headers=headers)
   soup = BeautifulSoup(site.content, 'html.parser')

   if i> n_cias-1:

       nome_comp = soup.find('div', class_=re.compile('jr2qk-15 cavUsr')).get_text().strip()
       dic_notas['cias'].append(nome_comp)
       # Esse dic_notas de baixo é pra deixar tudo no dicionario do mesmo tamanho. Da pra automatizar fazendo um for em dic_notas
       for l in range(n_datas):
           if l != 0:
              dic_notas[Datas[l]].append("")

   Nota = soup.find('span', class_='score').get_text().strip()
   Nota = Nota[:3]
   dic_notas[today].append(Nota)


print(dic_notas)

df = pd.DataFrame(dic_notas)
df.to_csv('C:/Users/lucas.costa/Desktop/Goal 2022/Reclame Aqui/Reclame11.csv', encoding='utf-8', sep=';')


# In[ ]:




