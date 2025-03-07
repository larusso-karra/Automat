from selenium.webdriver.common.by import By
class FormPage:
    def __init__(self, browser):
        self.browser = browser
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

    def __init__(self, browser):
        self.browser = browser

    # Локатор для проверки ошибки на поле Zip Code
    ZIP_CODE_ERROR_LOCATOR = (By.CSS_SELECTOR, "#zipCode.invalid")

    # Локатор для успешной отправки формы
    SUCCESS_MESSAGE_LOCATOR = (By.ID, "result")

    def load(self):
        """Метод загрузки страницы."""
        self.browser.get(self.url)

    def fill_first_name(self, first_name):
        """Метод ввода имени."""
        input_field = self.browser.find_element(By.NAME, "firstName")
        input_field.clear()
        input_field.send_keys(first_name)

    def fill_last_name(self, last_name):
        """Метод ввода фамилии."""
        input_field = self.browser.find_element(By.NAME, "lastName")
        input_field.clear()
        input_field.send_keys(last_name)

    def fill_address(self, address):
        """Метод ввода адреса."""
        input_field = self.browser.find_element(By.NAME, "address")
        input_field.clear()
        input_field.send_keys(address)

    def fill_email(self, email):
        """Метод ввода email."""
        input_field = self.browser.find_element(By.NAME, "email")
        input_field.clear()
        input_field.send_keys(email)

    def fill_phone_number(self, phone_number):
        """Метод ввода номера телефона."""
        input_field = self.browser.find_element(By.NAME, "phoneNumber")
        input_field.clear()
        input_field.send_keys(phone_number)

    def fill_city(self, city):
        """Метод ввода города."""
        input_field = self.browser.find_element(By.NAME, "city")
        input_field.clear()
        input_field.send_keys(city)

    def fill_country(self, country):
        """Метод ввода страны."""
        input_field = self.browser.find_element(By.NAME, "country")
        input_field.clear()
        input_field.send_keys(country)

    def select_job_position(self, job_position):
        """Метод выбора позиции."""
        select_field = self.browser.find_element(By.NAME, "jobPosition")
        select_field.clear()
        select_field.send_keys(job_position)

    def fill_company(self, company):
        """Метод ввода компании."""
        input_field = self.browser.find_element(By.NAME, "company")
        input_field.clear()
        input_field.send_keys(company)

    def submit_form(self):
        """Метод отправки формы."""
        submit_button = self.browser.find_element(By.XPATH, "//input[@value='Submit']")
        submit_button.click()

    def check_zip_code_error(self):
        """Проверяет наличие ошибки на поле Zip Code."""
        wait = WebDriverWait(self.browser, 10)
        return wait.until(
            EC.visibility_of_element_located(self.ZIP_CODE_ERROR_LOCATOR)
        ).is_displayed()

    def get_success_message_text(self):
        """Получаем текст сообщения успеха после отправки формы."""
        wait = WebDriverWait(self.browser, 10)
        return wait.until(
            EC.presence_of_element_located(self.SUCCESS_MESSAGE_LOCATOR)
        ).text