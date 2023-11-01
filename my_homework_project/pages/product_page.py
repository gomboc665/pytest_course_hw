from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from data.full_data import PRODUCT_PAGE
import time

class ProductPage(BasePage):

    ADD_BUTTON = (By.ID, 'add-to-cart-button')
    REMOVE_BUTTON = (By.ID, 'remove-button')
    BASKET_BAG = (By.ID, 'shopping_cart_container')

    ITEM_TEXT = (By.XPATH, 'item-name')
    ITEM_IMAGE = (By.XPATH, 'item-name')

    def __init__(self, driver,  item_name):
        super().__init__(driver=driver, url=PRODUCT_PAGE)
        self.url = PRODUCT_PAGE
        self.item_name = item_name

    def get_add_button_locator(self):
        return f'add-to-cart-{self.item_name}'


    def get_remove_button_locator(self):
        return f'remove-{self.item_name}'

    def button_click(self,add=None,remove=None):
        button = ''
        if add:
            button = self.get_add_button_locator()
        if remove:
            button = self.get_remove_button_locator()
        self.find_element(by=By.ID,value=button).click()