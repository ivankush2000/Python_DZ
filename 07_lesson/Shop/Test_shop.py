from selenium import webdriver
from LoginPage import LoginPage
from MainPage import MainPage
from CartPage import CartPage
from YourInfoPage import YourInfoPage


def test_shop_page():
    driver = webdriver.Firefox()

    log_in = LoginPage(driver)
    log_in.open_login_page()
    log_in.login("standard_user",
                 "secret_sauce"
                 )

    main_page = MainPage(driver)
    main_page.add_product()

    cart_page = CartPage(driver)
    items_in_cart = cart_page.get_item_names()
    expected_items = ["Sauce Labs Backpack",
                      "Sauce Labs Bolt T-Shirt",
                      "Sauce Labs Onesie"
                      ]
    for item in expected_items:
        assert item in items_in_cart, f"Товар {item} не найден в корзине!"
    cart_page.click_checkout()

    Your_info_page = YourInfoPage(driver)
    Your_info_page.your_info("Иван", "Куш", "123456")

    actual_total_text = Your_info_page.check()
    expected_total = "Total: $58.29"
    assert actual_total_text == expected_total, f"Ошибка! Ожидалось {expected_total}, но получили {actual_total_text}"

    driver.quit()
