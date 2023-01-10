#!/usr/bin/env python
# coding: utf-8

# In[14]:


import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import csv
from datetime import date
import math
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()

options.add_argument('window-size=400,800')

navegador = webdriver.Chrome(options=options)

url_list = []

dic_notas = {}

Chaves = []

today = date.today()

#Cria a Lista de URLs a partir do excel de URLs

with open("C:/Users/lucas.costa/Desktop/Goal 2022/Glassdoor/Nova Lista Glass.csv", "r") as arquivo:
    arquivo_csv_link = csv.reader(arquivo,delimiter=";")
    
    for link in (arquivo_csv_link):
        up = str(link[0])
        url_list.append(up)
print(url_list)

n = len(url_list)


# In[15]:


#Cria a Lista de chaves (datas e cia) passadas a partir da primeira linha do arquivo principal

with open("C:/Users/lucas.costa/Desktop/Goal 2022/Glassdoor/Glassdoor.csv", "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=";")


    for i in (arquivo_csv):

        test_num = i[0]

        if test_num == "":

            n_chaves = len(i)-1

            for x in range(n_chaves):

                 Chaves.append(i[x+1])

    print(n_chaves)
    
#Constroi chaves do dicionario a partir da listas de Datas criada Passar esse for para cima do with

    for y in range(n_chaves):
        dic_notas[Chaves[y]]=[]
        
print(dic_notas)        


# In[16]:


#Constroi series das chaves do dicionario a partir das linhas a partir da segunda pra baixo do arquivo principal 

with open("C:/Users/lucas.costa/Desktop/Goal 2022/Glassdoor/Glassdoor.csv", "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=";")

    for j in (arquivo_csv):

        test = j[0]

        if test != "":
          for x in range(n_chaves):
             f=j[x + 1]
             dic_notas[Chaves[x]].append(f)

#mede numero de cias do dicionario contruido ate agora para comparar com lista de URL atualizada

n_cias= (len(dic_notas['cias']))

print(n_cias)


# In[17]:


#Cria nova chave do dia de hoje

dic_notas[today]=[]

print(dic_notas)


# In[18]:


#Preenche dados faltantes referente a data de hoje a novas empresas adicionadas

for i in range(n):
   print(i)
   url = url_list[i]
   print(url) 

   navegador.get(url)

   sleep(2)

   soup = BeautifulSoup(navegador.page_source, 'html.parser')

# Preenche novas linhas com empresas que ainda não estavam na planilha

   if i+1> n_cias:

       Nome = soup.find('span', class_='d-inline-flex align-items-center').get_text().strip() 
       dic_notas['cias'].append(Nome)
       # Esse dic_notas de baixo é pra deixar tudo no dicionario do mesmo tamanho. Da pra automatizar fazendo um for em dic_notas
       for l in range(n_chaves):
           if l != 0:
              dic_notas[Chaves[l]].append("")

# Preenche todas as notas da data de hoje                
                
   Nota = soup.find('div', class_='mr-xsm css-1c86vvj eky1qiu0').get_text().strip()
   print(Nota)
   #Nota = Nota[:3]
   dic_notas[today].append(Nota)

#.get_text().strip()

print(dic_notas)


# In[20]:


df = pd.DataFrame(dic_notas)
df.to_csv('C:/Users/lucas.costa/Desktop/Goal 2022/Glassdoor/Glassdoor.csv', encoding='utf-8', sep=';')


# In[ ]:




