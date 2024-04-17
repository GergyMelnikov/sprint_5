import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.locators import Login_form_locators
from locators.locators import Header_locators
from locators.locators import Personal_account_locators


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get('https://stellarburgers.nomoreparties.site/login')

email = 'Account_for_sign_in_testing@yaya.ru'
password = '123123'

wait.until(EC.presence_of_element_located(Login_form_locators.EMAIL_FIELD)).send_keys(email)
driver.find_element(*Login_form_locators.PASSWORD_FIELD).send_keys(password)
driver.find_element(*Login_form_locators.SUBMIT_BUTTON).click()

wait.until(EC.presence_of_element_located(Header_locators.PERSONAL_ACCOUNT_LINK)).click()
wait.until(EC.presence_of_element_located(Personal_account_locators.EXIT_BUTTON)).click()

wait.until(EC.presence_of_element_located(Login_form_locators.EMAIL_FIELD))
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

driver.quit()