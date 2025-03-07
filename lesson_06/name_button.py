from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Шаг 1: Перейти на сайт
url = 'http://uitestingplayground.com/textinput'
driver = webdriver.Chrome()
driver.get(url)

# Шаг 2: Ввести текст в поле ввода
input_field = driver.find_element(By.ID, 'newButtonName')
input_field.send_keys('SkyPro')

# Шаг 3: Нажать на синюю кнопку
button = driver.find_element(By.CSS_SELECTOR, '.btn-primary')
button.click()

# Шаг 4: Получить текст кнопки и вывести в консоль
WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.btn-primary'), 'SkyPro')
)
renamed_button_text = button.text

# Шаг 5: Вывести текст в консоль
print(renamed_button_text)