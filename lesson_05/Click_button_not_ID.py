from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
driver.get('http://uitestingplayground.com/dynamicid/')

# Ищем синюю кнопку по классу btn-primary и сохраняем её в переменную
blue_button = driver.find_element(By.CSS_SELECTOR, '.btn-primary')

# Нажимаем на синюю кнопку
blue_button.click()


sleep(10)