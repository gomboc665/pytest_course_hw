import pytest
import time
from data.conftest import driver,driver_and_auth,chrome_options
from pages.catalog_page import CatalogPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from data.locators import back_pack_img,shopping_cart,back_pack_text,shopping_badge

def test_cart_page_delete_item(driver,driver_and_auth):
    """2. Удаление товара из корзины через корзину"""
    login_page = driver_and_auth
   
    catalog_page = CatalogPage(driver=driver,item_name="sauce-labs-backpack")
    add_button = catalog_page.get_add_button_locator()
    catalog_page.find_element(by=By.ID,value=add_button).click()
    
    catalog_page.find_element(by=By.XPATH,value=shopping_cart).click()

    cart_page = CartPage(driver=driver)
    cart_page.wait.until(EC.url_to_be(cart_page.url))

    cart_page.remove_item_from_cart()
    try:
        cart_page.wait.until_not(
            EC.presence_of_element_located((By.XPATH, back_pack_text))
        )
        print("Элемент больше не существует на странице.")
    except Exception:
        print("Элемент все еще существует на странице.")

    cart_page.reset_and_logout()

# **Корзина**

items = [back_pack_img,back_pack_text]

@pytest.mark.parametrize('item', items)
def test_cart_page_add_item_from_item_page(item,driver,driver_and_auth):
    """ 3. Добавление товара в корзину из карточки товара"""
    login_page = driver_and_auth

    catalog_page = CatalogPage(driver,item_name=item)
    catalog_page.find_element_by_item_name(by=By.XPATH).click()
    
    product_page = ProductPage(driver=driver,item_name="sauce-labs-backpack")
    product_page.wait.until(EC.url_to_be(product_page.url))
    
    add_button = product_page.get_add_button_locator()
    product_page.find_element(by=By.ID,value=add_button).click()
    # перешли в корзину


    product_page.find_element(by=By.XPATH,value=shopping_cart).click()
    cart_page = CartPage(driver=driver)
    if EC.presence_of_element_located((By.XPATH, back_pack_text))(driver):
        pass
    else:
        pytest.fail("there is no item in the cart")
    


    cart_page.reset_and_logout()


@pytest.mark.parametrize('item', items)
def test_cart_page_delete_item_from_item_page(item,driver,driver_and_auth):
    """ 4. Удаление товара из корзины через карточку товара"""
    login_page = driver_and_auth
   
    catalog_page = CatalogPage(driver,item_name=item)
    catalog_page.find_element_by_item_name(by=By.XPATH).click()

    product_page = ProductPage(driver=driver,item_name="sauce-labs-backpack")
    product_page.wait.until(EC.url_to_be(product_page.url))

    product_page.button_click(add=True)

    if product_page.shopping_badge_element().text != '1':
        pytest.fail("Item have not been added to the cart")

    product_page.button_click(remove=True)
 
    try:
        product_page.wait.until(
            EC.presence_of_element_located((By.XPATH, shopping_badge))
        )
    except Exception:
        pass  
    else:
        pytest.fail("Item was not removed from the cart")  

    

    


