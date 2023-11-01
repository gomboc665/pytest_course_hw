
from data.locators import USERNAME_FIELD, PASSWORD_FIELD, LOGIN_BUTTON
from data.full_data import MAIN_PAGE
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver, url=MAIN_PAGE)

    def login(self, username, password):

        self.driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(username)
  
    # вводим валидный пароль в поле "Password"
        self.driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(password)

    # кликаем на кнопку "Login"
        self.driver.find_element(By.XPATH, LOGIN_BUTTON).click()

   

