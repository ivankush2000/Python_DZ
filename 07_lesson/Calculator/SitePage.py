from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SitePage():
    def __init__(self, driver):
        self.driver = driver

    # Открыть сайт
    def open_main_page(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # установить задержку
    def set_delay(self):
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys("45")

    # Нажимаем кнопки: 7 + 8 =
    def click_on(self):
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

    # Ждем появления результата (до 50 секунд)
    def expectation(self):
        wait = WebDriverWait(self.driver, 50)
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"), "15")
        )

    # Проверяем итоговое значение
    def total_value(self):
        result_text = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        assert result_text == "15", f"Ожидалось 15, но получили {result_text}"
