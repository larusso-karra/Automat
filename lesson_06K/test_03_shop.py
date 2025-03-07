import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def browser():
    # Запускаем браузер
    driver = webdriver.Chrome()
    yield driver
    # Закрываем браузер после завершения тестов
    driver.quit()


@pytest.mark.parametrize(
    "username, password",
    [
        ("standard_user", "secret_sauce"),
    ],
)
def test_purchase(browser, username, password):
    # Открыть сайт магазина
    browser.get("https://www.saucedemo.com/")

    # Авторизация
    input_username = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "user-name"))
    )
    input_password = browser.find_element(By.ID, "password")
    button_login = browser.find_element(By.ID, "login-button")

    input_username.send_keys(username)
    input_password.send_keys(password)
    button_login.click()

    # Проверяем успешность входа
    assert "Products" in browser.title

    # Добавляем товары в корзину
    add_backpack = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='inventory_item_name' and text()='Sauce Labs Backpack']/ancestor::div[@class='inventory_item']//button"))
    )
    add_tshirt = browser.find_element(By.XPATH, "//div[@class='inventory_item_name' and text()='Sauce Labs Bolt T-Shirt']/ancestor::div[@class='inventory_item']//button")
    add_onesie = browser.find_element(By.XPATH, "//div[@class='inventory_item_name' and text()='Sauce Labs Onesie']/ancestor::div[@class='inventory_item']//button")

    add_backpack.click()
    add_tshirt.click()
    add_onesie.click()

    # Перейти в корзину
    cart_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
    )
    cart_button.click()

    # Нажать Checkout
    checkout_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='btn_action checkout_button']"))
    )
    checkout_button.click()

    # Заполнить форму
    first_name_input = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "first-name"))
    )
    last_name_input = browser.find_element(By.ID, "last-name")
    postal_code_input = browser.find_element(By.ID, "postal-code")
    continue_button = browser.find_element(By.XPATH, "//input[@value='CONTINUE']")

    first_name_input.send_keys("John")
    last_name_input.send_keys("Doe")
    postal_code_input.send_keys("12345")
    continue_button.click()

    # Прочитать итоговую сумму
    total_price = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    ).text

    # Проверить, что итоговая сумма равна $58.29
    assert total_price == "$58.29"