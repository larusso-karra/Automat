from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Шаг 1: Открыть страницу
driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

# Шаг 2: Ввести значение tomsmith в поле username
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("tomsmith")

# Шаг 3: Ввести значение SuperSecretPassword! в поле password
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")

# Шаг 4: Нажать кнопку Login
login_button = driver.find_element(By.CLASS_NAME, "radius")
login_button.click()

sleep(5)