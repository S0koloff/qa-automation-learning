import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@allure.feature("Корзина покупок")
def test_add_item_to_cart(driver):
    with allure.step("authorization"):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()
    
    with allure.step("Add item to cart"):
        inventory_page = InventoryPage(driver)
        inventory_page.add_item_to_cart("Sauce Labs Bike Light")
        inventory_page.add_item_to_cart("Sauce Labs Onesie")
        
        assert inventory_page.get_cart_count() == 2, f"Expected count: 2 \nCount: {inventory_page.get_cart_count()}"

    with allure.step("Go to cart"):
        inventory_page.go_to_cart()

    with allure.step("Start checkout"):
        cart_page = CartPage(driver)
        cart_page.start_checkout()