import pytest
from selenium import webdriver
from lesson_08.pages.SlowCalculatorPage import SlowCalculatorPage

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_calculator(browser):
    # Открыть страницу
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    browser.get(url)

    calculator_page = SlowCalculatorPage(browser)

    # Ввести задержку
    calculator_page.set_delay("60")

    # Нажать на кнопки калькулятора
    calculator_page.click_seven()
    calculator_page.click_plus()
    calculator_page.click_eight()
    calculator_page.click_equals()

    # Проверить результат
    result = calculator_page.get_result()
    assert result, "Результат вычисления должен быть равен 15."