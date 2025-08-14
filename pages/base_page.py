import requests
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except Exception as e:
            raise Exception(f"Element not found: {locator}. Error: {e}")
        
    def get_api_status(self) -> int:
        response = requests.get("https://www.saucedemo.com/")
        return response.status_code