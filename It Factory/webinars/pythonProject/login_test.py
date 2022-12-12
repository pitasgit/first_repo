# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# maximizam fereastra
chrome.maximize_window()

# navigam catre un url
chrome.get('https://the-internet.herokuapp.com/login')

chrome.find_element(By.ID, 'username').send_keys('tomsmith')
chrome.find_element(By.ID,'password').send_keys('SuperSecretPassword!')
# cu sleep putem pune pauza de cateva secunde sa asteptam sa vedem si noi ceva
sleep(3)

chrome.close()
