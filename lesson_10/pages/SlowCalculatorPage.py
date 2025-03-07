from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class SlowCalculatorPage:
    """Этот класс представляет страницу калькулятора с задержкой и позволяет взаимодействовать с элементами калькулятора."""

    def __init__(self, driver):
        """
        Инициализирует объект страницы SlowCalculatorPage.

        Args:
            driver: объект драйвера Selenium (WebDriver), используемый для управления браузером.
        """
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.seven_button = (By.XPATH, "//span[text()='7']")
        self.plus_button = (By.XPATH, "//span[text()='+']")
        self.eight_button = (By.XPATH, "//span[text()='8']")
        self.equals_button = (By.XPATH, "//span[text()='=']")
        self.result_element = (By.ID, "result")

    def set_delay(self, delay):
        """
        Устанавливает значение задержки в поле ввода.

        Args:
            delay: целое число (int), задающее величину задержки перед выполнением операции.
        """
        delay_input = self.driver.find_element(*self.delay_input)
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_seven(self):
        """Кликает на кнопку '7'."""
        self.driver.find_element(*self.seven_button).click()

    def click_plus(self):
        """Кликает на кнопку '+'."""
        self.driver.find_element(*self.plus_button).click()

    def click_eight(self):
        """Кликает на кнопку '8'."""
        self.driver.find_element(*self.eight_button).click()

    def click_equals(self):
        """Кликает на кнопку '='."""
        self.driver.find_element(*self.equals_button).click()

    def get_result(self, delay):
        """
        Ожидает появления результата "15" на экране калькулятора.

        Args:
            delay:  Величина задержки, установленная в калькуляторе.

        Returns:
            bool: True, если результат появился в течение времени ожидания, False в противном случае.
        """
        wait_time = delay + 1  # Добавляем 1 секунду к задержке
        try:
            WebDriverWait(self.driver, wait_time).until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.screen'), "15")
            )
            return True  # Результат найден
        except TimeoutException:
            return False # Результат не найден за отведенное время
