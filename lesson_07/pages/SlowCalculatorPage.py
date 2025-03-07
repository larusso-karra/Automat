from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SlowCalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.seven_button = (By.XPATH, "//span[text()='7']")
        self.plus_button = (By.XPATH, "//span[text()='+']")
        self.eight_button = (By.XPATH, "//span[text()='8']")
        self.equals_button = (By.XPATH, "//span[text()='=']")
        self.result_element = (By.ID, "result")

    def set_delay(self, delay):
        delay_input = self.driver.find_element(*self.delay_input)
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_seven(self):
        self.driver.find_element(*self.seven_button).click()

    def click_plus(self):
        self.driver.find_element(*self.plus_button).click()

    def click_eight(self):
        self.driver.find_element(*self.eight_button).click()

    def click_equals(self):
        self.driver.find_element(*self.equals_button).click()

    def get_result(self):
           return WebDriverWait(self.driver, 60).until(
       EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.screen'), "15"))