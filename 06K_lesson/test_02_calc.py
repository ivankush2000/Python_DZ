from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():
    driver = webdriver.Chrome()

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # Устанавливаем задержку
        delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")

        # Нажимаем кнопки: 7 + 8 =
        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()

        # Ждем появления результата (до 50 секунд)
        wait = WebDriverWait(driver, 50)
        wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15")
        )

        # Проверяем итоговое значение
        result_text = driver.find_element(By.CSS_SELECTOR, ".screen").text
        assert result_text == "15", f"Ожидалось 15, но получили {result_text}"

    finally:
        driver.quit()


if __name__ == "__main__":
    test_calc()
