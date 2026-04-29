import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class MainPage:
    """Класс для работы с главной страницей интернет-магазина."""
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Добавление товара в корзину и переход в корзину")
    def add_product(self):
        """Добавление товара в корзину и переход в корзину."""
        items_to_add = {
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie"
        }

        for item_id in items_to_add:
            self.driver.find_element(By.ID, item_id).click()

        self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link"
        ).click()
