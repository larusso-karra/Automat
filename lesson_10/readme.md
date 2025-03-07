# Тесты Selenium с использованием Pytest и Allure

Этот проект содержит автоматизированные тесты Selenium, разработанные с использованием pytest и allure для создания отчетов о тестировании.

## Обзор

Проект включает в себя следующие тесты:

*   **Тест для формы**: Проверяет заполнение и отправку веб-формы с валидацией полей.
*   **Тест для магазина**:  Эмулирует процесс покупки в онлайн-магазине, включая авторизацию, добавление товаров в корзину и проверку итоговой суммы.
*   **Тест для калькулятора**: Проверяет функциональность веб-калькулятора с искусственной задержкой.

## Предварительные требования

Убедитесь, что у вас установлены следующие программы и библиотеки:

*   Python 3.7+
*   [pip](https://pip.pypa.io/en/stable/installation/) (менеджер пакетов Python)
*   [Google Chrome](https://www.google.com/chrome/) (или другой поддерживаемый браузер)
*   [ChromeDriver](https://chromedriver.chromium.org/downloads) (должен соответствовать вашей версии Chrome, хотя `webdriver-manager` должен автоматически устанавливать его)

## Как подключить Allure к проекту

1. Откройте сайт pypi, раздел allure-pytest.
2. Скопируйте команду для подключения:
pip install allure-pytest
3. Откройте терминал и перейдите к рабочей директории (lesson_10):
cd lesson 10 (или указать путь к необходимой папке)
4. Подключите Allure:
pip install allure-pytest
5. Команда ниже запускает Allure и конвертирует результаты теста в отчет:
allure serve allure-result
## Чтобы терминал распознал команду allure, установите Allure Report.

- Пользователи macOS: запустите в терминале VS Code команду
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Затем команду
brew install allure

- Пользователи Windows: запустите в терминале VS Code команду
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression

- Затем команду
scoop install allure

## Запуск тестов

Чтобы запустить тесты и сгенерировать отчет Allure, выполните следующую команду:

bash
pytest --alluredir=allure-results


Эта команда запустит все тесты в вашем проекте и сохранит результаты в формате, необходимом для Allure, в директорию `allure-results`.

## Просмотр отчета Allure

После запуска тестов создайте отчет Allure HTML, выполнив следующую команду:

bash
allure serve allure-results


Эта команда запустит локальный веб-сервер и откроет отчет Allure в вашем браузере.  Вы сможете просмотреть подробные результаты тестов, включая шаги, вложения и другую полезную информацию.

## Структура проекта

.
├── lesson_10/                 # Директория с файлами тестов
│   ├── FormPage_test.py       # Тест для формы
│   ├── test_shop.py       # Тест для магазина
│   ├── test_slow_calculator.py # Тест для калькулятора
│   └── …
├── pages/                 # Директория с Page Object
│   ├── FormPage.py
│   ├── Login.py
│   ├── Shop.py
│   ├── Cart.py
│   ├── Information.py
│   ├── Overview.py
│   └── SlowCalculatorPage.py
├── README.md              # Этот файл


## Зависимости

В проекте используются следующие основные библиотеки:

*   **pytest**:  Фреймворк для запуска тестов на Python.
*   **selenium**:  Инструмент для автоматизации браузера.
*   **webdriver-manager**: Библиотека для автоматического управления драйверами браузеров (ChromeDriver, GeckoDriver и т.д.).
*   **allure-pytest**: Плагин pytest для интеграции с Allure Framework.

## Дополнительная информация

*   [Документация pytest](https://docs.pytest.org/en/stable/)
*   [Документация Selenium](https://www.selenium.dev/documentation/)
*   [Документация Allure Framework](https://docs.qameta.io/allure/)

## Лицензия

[Укажите здесь лицензию вашего проекта]