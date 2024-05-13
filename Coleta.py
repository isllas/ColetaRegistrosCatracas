# Importando Blibliotecas
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import shutil
import os
from datetime import datetime
import sys


# Configurações
catraca_url = "acesso à catraca"


# Configuração do ChromeDriver
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")  # Execução em modo headless (sem interface gráfica)
#chrome_options.add_argument("--start-minimized")
#chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-web-security")





# Inicializando o driver do Chrome
driver = webdriver.Chrome(options=chrome_options)

try:
    # Acessar a página da catraca
    driver.get(catraca_url)

    WebDriverWait(driver, 10)
    
    username_fields = driver.find_elements(By.CLASS_NAME, "form-control")

# Acessar o primeiro elemento
    primeiro_username = username_fields[0]

    primeiro_username.send_keys("login")

    WebDriverWait(driver, 10)

    # Preencher o campo de senha
    username_fields = driver.find_elements(By.CLASS_NAME, "form-control")
    segundo_username = username_fields[1]
    segundo_username.send_keys("senha")

    WebDriverWait(driver, 10)

    # Clicar no botão de envio
    submit_button = driver.find_element(By.CLASS_NAME, "btn-default-blue-dark")
    submit_button.send_keys(Keys.ENTER)
    
    # Navegar até a aba de registros    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "nav-link")))

    # Encontrar os elementos de "nav-link"
    registros_fields = driver.find_elements(By.CLASS_NAME, "nav-link")
    registros_field = registros_fields[1]
    registros_field.send_keys(Keys.ENTER)
    

    #Fazendo o dowload dos registros
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "btn-block"))).send_keys(Keys.ENTER)

    

    # Aguardar alguns segundos para garantir que o download seja concluído
    time.sleep(60)


except TimeoutException:
    print("Elementos de autenticação não encontrados ou página de registros não carregada. Verifique se os IDs estão corretos e se a página está carregando corretamente.")

finally:
    # Fechar o navegador
    driver.quit()

# Obter a data atual
data_atual = datetime.now()

# Formatar a data no formato desejado para o nome do arquivo
nome_arquivo = data_atual.strftime("Bilhetes %Y-%m-%d") + ".txt"  # Por exemplo, "Bilhetes 2024-05-09.txt"

#Move o arquivo baixado para pasta de acesso do Sênior

# Especifique o caminho do arquivo baixado e o destino para mover o arquivo
caminho_origem = "local/destino/bilhetes.txt"
caminho_destino = "Pasta/Destino"

# Verifica se o diretório de destino existe, se não, cria o diretório
if not os.path.exists(caminho_destino):
    os.makedirs(caminho_destino)

# Move o arquivo para o destino com o novo nome
shutil.move(caminho_origem, os.path.join(caminho_destino, nome_arquivo))

print("Arquivo movido com sucesso!")

time.sleep(5)
sys.exit()
