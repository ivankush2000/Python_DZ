from selenium import webdriver
from SitePage import SitePage


def test_calculator_website():
    driver = webdriver.Chrome()
    calculator = SitePage(driver)

    calculator.open_main_page()
    calculator.set_delay()
    calculator.click_on()
    calculator.expectation()
    calculator.total_value()

    driver.quit()
