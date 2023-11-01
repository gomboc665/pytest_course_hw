from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from data.full_data import CART_PAGE
from data.locators import remove_button,checkout_button
import time


class CartPage(BasePage):
    remove_button = remove_button
    checkout_button = checkout_button

    def __init__(self, driver):
        super().__init__(driver, url=CART_PAGE)  

    # Добавьте методы для работы с элементами на странице корзины
    def get_cart_total(self):
        total_element = self.find_element(By.ID, 'cart-total')
        return total_element.text

    def proceed_to_checkout(self):
        self.click_element(By.ID, checkout_button)

    def remove_item_from_cart(self):
        self.click_element(By.XPATH, remove_button)

    
