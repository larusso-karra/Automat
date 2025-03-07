from selenium.webdriver.common.by import By


class Information:
    """Этот класс предназначен для работы с формой ввода информации на сайте SauceDemo"""
    def __init__(self, driver):
        """объект драйвера Selenium (WebDriver), используемый для управления браузером"""
        self.driver = driver
        self.driver.get(
            "https://www.saucedemo.com/checkout-step-one.html")

    def fill_info(self, f_name, l_name, zip):
        """строка (string), содержащая имя"""
        self.driver.find_element(
            By.CSS_SELECTOR, "#first-name").clear()
        self.driver.find_element(
            By.CSS_SELECTOR, "#first-name").send_keys(f_name)
        """строка (string), содержащая фамилию"""
        self.driver.find_element(
            By.CSS_SELECTOR, "#last-name").clear()
        self.driver.find_element(
            By.CSS_SELECTOR, "#last-name").send_keys(l_name)
        """строка (string), содержащая почтовый индекс"""
        self.driver.find_element(
            By.CSS_SELECTOR, "#postal-code").clear()
        self.driver.find_element(
            By.CSS_SELECTOR, "#postal-code").send_keys(zip)

        self.driver.find_element(
            By.CSS_SELECTOR, "#continue").click()