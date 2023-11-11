import pytest
from data.conftest import driver,driver_and_auth,chrome_options
from pages.catalog_page import CatalogPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.locators import back_pack_img,back_pack_text,shopping_cart,shopping_badge


# def test_catalog_page_elements_clickable(driver,driver_and_auth):
#     # Получите экземпляр CatalogPage
#     driver_and_auth
#     catalog_page = CatalogPage(driver,CATALOG_PAGE,"item-name")

#     catalog_page.open()

#     # Найдите элементы
#     item_elements = catalog_page.find_elements_by_class(path_value="inventory_item_img", element_name="img")

#     # Проверьте кликабельность элементов
#     results = catalog_page.check_elements_clickable(elements=item_elements, element_name="img", attribute="alt")

#     for result in results:
#         assert "is clickable" in result, f"Element is not clickable: {result}"
    
# def test_catalog_page_elements_text(driver,driver_and_auth):
#     # Получите экземпляр CatalogPage
#     driver_and_auth
#     catalog_page = CatalogPage(driver,CATALOG_PAGE,"item-name")

#     catalog_page.open()

#     # Найдите элементы
#     item_elements = catalog_page.find_elements_by_class(path_value="inventory_item_name", element_name="div")
#     print(item_elements)
#     # Проверьте кликабельность элементов
#     results = catalog_page.check_elements_clickable(elements=item_elements,element_name="div", text=True)

#     for result in results:
#         assert "is clickable" in result, f"Element is not clickable: {result}"


items = [back_pack_img,back_pack_text]

@pytest.mark.parametrize('item', items)
def test_catalog_page_element_clickable(item,driver,driver_and_auth):

    login_page = driver_and_auth

    catalog_page = CatalogPage(driver,item_name=item)
    catalog_page.find_element_by_item_name(by=By.XPATH).click()

    catalog_page.reset_and_logout()


def test_catalog_page_add_to_cart(driver,driver_and_auth):
    """1. Добавление товара в корзину через каталог"""

    login_page = driver_and_auth

    catalog_page = CatalogPage(driver=driver,item_name="sauce-labs-backpack")

    catalog_page.button_click(add=True)

    catalog_page.reset_and_logout()

def test_catalog_page_remove_from_cart(driver,driver_and_auth):
    """1.1 Удаление товара в корзину через каталог"""
    login_page = driver_and_auth
    
    catalog_page = CatalogPage(driver=driver,item_name="sauce-labs-backpack")

    catalog_page.button_click(add=True)
    
    catalog_page.button_click(remove=True)

    catalog_page.reset_and_logout()

def test_catalog_page_check_badge(driver,driver_and_auth):
    """1.3 Проверка добавления айтема в корзину"""
    login_page = driver_and_auth
    
    catalog_page = CatalogPage(driver=driver,item_name="sauce-labs-backpack")

    catalog_page.button_click(add=True)


    if catalog_page.shopping_badge_element().text != '1':
        pytest.fail("Item have not been added to the cart")

    catalog_page.reset_and_logout()


    
