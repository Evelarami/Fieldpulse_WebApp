from pages.login_page import LoginPage
import time

def test_user_can_login(browser):
    page = LoginPage(browser)
    page.send_login_text("reloxes@hotmail.com")
    page.send_password_keys("qwerty")
    time.sleep(10)