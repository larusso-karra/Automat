import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_calculator(browser):
    # Открыть страницу
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    browser.get(url)

    # Ввести задержку
    delay_input = browser.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # Нажать на кнопки калькулятора
    seven_button = browser.find_element(By.XPATH, "//span[text()='7']")
    plus_button = browser.find_element(By.XPATH, "//span[text()='+']")
    eight_button = browser.find_element(By.XPATH, "//span[text()='8']")
    equals_button = browser.find_element(By.XPATH, "//span[text()='=']")

    seven_button.click()
    plus_button.click()
    eight_button.click()
    equals_button.click()

    # Подождать 45 секунд и проверить результат
    result = WebDriverWait(browser, 46).until(
        EC.text_to_be_present_in_element((By.ID, "result"), "15")
    )

    assert result, "Результат вычисления должен быть равен 15."