from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inicializar o navegador
driver = webdriver.Chrome()  # Certifique-se de ter o chromedriver instalado

# Acessar o site fictício
driver.get("https://www.site-ficticio-dinostore.com/login")

# Preencher o formulário de login
driver.find_element(By.ID, "email").send_keys("teste@teste.com")
driver.find_element(By.ID, "senha").send_keys("senha123")
driver.find_element(By.ID, "btnLogin").click()

# Esperar resposta da página
time.sleep(3)

# Verificar se o login foi bem-sucedido
assert "Bem-vindo" in driver.page_source

# Encerrar o navegador
driver.quit()