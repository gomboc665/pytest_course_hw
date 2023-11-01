from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from abc import ABC, abstractmethod
from selenium import webdriver
from data.locators import burger_menu,logout_btn,reset_btn,shopping_badge
from selenium.webdriver.support import expected_conditions as EC

class BasePage(ABC):
    burger_menu = burger_menu
    logout_btn = logout_btn
    reset_btn = reset_btn
    shopping_badge = shopping_badge

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, timeout=10)
    
    def open(self):
        self.driver.get(self.url)

    def wait_for_element(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def find_element(self, by, value, timeout=10):
        return self.wait_for_element(by, value, timeout)

    def click_element(self, by, value, timeout=10):
        element = self.find_element(by, value, timeout)
        element.click()

    def send_keys_to_element(self, by, value, keys, timeout=10):
        element = self.find_element(by, value, timeout)
        element.send_keys(keys)

    def reset_and_logout(self):
        # Нажимаем на бургер-меню
        self.find_element(by=By.XPATH, value=burger_menu).click()
        time.sleep(2)
        # Нажимаем на элемент с ресетом
        reset_element = self.wait_for_element(by=By.XPATH, value=reset_btn)
        reset_element.click()
        logout_element = self.wait_for_element(by=By.XPATH, value=logout_btn)
        logout_element.click()

    def shopping_badge_element(self):
        return self.wait.until(
            EC.presence_of_element_located((By.XPATH, shopping_badge))
        )
