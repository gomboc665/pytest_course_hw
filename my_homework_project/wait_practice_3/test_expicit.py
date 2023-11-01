from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import time


fake = Faker()
URL = "https://victoretc.github.io/selenium_waits/"
HEADER = (By.XPATH, "//h1")

BUTTON = (By.ID, "startTest")
BUTTON_REG = (By.ID, "register")
PASSWORD = (By.ID, "password")
LOGIN = (By.ID, "login")
CHECKBOX = (By.XPATH, '//input [@type="checkbox"]')
SUCCESS_MES = (By.ID, "successMessage")

login_key = fake.user_name()
password_key = fake.password(length=8, special_chars=True, digits=True)


def test_visible_after_with_explicit_waits(driver, wait):
    driver.get(URL)

    assert wait.until(
        EC.text_to_be_present_in_element(HEADER, "Практика с ожиданиями в Selenium")
    )

    # or
    # assert wait.until(EC.title_is('Практика с ожиданиями в Selenium'))

    clickable_after_button = wait.until(EC.element_to_be_clickable(BUTTON))
    assert clickable_after_button.text == "Начать тестирование"

    clickable_after_button.click()

    login_field = wait.until(EC.visibility_of_element_located(LOGIN))
    password_field = wait.until(EC.visibility_of_element_located(PASSWORD))
    login_field.clear()
    password_field.clear()

    login_field.send_keys(login_key)
    password_field.send_keys(password_key)
    find_checkbox = wait.until(EC.visibility_of_element_located(CHECKBOX))
    # assert wait.until(EC.text_to_be_present_in_element(CHECKBOX,'Согласен со всеми правилами'))

    find_checkbox.click()

    text_in_reg_button = driver.find_element(*BUTTON_REG)
    text_in_reg_button.click()
    visible_success = wait.until(EC.visibility_of_element_located(SUCCESS_MES))

    assert visible_success.text == "Вы успешно зарегистрированы!"

    time.sleep(3)
