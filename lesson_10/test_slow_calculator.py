import pytest
from selenium import webdriver
from lesson_10.pages.SlowCalculatorPage import SlowCalculatorPage
import allure

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.title("Тест калькулятора с задержкой")
@allure.description("Проверка работы калькулятора с задержкой на странице")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator(browser):
    # Открыть страницу
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    with allure.step("Загрузка страницы калькулятора"):
        browser.get(url)

    calculator_page = SlowCalculatorPage(browser)

    with allure.step("Установка задержки"):
        calculator_page.set_delay("60")

    with allure.step("Нажатие на кнопку 7"):
        calculator_page.click_seven()

    with allure.step("Нажатие на кнопку +"):
        calculator_page.click_plus()

    with allure.step("Нажатие на кнопку 8"):
        calculator_page.click_eight()

    with allure.step("Нажатие на кнопку ="):
        calculator_page.click_equals()

    with allure.step("Проверка результата"):
        result = calculator_page.get_result()
        assert result, "Результат вычисления должен быть равен 15."