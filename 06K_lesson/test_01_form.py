from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form():
    driver = webdriver.Edge()
    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        # Заполнение полей
        search_input = driver.find_element(By.CSS_SELECTOR, "[name=first-name]")
        search_input.send_keys("Иван")
        print("✅ First name: Иван")

        search_input = driver.find_element(By.CSS_SELECTOR, "[name=last-name]")
        search_input.send_keys("Петров")
        print("✅ Last name: Петров")

        search_input = driver.find_element(By.CSS_SELECTOR, "[name=address]")
        search_input.send_keys("Ленина, 55-3")
        print("✅ Address: Ленина, 55-3")

        search_input = driver.find_element(By.CSS_SELECTOR, "[name=e-mail]")
        search_input.send_keys("test@skypro.com")
        print("✅ Email: test@skypro.com")

        search_input = driver.find_element(By.CSS_SELECTOR, "[name=phone]")
        search_input.send_keys("+7985899998787")
        print("✅ Phone number: +7985899998787")

        search_input = driver.find_element(By.CSS_SELECTOR, "[name=zip-code]")
        search_input.send_keys("")
        print("✅ Zip code: (пусто)")

        search_input = driver.find_element(By.CSS_SELECTOR, "[name=city]")
        search_input.send_keys("Москва")
        print("✅ City: Москва")

        search_input = driver.find_element(By.CSS_SELECTOR, "[name=country]")
        search_input.send_keys("Россия")
        print("✅ Country: Россия")

        search_input = driver.find_element(By.CSS_SELECTOR, "[name=job-position]")
        search_input.send_keys("QA")
        print("✅ Job position: QA")

        search_input = driver.find_element(By.CSS_SELECTOR, "[name=company]")
        search_input.send_keys("SkyPro")
        print("✅ Company: SkyPro")

        # Нажатие кнопки
        driver.find_element(By.CSS_SELECTOR, "[type=submit]").click()

        # Проверка поля Zip-code (должно быть красным)
        zip_field = driver.find_element(By.ID, "zip-code").get_attribute("class")
        print(f"✅ Результат для Zip-code: {zip_field}")
        assert "alert-danger" in zip_field

        # Список полей для проверки на зеленый цвет
        fields = [
            "first-name",
            "last-name",
            "address",
            "e-mail",
            "phone",
            "city",
            "country",
            "job-position",
            "company"
        ]

        # Проверка всех остальных полей в цикле
        for item in fields:
            current_field = driver.find_element(By.ID, item).get_attribute("class")
            print(f"✅ Поле {item} имеет класс: {current_field}")
            # Assert теперь внутри цикла — проверяем каждое поле!
            assert "alert-success" in current_field

    finally:
        driver.quit()


if __name__ == "__main__":
    test_form()