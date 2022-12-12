from selenium import webdriver
from selenium.webdriver.common.by import By

# seteaza driverul
driver = webdriver.Chrome('chromedriver')

# Navigam catre un url
driver.get('https://phptravels.net/login')

#selector by ID
password_input = driver.find_element(By.CSS_SELECTOR, 'input[type="password"')
login_btn = driver.find_elent(By.CSS_SELECTOR)
password_input.send.keys("ceva")
