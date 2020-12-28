from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPageLocators:
    LOGIN_FIELD = BasePage.find_element(By.CSS_SELECTOR, "#icon-email")
    PASSWORD_FIELD = BasePage.find_element(By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = BasePage.find_element(By.CSS_SELECTOR, ".btn.waves-effect")
    RESET_PASSWORD_BUTTON = BasePage.find_element(By.CSS_SELECTOR, ".btn-flat")
