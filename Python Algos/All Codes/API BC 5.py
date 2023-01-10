#!/usr/bin/env python
# coding: utf-8

# In[8]:


#get_ipython().system('pip install requests')
import requests
import pandas as pd
import csv
import json


# In[9]:


lista_codigos = []
lista_nomes = []
lista_df = {}
Dic_inf = {}
Df_tot = pd.DataFrame()

with open("C:/Users/lucas.costa/Desktop/Goal 2022/BCB/CODBCB-Input.csv", "r") as arquivo:
    arquivo_csv_link = csv.reader(arquivo, delimiter=";")

    for link in (arquivo_csv_link):
        up = str(link[0])
        lista_nomes.append(up)
print(lista_nomes)
n = len(lista_nomes)
print(n)

with open("C:/Users/lucas.costa/Desktop/Goal 2022/BCB/CODBCB-Input.csv", "r") as arquivo:
    arquivo_csv_link = csv.reader(arquivo, delimiter=";")

    for link in (arquivo_csv_link):
        up = str(link[1])
        lista_codigos.append(up)
print(lista_codigos)


# In[10]:


for i in range(n):

    CODBC = lista_codigos[i]
    link = f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{CODBC}/dados?formato=json'
    requisição = requests.get(link)
    informacoes = requisição.json()

    Df_inf = pd.DataFrame(informacoes)
    Df_inf = Df_inf.set_index('data')
    print(lista_nomes[i])
   # display(Df_inf)

    Df_tot[lista_nomes[i]] = Df_inf['valor']

print(Df_tot)
# display(Df_tot)

# lista_df{'lista_nomes[i]'}=pd.DataFrame(informacoes)


# print(informacoes)
#import pprint
# pprint.pprint(informacoes)


# In[11]:


Df_tot.to_csv('C:/Users/lucas.costa/Desktop/Goal 2022/BCB/BCB SERIES-Output.csv',
              encoding='utf-8', sep=';')


# In[ ]:


# In[ ]:
