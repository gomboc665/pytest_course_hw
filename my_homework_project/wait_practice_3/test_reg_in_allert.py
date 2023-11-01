from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_add(driver,wait):
    # Инициализация драйвера
    username = 'admin'
    password = 'admin'
    url = f'https://{username}:{password}@the-internet.herokuapp.com/basic_auth'
    
    # Вводим логин и пароль с помощью pyautogui
    driver.get(url)

    assert wait.until(EC.text_to_be_present_in_element((By.XPATH,'//p'),'Congratulations! You must have the proper credentials.'))
    
