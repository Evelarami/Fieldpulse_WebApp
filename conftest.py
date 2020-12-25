import pytest
from selenium import webdriver

link = "https://webapp.fieldpulse.com/auth/login"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser")
    browser = webdriver.Chrome()
    browser.get(link)
    yield browser
    print("\nexit browser")
    browser.quit()