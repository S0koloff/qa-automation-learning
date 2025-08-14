import pytest
import allure
from pages.base_page import BasePage

@allure.feature("Status code")
def test_api_status(driver):
    base_page = BasePage(driver)
    assert base_page.get_api_status() == 200