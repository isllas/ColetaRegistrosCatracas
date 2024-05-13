# Importando Blibliotecas
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# Configurações
catraca_url = "IP de Acesso"


# Configuração do ChromeDriver
chrome_options = webdriver.ChromeOptions()

# Execução em modo headless (sem interface gráfica)
#chrome_options.add_argument("--headless")   causa interagbilidade nos botões necessários
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--window-size=1920,1080")  # Definindo o tamanho da janela


# Inicializando o driver do Chrome
driver = webdriver.Chrome(options=chrome_options)

try:
    # Acessar a página da catraca
    driver.get(catraca_url)

    WebDriverWait(driver, 10)
    
    username_fields = driver.find_elements(By.CLASS_NAME, "form-control")

# Acessar o primeiro elemento
    primeiro_username = username_fields[0]

    primeiro_username.send_keys("USERNAME")

    WebDriverWait(driver, 10)

    # Preencher o campo de senha
    username_fields = driver.find_elements(By.CLASS_NAME, "form-control")
    segundo_username = username_fields[1]
    segundo_username.send_keys("PASSWORD")

    WebDriverWait(driver, 10)

    # Clicar no botão de envio
    submit_button = driver.find_element(By.CLASS_NAME, "btn-default-blue-dark")
    submit_button.click()
    
    # Navegar até a aba de registros    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "nav-link")))

    # Encontrar os elementos de "nav-link"
    registros_fields = driver.find_elements(By.CLASS_NAME, "nav-link")
    registros_field = registros_fields[1].click()
    


    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "btn-block"))).click()

    

    # Aguardar alguns segundos para garantir que o download seja concluído
    time.sleep(60)


except TimeoutException:
    print("Elementos de autenticação não encontrados ou página de registros não carregada. Verifique se os IDs estão corretos e se a página está carregando corretamente.")

finally:
    # Fechar o navegador
    driver.quit()
