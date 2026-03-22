from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()
    # Настройка явного ожидания (10 секунд)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.saucedemo.com/")

        # Авторизация
        username_field = wait.until(
            EC.element_to_be_clickable((By.ID, "user-name")))
        username_field.clear()
        username_field.send_keys("standard_user")

        password_field = driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys("secret_sauce")

        driver.find_element(By.ID, "login-button").click()

        # Добавление товаров в корзину
        items_to_add = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie"
        ]

        for item_id in items_to_add:
            driver.find_element(By.ID, item_id).click()

        # Переход в корзину и к оформлению
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

        # Заполнение данных пользователя
        driver.find_element(By.ID, "first-name").send_keys("Иван")
        driver.find_element(By.ID, "last-name").send_keys("Кушеев")
        driver.find_element(By.ID, "postal-code").send_keys("123456")

        driver.find_element(By.ID, "continue").click()

        # Проверка итоговой суммы
        total_element = wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label"))
        )
        actual_total_text = total_element.text
        expected_total = "Total: $58.29"

        print(f"Итоговая сумма в системе: {actual_total_text}")

        assert expected_total in actual_total_text, (
            f"Ошибка: Ожидалась сумма {expected_total}, но получена {actual_total_text}"
        )

    finally:
        driver.quit()


if __name__ == "__main__":
    test_shop()
