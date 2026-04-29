import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class YourInfoPage:
    """Класс для работы со страницей ввода информации о покупателе"""
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Корректный ввод поля:")
    def your_info(self, first_name, last_name, postal_code):
        """Заполняет форму с информацией о покупателе и переходит к оплате
            first_name: str - имя покупателя
            last_name: str - фамилия покупателя
            postal_code: str - почтовый индекс
        """
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

        self.driver.find_element(By.ID, "continue").click()

    @allure.step("Проверяем итоновую сумму заказа")
    def check(self):
        """Получает итоговую сумму заказа
            str - текст с итоговой суммой (например, "Total: $58.29")
        """
        total_element = self.wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label"))
        )
        
        return total_element.text
