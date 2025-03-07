from selenium.webdriver.common.by import By


class Shop:
    """Этот класс управляет действиями на странице магазина на сайте SauceDemo"""
    def __init__(self, driver):
        """объект драйвера Selenium (WebDriver), используемый для управления браузером"""
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/inventory.html")

    def add_to_cart(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()