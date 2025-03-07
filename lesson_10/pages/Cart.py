from selenium.webdriver.common.by import By


class Cart:
    """Этот класс управляет поведением корзины покупок на веб-сайте SauceDemo"""
    def __init__(self, driver):
        """объект драйвера Selenium (WebDriver), который используется для взаимодействия с браузером"""
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/cart.html")

    def checkout(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#checkout").click()