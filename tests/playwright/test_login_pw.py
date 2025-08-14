import pytest
from playwright.sync_api import Page, expect

@pytest.mark.parametrize("username, password", 
                        [("standard_user", "secret_sauce")])
def test_login(page: Page, username, password):
    page.goto("https://www.saucedemo.com")
    page.locator("#user-name").fill(username)
    page.locator("#password").fill(password)
    page.locator("#login-button").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
