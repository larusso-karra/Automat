from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Шаг 1: Открыть страницу
driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")

# Шаг 2: Найти поле ввода и ввести текст 1000
input_field = driver.find_element(By.TAG_NAME, "input")
input_field.send_keys("1000")

# Шаг 3: Очистить поле
input_field.clear()

# Шаг 4: Ввести текст 999
input_field.send_keys("999")

sleep(5)