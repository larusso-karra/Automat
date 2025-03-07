import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_form(browser):
    # Открыть страницу
    url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    browser.get(url)

    # Заполнить форму
    first_name_input = browser.find_element(By.NAME, "firstName")
    last_name_input = browser.find_element(By.NAME, "lastName")
    address_input = browser.find_element(By.NAME, "address")
    email_input = browser.find_element(By.NAME, "email")
    phone_number_input = browser.find_element(By.NAME, "phoneNumber")
    city_input = browser.find_element(By.NAME, "city")
    country_input = browser.find_element(By.NAME, "country")
    job_position_select = browser.find_element(By.NAME, "jobPosition")
    company_input = browser.find_element(By.NAME, "company")

    first_name_input.send_keys("Иван")
    last_name_input.send_keys("Петров")
    address_input.send_keys("Ленина, 55-3")
    email_input.send_keys("test@skypro.com")
    phone_number_input.send_keys("+7985899998787")
    city_input.send_keys("Москва")
    country_input.send_keys("Россия")
    job_position_select.send_keys("QA")
    company_input.send_keys("SkyPro")

    submit_button = browser.find_element(By.XPATH, "//input[@value='Submit']")
    submit_button.click()

    # Проверить подсветку полей
    zip_code_error = browser.find_element(By.CSS_SELECTOR, "#zipCode.invalid")
    other_fields_valid = browser.find_elements(By.CSS_SELECTOR, "input.valid")

    assert zip_code_error.is_displayed(), "Поле Zip Code должно быть подсвечено красным."
    assert len(other_fields_valid) == 9, "Остальные поля должны быть подсвечены зеленым."