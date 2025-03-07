from selenium.webdriver.common.by import By


class Cart:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/cart.html")

    def checkout(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#checkout").click()