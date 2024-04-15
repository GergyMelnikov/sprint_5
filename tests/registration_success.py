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
name = email.split('_')[0]
password = generate_password(6)

wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div/main/div/form/fieldset[1]/div/div/input'))).send_keys(name)
driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/fieldset[2]/div/div/input').send_keys(email)
driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys(password)
driver.find_element(By.CSS_SELECTOR, 'button[class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()

try:
    assert '/login' in driver.current_url
except AssertionError:
    time.sleep(0.5) # жду редирект на страницу авторизации
    assert '/login' in driver.current_url

wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/main/div/form/fieldset[1]/div/div/input'))).send_keys(email)
driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys(password)
driver.find_element(By.CSS_SELECTOR, 'button[class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()

wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/header/nav/a/p'))).click()

wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/main/div/div/div/ul/li[1]/div/div/input')))
recieved_name = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/ul/li[1]/div/div/input').get_attribute('value')

assert name == recieved_name

driver.quit()