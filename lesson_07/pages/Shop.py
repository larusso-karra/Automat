from selenium.webdriver.common.by import By


class Shop:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/inventory.html")

    def add_to_cart(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()