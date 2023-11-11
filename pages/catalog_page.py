from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from data.full_data import CATALOG_PAGE
import time

class CatalogPage(BasePage):

    ADD_BUTTON = (By.ID, 'add-to-cart-button')
    REMOVE_BUTTON = (By.ID, 'remove-button')
    BASKET_BAG = (By.ID, 'shopping_cart_container')

    ITEM_TEXT = (By.XPATH, 'item-name')
    ITEM_IMAGE = (By.XPATH, 'item-name')

    def __init__(self, driver,  item_name):
        super().__init__(driver=driver, url=CATALOG_PAGE)
        self.url = CATALOG_PAGE
        self.item_name = item_name

    def get_add_button_locator(self):
        return f'add-to-cart-{self.item_name}'

    def get_remove_button_locator(self):
        return f'remove-{self.item_name}'

    def find_element_by_item_name(self,by,timeout=10):
        return self.wait_for_element(by=by, value=self.item_name, timeout=10)
    
    def find_elements_by_class(self, path_value: str, element_name: str):
        # Найти и вернуть список элементов с заданным классом
        elements = self.driver.find_elements(By.XPATH, f'//{element_name}[@class="{path_value}"]')
        return elements

    def get_attribute_values(self, elements, attribute):
        # Получить атрибуты заданных элементов
        item_names = [element.get_attribute(attribute) for element in elements]
        return item_names

    def get_text_values(self, elements):
        # Получить текстовые значения заданных элементов
        item_names = [element.text for element in elements]
        return item_names

    def click_element_by_attribute(self, attribute_path):
        # Кликнуть на элемент по атрибутному пути
        self.driver.find_element(By.XPATH, attribute_path).click()

    def click_element_by_text(self, text_path):
        # Кликнуть на элемент по текстовому пути
        self.driver.find_element(By.XPATH, text_path).click()
    
    def button_click(self,add=None,remove=None):
        button = ''
        if add:
            button = self.get_add_button_locator()
        if remove:
            button = self.get_remove_button_locator()
        self.find_element(by=By.ID,value=button).click()


    # def check_elements_clickable(self, elements, element_name, attribute=None, text=None):
        # results = []

        # for i, item_name in enumerate(elements):
        #     print(f"Value for element {i + 1}: {item_name}")

        #     if attribute:
        #         attribute_path = f'//{element_name}[@{attribute}="{item_name}"]'
        #         self.click_element_by_attribute(attribute_path)
        #         print(attribute_path)
        #     elif text:
        #         text_path = f'//{element_name}[text()="{item_name}"]'
        #         self.click_element_by_text(text_path)
        #         print(text_path)
        #     time.sleep(2)

        #     if self.driver.current_url.startswith("https://www.saucedemo.com/inventory-item."):
        #         results = []
        #     else:
        #         results.append(f"item {i + 1} didn't lead to the item path")

        #     self.driver.back()
        #     time.sleep(2)

        # return results