import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options
from data.full_data import LOGIN, PASSWORD


@pytest.fixture(scope="module")
def chrome_options():
    options = Options()
    # options.add_argument('--window-size=100,100')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    return options

@pytest.fixture(scope="function")
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()
    

@pytest.fixture(scope="function") 
def driver_and_auth(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(LOGIN, PASSWORD)
    yield driver

