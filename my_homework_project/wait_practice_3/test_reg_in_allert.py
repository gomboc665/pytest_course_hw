import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_add(driver,wait):
    # Инициализация драйвера
    
    # Открываем веб-страницу с HTTP-авторизацией
    driver.get("https://the-internet.herokuapp.com/basic_auth")
    
    # Вводим логин и пароль с помощью pyautogui
    pyautogui.write("admin")
    pyautogui.press("tab")
    pyautogui.write("admin")
    pyautogui.press("enter")

    assert wait.until(EC.text_to_be_present_in_element((By.XPATH,'//p'),'Congratulations! You must have the proper credentials.'))

    