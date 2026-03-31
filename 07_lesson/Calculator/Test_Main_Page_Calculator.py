import pytest
from selenium import webdriver
from SitePage import SitePage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calculator_website(driver):
    calculator = SitePage(driver)

    calculator.open_main_page()
    calculator.set_delay("45")
    calculator.click_on()
    calculator.wait_for_result("15")

    result = calculator.get_total_value()
    assert result == "15", f"Ожидалось 15, но получили {result}"
