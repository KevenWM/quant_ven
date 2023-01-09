from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


dic_modelos = {'marca': [], 'preco promo': [], 'preco standard': []}


# Options
options = webdriver.ChromeOptions()
options.headless = True  # running in headless mode
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)


# definindo o caminho do webdriver
driver = webdriver.Chrome(
    executable_path='Scrapping Locadoras\chromedriver.exe')

# Site a set acessado
driver.get("https://www.localiza.com/brasil/pt-br")
driver.maximize_window()
time.sleep(1)

# Manipulando o campo de loja
elem = driver.find_element(By.ID, "mat-input-1")
elem.clear()
elem.send_keys("Agencia Centro Savassi")
time.sleep(2)
elem.send_keys(Keys.TAB)
elem.send_keys(Keys.ENTER)
time.sleep(1)

# fecha o quadrado

elem2 = driver.find_elements(
    By.CLASS_NAME, 'mat-calendar-body-cell-content')


for i in elem2:
    dia = i.text

    if dia == "30":
        diacerto = i
        break

diacerto.click()

time.sleep(2)


# hora
elem3 = driver.find_elements(
    By.CLASS_NAME, 'mat-focus-indicator')

for k in elem3:
    hora = k.text

    if hora == "15:00":
        horacerta = k
        elem.send_keys(Keys.ENTER)
        break

horacerta.click()

time.sleep(2)

elem4 = driver.find_elements(
    By.CLASS_NAME, 'mat-calendar-body-cell-content')


for j in elem4:
    dia2 = j.text

    if dia2 == "30":
        j.click()

time.sleep(2)

elem5 = driver.find_elements(
    By.CLASS_NAME, 'mat-focus-indicator')

for k in elem5:
    hora2 = k.text

    if hora2 == "16:00":
        horacerta2 = k
        break

horacerta2.click()

time.sleep(2)


# botão libera

elem6 = driver.find_element(
    By.CLASS_NAME, 'cdk-overlay-container')

elem6.click()

time.sleep(2)

# botão FINAL

elem7 = driver.find_element(
    By.CLASS_NAME, 'ds-button--primary')

elem7.click()

time.sleep(10)
### --- PASSEI DE FASE ---###

# SCROLL ATÉ O FINAL

SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# PEGAR NOMES

elem8 = driver.find_elements(
    By.CLASS_NAME, 'ds-car-group-text__model-name')

elem9 = driver.find_elements(
    By.CLASS_NAME, 'tarifas__preco')

for n in elem8:
    print(n.text)

for k in elem9:
    print(k.text)
