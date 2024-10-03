import time
import pandas as pd  # Para manipular os dados do Excel
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pyperclip  # Para acessar o conteúdo da área de transferência (clipboard)

# Configurando o WebDriver automaticamente
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Acessa o site
driver.get("https://www.visuall.store/")

# Aguarda o carregamento da página
time.sleep(5)  # Aguardar 5 segundos para garantir o carregamento

# Localiza o botão "Special Characters" e clica nele
special_chars_button = driver.find_element(By.XPATH, '//div[@class="button deactived" and @title="Special Characters"]')
special_chars_button.click()

# Aguarda 2 segundos para carregar a interação
time.sleep(2)

# Carrega os contatos da planilha existente
contacts_df = pd.read_excel('./data/contacts_fictitious.xlsx')

# Loop para gerar e copiar 20 senhas
for i in range(len(contacts_df)):
    # Localiza o botão "Generate Password" e clica nele
    generate_password_button = driver.find_element(By.XPATH, '//button[@class="btn-gen"]')
    generate_password_button.click()

    # Aguarda 2 segundos para carregar a senha
    time.sleep(2)

    # Localiza o botão "Copy Password" e clica nele
    copy_password_button = driver.find_element(By.XPATH, '//button[@class="secondary-btn-v2"]')
    copy_password_button.click()

    # Aguarda 1 segundo antes de continuar
    time.sleep(1)

    # Pega a senha copiada do clipboard (área de transferência)
    password = pyperclip.paste()
    
    # Atribui a senha ao contato correspondente
    contacts_df.at[i, 'Password'] = password

    # Aguarda 1 segundo antes de gerar a próxima senha
    time.sleep(1)

# Fecha o navegador
driver.quit()

# Salva o DataFrame atualizado com as senhas na planilha
contacts_df.to_excel('./data/contacts_fictitious_with_passwords.xlsx', index=False)

print("As senhas foram geradas e salvas no arquivo contacts_fictitious_with_passwords.xlsx")
