import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Класс для работы со строницей авторизации."""
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открытие сайта авторизации интернет-магазина")
    def open_login_page(self):
        """Открывает сайт авторизации"""
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Выполнение авторизации подьзователя.")
    def login(self, user_name, password):
        """выполняет авторизацию пользователя:
            user_name: str - {user_name}
            password: str - {password}
        """
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "user-name"))
        ).send_keys(user_name)

        self.driver.find_element(By.ID, "password").send_keys(password)

        self.driver.find_element(By.ID, "login-button").click()
