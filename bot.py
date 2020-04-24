from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

# configurando chromedriver para heroku

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument = ("--headless")
chrome_options.add_argument = ("--disable-dev-shm-usage")
chrome_options.add_argument = ("--no-sandbox")
browser = webdriver.Chrome('/app/.chromedriver/bin/chromedriver', chrome_options=chrome_options)

print('configurado !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

site = browser.get('https://www.google.com.br')
print(site)

# dados do leilao e login
'''
id_leilao = 39569
login = 'LA 22K'
senha = '21466635'
print('tenho os dados')
# login

browser = webdriver.Chrome('/home/ggpedro/selenium/chromedriver')
browser.get('https://www.lance24h.com.br/Login.php')
select = browser.find_element_by_id('Log_Email')
select.click()
select.send_keys(login)
select = browser.find_element_by_id('Log_Senha')
select.click()
select.send_keys(senha)
select.send_keys(Keys.ENTER)
time.sleep(2)
print('fiz login')
# pagina do leilao

browser.get(f'https://www.lance24h.com.br/Detalhes.php?Codigo={id_leilao}')
print('estou rodando')

while browser.find_element_by_id(f'L_BotaoA_{id_leilao}').text == 'Lance':
    dez_s = browser.find_element_by_id(f'L_ContDown_1_{id_leilao}').text
    uni_s = browser.find_element_by_id(f'L_ContDown_2_{id_leilao}').text
    seg = int(dez_s + uni_s)

    if seg == 7:
        time.sleep(0.6)
        if seg == 7:
            botao = browser.find_element_by_id(f'L_BotaoA_{id_leilao}')
            botao.click()
            time.sleep(3)
            
        else:
            pass
    else:
        pass
    
browser.close'''