from .base_page import BasePage
from selenium.webdriver.common.by import By
from locators import LoginPageLocators

class LoginPage(BasePage):

    def send_login_text(self, text):
        login_field = self.find_element(LoginPageLocators.LOGIN_FIELD)
        login_field.send_keys(text)

    def send_password_keys(self, text):
        password_field = self.find_element(LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(text)

    def click_login_button(self):
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()



