import pytest
import allure
from selenium import webdriver
from SitePage import SitePage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.feature("Калькулятор")
@allure.story("Проверка сложения с задержкой")
@allure.title("Проверка вычисления 7 + 8 с задержкой 45 секунд")
@allure.description("""
Тест открывает страницу калькулятора, 
устанавливает задержку 45 секунд, нажимает 7+8=,
ожидает результат 15 и проверяет его.
""")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator_website(driver):
    calculator = SitePage(driver)

    with allure.step("Открыть главную страницу калькулятора"):
        calculator.open_main_page()

    with allure.step(f"Установить задержку = 45 секунд"):
        calculator.set_delay("45")

    with allure.step("Нажать кнопки 7, +, 8, ="):
        calculator.click_on()

    with allure.step("Ожидать появления результата '15' на экране"):
        calculator.wait_for_result("15")

    with allure.step("Получить итоговое значение с экрана"):
        result = calculator.get_total_value()

    with allure.step("Проверить, что результат равен 15"):
        assert result == "15", f"Ожидалось 15, но получили {result}"