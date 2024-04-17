import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from generators.email_and_password_generators import generate_email
from generators.email_and_password_generators import generate_password
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import Registration_form_locators


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get('https://stellarburgers.nomoreparties.site/register')

email = generate_email()
password = generate_password(5)

wait.until(EC.presence_of_element_located(Registration_form_locators.PASSWORD_FIELD)).send_keys(password)
driver.find_element(*Registration_form_locators.SUBMIT_BUTTON).click()

recieved_error_text = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'p[class="input__error text_type_main-default"]'))).text

assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'
assert recieved_error_text == 'Некорректный пароль'

driver.quit()