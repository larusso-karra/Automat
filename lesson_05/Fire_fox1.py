from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Шаг 1: Открыть страницу
driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/entry_ad")

# Шаг 2: Нажать на кнопку Close в модальном окне
close_button = driver.find_element(By.ID, "close")
close_button.click()

sleep(5)