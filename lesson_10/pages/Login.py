from selenium.webdriver.common.by import By


class Login:
    """Этот класс предназначен для авторизации на сайте SauceDemo"""
    def __init__(self, driver):
        """объект драйвера Selenium (WebDriver), используемый для управления браузером"""
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")

    def autorization(self, user_name, password):
        """строка (string), содержащая имя пользователя"""
        self._driver.find_element(
            By.CSS_SELECTOR, "#user-name").clear()
        self._driver.find_element(
            By.CSS_SELECTOR, "#user-name").send_keys(user_name)
        """строка (string), содержащая пароль"""
        self._driver.find_element(
            By.CSS_SELECTOR, "#password").clear()
        self._driver.find_element(
            By.CSS_SELECTOR, "#password").send_keys(password)
        self._driver.find_element(
            By.CSS_SELECTOR, "#login-button").click()