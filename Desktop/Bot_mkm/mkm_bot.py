# Librerías necesarias para la ejecución del bot
    
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
# Para cargar el archivo de configuración
from dotenv import dotenv_values
# Para cargar otros scripts que no estén en la carpeta raíz

def load_user_credentials():
    '''Carga del archivo de configuración (como diccionario).'''

    config = dotenv_values('.env')
    print(config['CARD'])

    return config

### Operativa del bot

def bot_basics():
    '''Define el buscador a utilizar, la URL de la páginas a snippear y entra en la página.'''

    driver = webdriver.Firefox()

    url = "https://www.cardmarket.com/es/Magic"

    driver.get(url)

    return driver

def avoid_cookies(driver):

    '''Código para saltar las cookies que aparecen al poco tiempo después de entrar en la página, rechazándolo todo.'''

    time.sleep(1)
    cookie_settings = driver.find_element_by_class_name("modal-link")
    cookie_settings.click()
    time.sleep(1)
    close_icon = driver.find_element_by_class_name("btn-outline-primary")
    close_icon.click()
    time.sleep(1)

def login(driver, config):

    '''Código encargado de registrarse con el usuario y la contraseña proporcionados por el archivo .env'''
    
    # Introducimos el usuario y la contraseña (si se te abre en una ventana adyacente a las que ya tienes abiertas, dicha ventana deberá ser más ancha que alta para que funcione)
    user_input = driver.find_element_by_class_name('username-input')
    user_input.send_keys(config['USER']) 
    pass_input = driver.find_element_by_class_name('password-input')
    pass_input.send_keys(config['PASSWORD']) 
    # Iniciamos sesión 
    login_icon = driver.find_element_by_class_name("btn.AB-login-btn.btn-outline-primary.btn-sm")
    login_icon.click()
    # Buscamos la carta a snippear
    browser_input = driver.find_element_by_class_name('form-control.autocomplete-input')
    browser_input.send_keys(config['CARD'])
    search_icon = driver.find_element_by_class_name("fonticon-search")
    search_icon.click()

# Buscamos la edición para la que actualmente podemos encontrar el precio más bajo para esa carta y la seleccionamos (¿función externa?)

def stop_bot(driver):
    '''Cerramos el navegador'''
    time.sleep(5)
    driver.close()

def main():
    config = load_user_credentials()
    
    driver = bot_basics()
    avoid_cookies(driver)
    login(driver, config)
    
    stop_bot(driver)

