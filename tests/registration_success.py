import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from generators.email_and_password_generators import generate_email
from generators.email_and_password_generators import generate_password
# без таких манипуляций VS Code не ест импорт из каталогов на разных уровнях вложенности

import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import Login_form_locators
from locators import Header_locators
from locators import Registration_form_locators
from locators import Personal_account_locators


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get('https://stellarburgers.nomoreparties.site/register')

email = generate_email()
name = email.split('_')[0]
password = generate_password(6)

wait.until(EC.presence_of_element_located(Registration_form_locators.NAME_FIELD)).send_keys(name)
driver.find_element(*Registration_form_locators.EMAIL_FIELD).send_keys(email)
driver.find_element(*Registration_form_locators.PASSWORD_FIELD).send_keys(password)
driver.find_element(*Registration_form_locators.SUBMIT_BUTTON).click()

try:
    assert '/login' in driver.current_url
except AssertionError:
    time.sleep(0.5) # жду редирект на страницу авторизации
    assert '/login' in driver.current_url

wait.until(EC.presence_of_element_located(Login_form_locators.EMAIL_FIELD)).send_keys(email)
driver.find_element(*Login_form_locators.PASSWORD_FIELD).send_keys(password)
driver.find_element(*Login_form_locators.SUBMIT_BUTTON).click()

wait.until(EC.element_to_be_clickable(Header_locators.PERSONAL_ACCOUNT_LINK)).click()

recieved_name = wait.until(EC.presence_of_element_located(Personal_account_locators.NAME_FIELD)).get_attribute('value')
assert name == recieved_name

driver.quit()