import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from lesson_10.pages.FormPage import FormPage
import allure

@pytest.fixture(scope="module")
def browser():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

@allure.title("Тест заполнения и отправки формы")
@allure.description("Проверка заполнения формы на сайте с проверкой успешного отправления")
@allure.feature("Форма")
@allure.severity(allure.severity_level.NORMAL)
def test_fill_and_submit_form(browser):
    form_page = FormPage(browser)

    with allure.step("Загрузка страницы формы"):
        form_page.load()

    with allure.step("Заполнение формы"):
        form_page.fill_first_name("Иван")
        form_page.fill_last_name("Петров")
        form_page.fill_address("Ленина, 55-3")
        form_page.fill_email("test@skypro.com")
        form_page.fill_phone_number("+7985899998787")
        form_page.fill_city("Москва")
        form_page.fill_country("Россия")
        form_page.select_job_position("QA")
        form_page.fill_company("SkyPro")

    with allure.step("Нажатие кнопки Submit"):
        form_page.submit_form()

    with allure.step("Проверка на наличие ошибки на поле Zip Code"):
        assert form_page.check_zip_code_error(), "Поле Zip Code должно быть подсвечено красным."

    with allure.step("Проверка правильности остальных полей"):
        other_fields_valid = browser.find_elements(By.CSS_SELECTOR, "input.valid")
        assert len(other_fields_valid) == 9, "Остальные поля должны быть подсвечены зеленым."

    with allure.step("Проверка успешного сообщения после отправки формы"):
        assert form_page.get_success_message_text() == "Success!", "Не удалось успешно отправить форму."