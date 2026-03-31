from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # открыть сайт авторизации
    def open_login_page(self):
        self.driver.get("https://www.saucedemo.com/")

    # авторизация
    def login(self, user_name, password):
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "user-name"))
        ).send_keys(user_name)

        self.driver.find_element(By.ID, "password").send_keys(password)

        self.driver.find_element(By.ID, "login-button").click()
