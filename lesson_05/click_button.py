from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
driver.get('http://the-internet.herokuapp.com/add_remove_elements/')

# Ищем кнопку "Add Element" и сохраняем её в переменную
add_button = driver.find_element(By.XPATH, '//button[text()="Add Element"]')

# Цикл для пяти нажатий на кнопку "Add Element"
for i in range(5):
    # Нажатие на кнопку
    add_button.click()

# Ищем все элементы-кнопки с надписью "Delete" и сохраняем их в список
delete_buttons = driver.find_elements(By.XPATH, '//button[text()="Delete"]')

# Выводим количество найденных кнопок "Delete"
print(len(delete_buttons))


sleep(5)
