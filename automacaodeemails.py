from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Abrir o navegado
navegador = webdriver.Chrome()

# Acessar o navegador
navegador.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=170&ct=1738261090&rver=7.5.2211.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26cobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26culture%3dpt-br%26country%3dbr%26RpsCsrfState%3dece7d13f-2ad1-f1b7-2998-70d7e05e5414&id=292841&aadredir=1&whr=hotmail.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c")

#Colocar o navegador em tela cheia
navegador.maximize_window()

time.sleep(1)

# preencher login
navegador.find_element(by=By.ID, value="i0116").send_keys("leandro_m.dias@hotmail.com")

time.sleep(1)

botao_avancar=navegador.find_element(by=By.ID, value="idSIButton9")

botao_avancar.click()

time.sleep(1)

navegador.find_element(by=By.ID, value="i0118").send_keys("abc123")


botao_entrar=navegador.find_element(by=By.ID, value="idSIButton9")

botao_entrar.click()

time.sleep(1)
botao_aceitar=navegador.find_element(by=By.ID, value="acceptButton")

botao_aceitar.click()

time.sleep(10)


