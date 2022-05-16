from sys import displayhook
from timeit import repeat
import pandas as pd
import time
import urllib

 # pip install openpyxl
contatos_df = pd.read_excel('C:\\Users\\Brendoge\\Desktop\\HarveProject\\contatos.xlsx')
print(contatos_df.head())

 # downlaod chromedriver no navegador
 # pip install selenium 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Chrome('C:\\Users\\Brendoge\\python\\lib\windows-i686/chromedriver')
navegador.get('https://web.whatsapp.com/')

while len(navegador.find_elements_by_id('side')) < 1:
    time.sleep(1)

#pós log feito no wppweb

for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i, 'Pessoa']
    numero = contatos_df.loc[i, 'Numero']
    texto = urllib.parse.quote(f'Oi {pessoa}! {mensagem}')
    link = f'https://web.whatsapp.com/send?phone={numero}&text={mensagem}'
    navegador.get(link)
    while len(navegador.find_elements_by_id('side')) < 1:
       time.sleep(1)
    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
    time.sleep(5)