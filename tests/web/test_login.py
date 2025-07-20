import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize("username, password, expected_error, expected_url", [
    ("invalid_user", "invalid_pass", "Epic sadface: Username and password do not match any user in this service", None),
    ("", "secret_sauce", "Epic sadface: Username is required", None),
    ("valid_user", "", "Epic sadface: Password is required", None),
    ("standard_user", "secret_sauce", None, "https://www.saucedemo.com/inventory.html")
])
def test_login_func(driver, username, password, expected_error, expected_url):
    login_page = LoginPage(driver)
    driver.get("https://www.saucedemo.com")

    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    if expected_error:
        assert login_page.get_error_message() == expected_error, f"Expected error message: {expected_error}"
    if expected_url:
        assert driver.current_url == expected_url, f"Expected URL: {expected_url}, but got {driver.current_url}"

