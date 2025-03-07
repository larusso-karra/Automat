from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Шаг 1: Перейти на страницу
url = 'http://uitestingplayground.com/ajax'
driver = webdriver.Chrome()
driver.get(url)

# Шаг 2: Найти и нажать на синюю кнопку
button = driver.find_element(By.ID, 'ajaxButton')
button.click()

# Шаг 3: Получить текст из зеленой плашки
WebDriverWait(driver, 15).until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'bg-success')))
green_bar_text = driver.find_element(By.CLASS_NAME, 'bg-success').text

# Шаг 4: Вывести текст в консоль
print(green_bar_text)