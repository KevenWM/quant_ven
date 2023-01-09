import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
import openpyxl
import os
import numpy as np
import matplotlib.pyplot as plt
import csv
from datetime import datetime, timedelta

# Google Trends

webdriver = webdriver.Chrome(executable_path=r'C:\Users\diego.resende\Documents\Programação\Chromedriver\chromedriver.exe')
webdriver.get('https://trends.google.com.br/trends/explore?date=now%201-d&geo=BR&q=Instagram,TikTok,Youtube')
time.sleep(2)
webdriver.refresh()
time.sleep(2)
webdriver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div/md-content/div/div/div[1]/trends-widget/ng-include/widget/div/div/div/widget-actions/div/button[1]').click()
time.sleep(2)
webdriver.quit()
time.sleep(2)

#Média

data_instagram = []
data_tiktok = []
data_youtube = []

#Variáveis Úteis

data_x = 4
new_soma = 0
new_soma2 = 0
new_soma3 = 0

with open(r'C:\Users\diego.resende\Downloads\multiTimeline.csv', "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=",")

    for i, linha in enumerate(arquivo_csv):

       if len(linha) == data_x and i>2:

            data_instagram.append(linha[1])
            data_tiktok.append(linha[2])
            data_youtube.append(linha[3])


size_insta = len(data_instagram)
size_tiktok = len(data_tiktok)
size_youtube = len(data_youtube)

for i in data_instagram:

        new_soma = int(i) + new_soma

media_insta = float(new_soma/size_insta)

print(media_insta)

for i in data_tiktok:

        new_soma2 = int(i) + new_soma2

media_tiktok = float(new_soma2/size_tiktok)

print(media_tiktok)

for i in data_youtube:

        new_soma3 = int(i) + new_soma3

media_youtube = float(new_soma3/size_youtube)

print(media_youtube)

# Export
dia_anterior = datetime.now() - timedelta (1)
print(dia_anterior)
tabela_compilar = [dia_anterior,media_insta,media_tiktok,media_youtube]

df = pd.DataFrame(data = tabela_compilar)
df1 = df.transpose()
df1.rename(columns={0:'DATA',1:'INSTAGRAM',2:'TIKTOK',3:'YOUTUBE'}, inplace=True)

df1.to_excel('C:/Users/diego.resende/Downloads/dados_tratados.xlsx',
        encoding="latin-1", index=None)

tabela_Goal = pd.read_excel(r'C:\Users\diego.resende\Documents\Goal\Goal.xlsx')
tabela_df1 = pd.read_excel(r'C:\Users\diego.resende\Downloads\dados_tratados.xlsx')
tabela_Mestre = pd.concat([tabela_Goal, tabela_df1])
print(tabela_Mestre)
tabela_Mestre.to_excel(r'C:\Users\diego.resende\Documents\Goal\Goal.xlsx', index=False )


# Limpar base

os.remove(r'C:\Users\diego.resende\Downloads\multiTimeline.csv')
os.remove(r'C:\Users\diego.resende\Downloads\dados_tratados.xlsx')











































# Tratamento de dados

# tabela_Goal = pd.read_excel(r'C:\Users\diego.resende\Documents\Goal\Goal.xlsx')
# tabela_troca = pd.read_excel(r'C:\Users\diego.resende\Documents\Goal\troca.xlsx')
# time.sleep(1)
#
# tabela_troca.loc[:, 'Compilar'] = 0
# time.sleep(1)
# # tabela_troca = tabela_troca.drop(0, axis=0)
# # time.sleep(1)
# # tabela_troca = tabela_troca.drop('Unnamed: 0', axis=1)
# # time.sleep(1)
# media1 = tabela_troca.groupby(['Compilar']).mean()
# time.sleep(1)
# print(media1)
#
# excelWriterCompilar= pd.ExcelWriter(r'C:\Users\diego.resende\Documents\Goal\Media.xlsx')
# time.sleep(1)
# media1.to_excel(excelWriterCompilar)
# time.sleep(1)
# excelWriterCompilar.save()
# time.sleep(1)
#
# tabela_media = pd.read_excel(r'C:\Users\diego.resende\Documents\Goal\Media.xlsx')
# print(tabela_media)



# tabela_Mestre = pd.concat([tabela_troca, tabela_media])
# print(tabela_Mestre)
# time.sleep(2)
# tabela_Mestre.to_excel(r'C:\Users\diego.resende\Documents\Goal\Goal.xlsx', index=False )




#CSV para XLSX

# tabela_multiTimeline = pd.read_csv(r'C:\Users\diego.resende\Downloads\multiTimeline.csv')
# time.sleep(1)
# excelWriter= pd.ExcelWriter(r'C:\Users\diego.resende\Documents\Goal\troca.xlsx')
# time.sleep(1)
# tabela_multiTimeline.to_excel(excelWriter)
# time.sleep(1)
# excelWriter.save()
# time.sleep(1)



# tabela_troca.insert(4, 'Unnamed: 4', 0)
# time.sleep(1)
# tabela_troca.to_excel(r'C:\Users\diego.resende\Documents\Goal\troca.xlsx', index=False)



# tabela_multiTimeline.to_csv(r'C:\Users\diego.resende\Downloads\multiTimeline.csv', index=False)

# tabela_Mestre = pd.concat([tabela_Goal, tabela_multiTimeline])
# print(tabela_Mestre)
# time.sleep(2)
# tabela_Mestre.to_excel(r'C:\Users\diego.resende\Documents\Goal\Goal.xlsx', index=False )
# time.sleep(2)
# os.remove(r'C:\Users\diego.resende\Downloads\multiTimeline.csv')




#https://trends.google.com.br/trends/explore?date=now%201-d&geo=BR&q=Tiktok,Instagram,You%20tube
#/html/body/div[3]/div[2]/div/md-content/div/div/div[1]/trends-widget/ng-include/widget/div/div/div/widget-actions/div/button[1]/i
#//*[@id="input-254"]
#https://trends.google.com.br/trends/explore?geo=BR&q=Instagram,Tiktok,Youtube
#https://trends.google.com.br/trends/?geo=BR
#https://trends.google.com.br/trends/explore?q=Instagram&geo=BR

#webdriver.find_element(By.XPATH,'//*[@id="input-254"]').send_keys(Keys.RETURN + 'Instagram' + Keys.RETURN)
#time.sleep(2)
#webdriver.find_element(By.XPATH,'//*[@id="explorepage-content-header"]/explore-pills/div/button').send_keys(Keys.RETURN + 'Tiktok')
#time.sleep(2)
#webdriver.find_element(By.XPATH,'//*[@id="explorepage-content-header"]/explore-pills/div/button').send_keys(Keys.RETURN + 'Youtube' + Keys.RETURN)
#time.sleep(2)

# tabela_troca.insert(4, '=MÉDIA(B:B)', 0)
# time.sleep(1)
# tabela_multiTimeline.loc[:, 'INSTAGRAM'] = '=EXT.TEXTO(A2;G2+1;J2)'
# time.sleep(1)
# tabela_multiTimeline.loc[:, 'TIKTOK'] = '=EXT.TEXTO(A2;H2+1;K2)'
# time.sleep(1)
# tabela_multiTimeline.loc[:, 'YOUTUBE'] = '=DIREITA(A2;NÚM.CARACT(A2)-I2)'
# time.sleep(1)
# tabela_multiTimeline.loc[:, 'a'] = '=PROCURAR(",";A2)'
# time.sleep(1)
# tabela_multiTimeline.loc[:, 'b'] = '=PROCURAR(",";A2;G2+1)'
# time.sleep(1)
# tabela_multiTimeline.loc[:, 'c'] = '=PROCURAR(",";A2;H2+1)'
# time.sleep(1)
# tabela_multiTimeline.loc[:, 'd'] = '=H2-G2-1'
# time.sleep(1)
# tabela_multiTimeline.loc[:, 'e'] = '=I2-H2-1'
# time.sleep(2)
#print(tabela_multiTimeline)
#tabela_multiTimeline.to_excel(r'C:\Users\diego.resende\Documents\Goal\Goal.xlsx', index=False)