from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage(BasePage):
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def get_items_count(self) -> int:
        items = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.CART_ITEM))
        return len(items)
    
    def start_checkout(self):
        self.find_element(self.CHECKOUT_BUTTON).click()
    
