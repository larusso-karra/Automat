import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from lesson_08.pages.Login import Login
from lesson_08.pages.Shop import Shop
from lesson_08.pages.Cart import Cart
from lesson_08.pages.Information import Information
from lesson_08.pages.Overview import Overview

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

# Откройте сайт магазина: https://www.saucedemo.com/.
login = Login(driver)

# Авторизуйтесь как пользователь standard_user.

login.autorization('standard_user', 'secret_sauce')

# Добавьте в корзину товары:
# Sauce Labs Backpack.
# Sauce Labs Bolt T-Shirt.
# Sauce Labs Onesie.
shop = Shop(driver)
shop.add_to_cart()

# Перейдите в корзину.

cart = Cart(driver)

# Нажмите Checkout.
information = Information(driver)

# Заполните форму своими данными:
# имя,
# фамилия,
# почтовый индекс.
information.fill_info("Constantine", "Belyakov", 199406)

# Нажмите кнопку Continue.
overview = Overview(driver)

# Прочитайте со страницы итоговую стоимость (Total).
total = overview.total()

# Закройте браузер.
driver.close()

# Проверьте, что итоговая сумма равна $58.29.


def test_total():
    assert total == "$58.29"


driver.quit()