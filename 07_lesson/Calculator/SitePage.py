from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SitePage:
    def __init__(self, driver):
        self.driver = driver

    # открыть сайт
    def open_main_page(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # установить задержку
    def set_delay(self, seconds="45"):
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(seconds)

    # нажимаем кнопки: 7 + 8 =
    def click_on(self):
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

    # ждем появления результата (до 50 секунд)
    def wait_for_result(self, expected_value, timeout=50):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"), expected_value)
        )

    # проверяем итоговое значение
    def get_total_value(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
