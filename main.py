from time import sleep
import getpass
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from config import URL

usuario_facebook = input("Digite seu e-mail de acesso ao Facebook: ")
senha = getpass.getpass("Entre com a sua senha: ")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)
print(" - Abrindo o Facebook")
sleep(1)

campo_usuario = driver.find_element_by_id('email')
campo_usuario.send_keys(usuario_facebook)
print(" - Inserindo usuário no campo e-mail")
sleep(1)

campo_senha = driver.find_element_by_id('pass')
campo_senha.send_keys(senha)
print(" - Inserindo senha")


botao_login = driver.find_element_by_id('loginbutton')
botao_login.click()
print(" - Completando o acesso")
input(" - Pressione qualquer tecla para sair")
driver.quit()
print(" - Finalizado.")









