from selenium.webdriver.common.by import By


class Overview:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/checkout-step-two.html")

    def total(self):
        totals = list((self.driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label").text).split(" ")
            )
        total = totals[1]
        return total