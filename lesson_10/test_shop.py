import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from lesson_10.pages.Login import Login
from lesson_10.pages.Shop import Shop
from lesson_10.pages.Cart import Cart
from lesson_10.pages.Information import Information
from lesson_10.pages.Overview import Overview
import allure

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

@allure.title("Тест покупки в магазине SauceDemo")
@allure.description("Проверка процесса покупки, включая авторизацию, добавление товаров в корзину и проверку итоговой суммы.")
@allure.feature("Покупки")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_process(browser):
    with allure.step("Открытие сайта магазина"):
        browser.get("https://www.saucedemo.com/")

    login = Login(browser)

    with allure.step("Авторизация как standard_user"):
        login.autorization('standard_user', 'secret_sauce')

    shop = Shop(browser)

    with allure.step("Добавление товаров в корзину"):
        shop.add_to_cart()

    cart = Cart(browser)

    with allure.step("Переход в корзину и нажатие на Checkout"):
        cart.checkout()

    information = Information(browser)

    with allure.step("Заполнение формы данными"):
        information.fill_info("Constantine", "Belyakov", "199406")

    overview = Overview(browser)

    with allure.step("Чтение итоговой стоимости из страницы"):
        total = overview.total()

    with allure.step("Проверка, что итоговая сумма равна $58.29"):
        assert total == "$58.29", f"Ожидаемая сумма: $58.29, фактическая сумма: {total}"