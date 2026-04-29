import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """Класс для работы со страницей корзины."""
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_item_names(self):
        """Получает список названий товаров в корзине"""
        items = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "inventory_item_name"))
        )
        return [item.text for item in items]

    @allure.step("Нажимает на кнопку для перехода к оформлению заказа")
    def click_checkout(self):
        """Нажимает на кнопку для перехода к оформлению заказа."""
        self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "checkout"))
        ).click()
