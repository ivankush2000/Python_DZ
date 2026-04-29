import pytest
import allure
from selenium import webdriver
from LoginPage import LoginPage
from MainPage import MainPage
from CartPage import CartPage
from YourInfoPage import YourInfoPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver

    driver.quit()

@allure.feature("Интернет-магазин")
@allure.title("Тест оформления заказа в интернет-магазине")
@allure.description("""
    Тест проверяет полный сценарий покупки:
    1. Авторизация пользователя
    2. Добавление трех товаров в корзину
    3. Проверка наличия товаров в корзине
    4. Заполнение информации о покупателе
    5. Проверка итоговой суммы заказа
""")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_page(driver):
    """Тест-кейс: Покупка товаров в интернет-магазине"""
    
    with allure.step("1. Авторизация на сайте"):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.login("standard_user", "secret_sauce")

    with allure.step("2. Добавление товаров в корзину"):
        main_page = MainPage(driver)
        main_page.add_product()

    with allure.step("3. Проверка наличия товаров в корзине"):
        cart_page = CartPage(driver)
        items_in_cart = cart_page.get_item_names()
        expected_items = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]

        for item in expected_items:
            with allure.step(f"Проверка наличия товара: {item}"):
                assert item in items_in_cart, f"Товар {item} не найден в корзине!"

    with allure.step("4. Переход к оформлению заказа"):
        cart_page.click_checkout()

    with allure.step("5. Заполнение информации о покупателе"):
        your_info_page = YourInfoPage(driver)
        your_info_page.your_info("Иван", "Куш", "123456")

    with allure.step("6. Проверка итоговой суммы заказа"):
        actual_total_text = your_info_page.check()
        expected_total = "Total: $58.29"

        assert actual_total_text == expected_total, \
            f"Ошибка! Ожидалось {expected_total}, но получили {actual_total_text}"