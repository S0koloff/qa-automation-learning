import pytest
from playwright.sync_api import Page, expect

@pytest.mark.parametrize("username, password, product_name",
                         [("standard_user", "secret_sauce", "Sauce Labs Backpack")])
def test_add_item_to_cart_pw(page: Page, db_connection, username, password, product_name):
    page.goto("https://www.saucedemo.com")
    page.locator("#user-name").fill(username)
    page.locator("#password").fill(password)
    page.locator("#login-button").click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    productItem = page.locator('[data-test="inventory-item"]').filter(
        has=page.locator(f'[data-test="inventory-item-name"]:has-text("{product_name}")'))
    
    productItem.locator('[data-test^="add-to-cart-"]').click()

    #анстройки для заказа
    productItemId = 10101
    user_id = 1

    card_badge = page.locator(".shopping_cart_badge")
    expect(card_badge).to_have_text("1")

    cursor = db_connection.cursor()

    cursor.execute(f"""
        INSERT INTO orders (user_id, product_id, status)
        VALUES (%s, %s, 'pending')
    """, (user_id, productItemId))
    db_connection.commit()

    with cursor:
        cursor.execute("""
            SELECT order_id FROM orders
            WHERE user_id = %s AND product_id = %s
        """, (user_id, productItemId))

        result = cursor.fetchone()

        if result:
            order_id = result[0]
            print(f"Found order with id: {order_id}")
            assert True
        else:
            print("Order not found")
            assert False