from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SitePage:
    def __init__(self, driver):
        self.driver = driver

    def open_main_page(self):
        """Открывает главную страницу калькулятора."""
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, seconds="45"):
        """Устанавливает задержку перед вычислением."""
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(seconds)

    def click_on(self):
        """Выполняем нажатие на кнопки 7, +, 8, ="""
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

    def wait_for_result(self, expected_value, timeout=50):
        """Ожидаем появление предпологаемого результата = 50 сек."""
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"), expected_value)
        )

    def get_total_value(self):
        """Возвращает текущее значение с экрана калькулятора."""
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
