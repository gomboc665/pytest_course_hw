from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import pytest
from faker import Faker

"""
    1. https://the-internet.herokuapp.com/add_remove_elements/ (Необходимо создать и удалить элемент)
    2. https://the-internet.herokuapp.com/basic_auth (Необходимо пройти базовую авторизацию)
    3. https://the-internet.herokuapp.com/broken_images (Необходимо найти сломанные изображения)
    4. https://the-internet.herokuapp.com/checkboxes (Практика с чек боксами)
"""

url_1 = 'https://the-internet.herokuapp.com/add_remove_elements/'
url_2 = 'https://the-internet.herokuapp.com/basic_auth'
url_3 = 'https://the-internet.herokuapp.com/broken_images'
url_4 = 'https://the-internet.herokuapp.com/checkboxes'

def get_button_color(button, driver_imp):
    button_color_in_rgb = driver_imp.execute_script("return getComputedStyle(arguments[0]).backgroundColor;", button)
    r, g, b = [int(x) for x in button_color_in_rgb.replace("rgb(", "").replace(")", "").split(", ")]
    hex_color = "#{:02X}{:02X}{:02X}".format(r, g, b)
    return hex_color.lower()

def test_add_remove_elements(driver_imp):
    driver_imp.get(url_1)

    add_element_button = driver_imp.find_element(By.XPATH,'//button[@onclick="addElement()"]')
    add_button_color = get_button_color(button=add_element_button,driver_imp=driver_imp)

    assert add_button_color == '#2ba6cb'  # Проверка цвета кнопки
    assert add_element_button.text == 'Add Element', f'WRONG ADD BUTTON - {add_element_button.text}' # Проверка Текста
    add_element_button.click()
    
    delete_element_button = driver_imp.find_element(By.XPATH,'//button[@onclick="deleteElement()"]')
    delete_button_color = get_button_color(button=delete_element_button,driver_imp=driver_imp)

    assert delete_element_button.text == 'Delete', f"WRING DELETE BUTTON - {delete_element_button.text}" # Проверка Текста
    assert delete_button_color == '#2ba6cb' # Проверка цвета кнопки



