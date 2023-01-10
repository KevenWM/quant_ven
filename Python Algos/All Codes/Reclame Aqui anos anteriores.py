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
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


url_list = []

dic_notas = {}

dic_notas['cias']=[]
dic_notas['2020']=[]
dic_notas['2021']=[]

# for y in range(n_datas):
#         dic_notas[Datas[y]]=[]

#Contruir lista de URLs

with open("C:/Users/lucas.costa/Desktop/Goal 2022/Reclame Aqui/Nova Lista Reclame Aqui.csv", "r") as arquivo:
    arquivo_csv_link = csv.reader(arquivo)

    for link in (arquivo_csv_link):
        up = str(link[0])
        url_list.append(up)
print(url_list)

n = len(url_list)


# with open("C:/Users/lucas.costa/Desktop/Goal 2022/Reclame Aqui/Reclame11.csv", "r") as arquivo:
#     arquivo_csv = csv.reader(arquivo, delimiter=";")

#     for j in (arquivo_csv):

#         test = j[0]

#         if test != "":
#           for x in range(3):
             
#              f=j[x + 1]
#              dic_notas[x].append(f)


# n_cias= (len(dic_notas['cias']))

# print(n_cias)

# dic_notas[today]=[]

options = Options()

options.add_argument('window-size=400,800')

navegador = webdriver.Chrome(options=options)

for i in range(n):
   print(i)
   url = url_list[i]

   navegador.get(url)

   sleep(10)

   try:
       button21 = WebDriverWait(navegador, 10).until(
           EC.presence_of_element_located((By.XPATH, '//button[@id="reputation-tab-3"]'))
       )
   except:
       print("Erro ao selecionar o elemento button")
    
   print(button21)
 
#    ActionChains(navegador).move_to_element(button21).perform()

#    navegador.execute_script('arguments[0].scrollIntoView(true);', button21)

   button21.click()

   soup = BeautifulSoup(navegador.page_source, 'html.parser')

#    if i> n_cias-1:

#        nome_comp = soup.find('div', class_=re.compile('jr2qk-15 cavUsr')).get_text().strip()
#        dic_notas['cias'].append(nome_comp)

   #nome_comp = soup.find('div', class_=re.compile('jr2qk-15 cavUsr')).get_text().strip()
   dic_notas['cias'].append(url)

   Nota = soup.find('span', class_='score').get_text().strip()
   Nota = Nota[:3]
   dic_notas['2021'].append(Nota)
    
   try:
       button21 = WebDriverWait(navegador, 10).until(
           EC.presence_of_element_located((By.XPATH, '//button[@id="reputation-tab-4"]'))
       )
   except:
       print("Erro ao selecionar o elemento button")
    
   print(button21)    

   button21.click()

   soup = BeautifulSoup(navegador.page_source, 'html.parser')

   Nota = soup.find('span', class_='score').get_text().strip()
   Nota = Nota[:3]
   dic_notas['2020'].append(Nota)

    

print(dic_notas)

df = pd.DataFrame(dic_notas)
df.to_csv('C:/Users/lucas.costa/Desktop/Goal 2022/Reclame Aqui/ReclameAnos.csv', encoding='utf-8', sep=';')


# In[ ]:




