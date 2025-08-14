from .base_page import BasePage
from selenium.webdriver.common.by import By

class InventoryPage(BasePage):
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ADD_TO_CART_BUTTON = (By.XPATH, ".//button[contains(@id, 'add-to-cart')]")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def add_item_to_cart(self, item_name: str):
        item_cards = self.driver.find_elements(*self.INVENTORY_ITEM)
        for card in item_cards:
            name_element = card.find_element(*self.ITEM_NAME)
            if name_element.text == item_name:
                add_button = card.find_element(*self.ADD_TO_CART_BUTTON)
                add_button.click()

    def go_to_cart(self):
        self.find_element(self.CART_LINK).click()

    def get_cart_count(self) -> int:
        return int(self.find_element(self.CART_BADGE).text)

