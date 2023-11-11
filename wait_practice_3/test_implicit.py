from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from faker import Faker

fake = Faker()

URL = "https://victoretc.github.io/selenium_waits/"
HEADER = (By.XPATH, "//h1")

BUTTON = (By.XPATH, '//button[@id="startTest" and not(contains(@class, "hidden"))]')
BUTTON_REG = (By.ID, "register")
PASSWORD = (By.ID, "password")
LOGIN = (By.ID, "login")
CHECKBOX = (By.XPATH, '//input [@type="checkbox"]')
SUCCESS_MES = (
    By.XPATH,
    '//p[@id="successMessage" and not(contains(@class, "hidden"))]',
)
REG_FORM = (
    By.XPATH,
    '//div[@id="registrationForm" and not(contains(@class, "hidden"))]',
)


login_key = fake.user_name()
password_key = fake.password(length=8, special_chars=True, digits=True)


def test_visible_after_with_implicit_wait(driver_imp):
    driver_imp.get(URL)

    visible_header = driver_imp.find_element(*HEADER)
    assert visible_header.is_displayed()

    visible_button = driver_imp.find_element(*BUTTON)

    assert visible_button.text == "Начать тестирование"

    try:
        visible_button.click()
    except ElementClickInterceptedException:
        print("Элемент не кликабельный")

    registration_form = driver_imp.find_element(*REG_FORM)

    assert registration_form.is_displayed()
    login_field = driver_imp.find_element(*LOGIN)
    password_field = driver_imp.find_element(*PASSWORD)
    login_field.clear()
    password_field.clear()

    login_field.send_keys(login_key)
    password_field.send_keys(password_key)
    find_checkbox = driver_imp.find_element(*CHECKBOX)

    # assert find_checkbox.text == 'Согласен со всеми правилами'
    find_checkbox.click()

    text_in_reg_button = driver_imp.find_element(*BUTTON_REG)
    text_in_reg_button.click()
    visible_success = driver_imp.find_element(*SUCCESS_MES)

    assert visible_success.text == "Вы успешно зарегистрированы!"
