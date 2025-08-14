from .base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, "//div[contains(@class, 'error-message-container')]")

    def enter_username(self, username: str):
        self.find_element(self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password: str):
        self.find_element(self.PASSWORD_INPUT).send_keys(password)
    
    def click_login(self):
        self.find_element(self.LOGIN_BUTTON).click()

    def get_error_message(self):
        return self.find_element(self.ERROR_MESSAGE).text
    
    def open(self):
        self.driver.get("https://www.saucedemo.com/")