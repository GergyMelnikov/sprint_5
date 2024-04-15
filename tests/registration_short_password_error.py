import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from generators.email_and_password_generators import generate_email
from generators.email_and_password_generators import generate_password
# без таких манипуляций VS Code не ест импорт из каталогов на разных уровнях вложенности

import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get('https://stellarburgers.nomoreparties.site/register')

email = generate_email()
password = generate_password(5)

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"]'))).send_keys(password)
driver.find_element(By.CSS_SELECTOR, 'button[class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()

recieved_error_text = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'p[class="input__error text_type_main-default"]'))).text

assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'
assert recieved_error_text == 'Некорректный пароль'


driver.quit()