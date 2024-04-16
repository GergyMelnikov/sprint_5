from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get('https://stellarburgers.nomoreparties.site/login')

email = 'Account_for_sign_in_testing@yaya.ru'
password = '123123'

driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/fieldset[1]/div/div/input').send_keys(email)
driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys(password)
driver.find_element(By.CSS_SELECTOR, 'button[class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()

wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/header/nav/a/p'))).click()
wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/main/div/nav/ul/li[3]/button'))).click()

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'form[class="Auth_form__3qKeq mb-20"]')))
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

driver.quit()