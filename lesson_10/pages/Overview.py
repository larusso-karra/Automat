from selenium.webdriver.common.by import By


class Overview:
    """Этот класс работает с информацией на странице обзора заказа на сайте SauceDemo"""
    def __init__(self, driver):
        """объект драйвера Selenium (WebDriver), используемый для управления браузером"""
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/checkout-step-two.html")

    def total(self):
        totals = list((self.driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label").text).split(" ")
            )
        total = totals[1]
        """Возвращается строка (string), представляющая итоговую сумму заказа"""
        return total