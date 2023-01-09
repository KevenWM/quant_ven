from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import pathlib
from datetime import date
import csv

dic_modelos = {'data': [], 'marca': [], 'preco': []}

# Recupera dados que já estão salvos e joga no dicionário
try:
    with open("Scrapping Locadoras\carros_movida_0km.csv", "r") as arquivo:
        arquivo_csv = csv.reader(arquivo, delimiter=",")

        for i, linha in enumerate(arquivo_csv):

            if i == 0:
                pass
            else:
                dic_modelos['data'].append(linha[0])
                dic_modelos['marca'].append(linha[1])
                dic_modelos['preco'].append(linha[2])

except:
    print("File not found")

# Opções -> início selenium
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--headless")


# definindo o caminho do webdriver
driver = webdriver.Chrome(
    executable_path='Scrapping Locadoras\chromedriver.exe')

# Site a set acessado
driver.get("https://www.movidazerokm.com.br/")
driver.maximize_window()
time.sleep(1)

# Manipulando o campo de loja
elem = driver.find_element(By.ID, "searchInput")
elem.clear()
elem.send_keys("Fiat Argo")
time.sleep(1)
elem.send_keys(Keys.ENTER)
time.sleep(2)

elem2 = driver.find_element(By.CLASS_NAME, "button-options")
elem2.click()

time.sleep(1)

soup = BeautifulSoup(driver.page_source, 'html.parser')

time.sleep(1)
driver.close()

# Fechou o navegador
carros = soup.find_all('div', class_='card-prod-info')

for carro in carros:
    marca = carro.find('div', class_='card-prod-info-title').get_text().strip()
    price = carro.find('div', class_='text-none').get_text().strip()

    dic_modelos['marca'].append(marca)

    # limpar o preço
    price = price.replace('R$', '').replace('/mês*', '').replace('Â', '')

    dic_modelos['preco'].append(price.strip())

    # data
    today = date.today()

    dic_modelos['data'].append(today)


df = pd.DataFrame(dic_modelos)

path = str(pathlib.Path().resolve())

df.to_csv(path + '/Scrapping Locadoras/carros_movida_0km.csv',
          encoding='latin-1', sep=',', index=None)

print("Arquivo Gerado")

# finaliza
exit()
