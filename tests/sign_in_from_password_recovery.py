from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import Forgot_password_form_locators
from locators import Login_form_locators


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get('https://stellarburgers.nomoreparties.site/forgot-password')

email = 'Account_for_sign_in_testing@yaya.ru'
password = '123123'

wait.until(EC.element_to_be_clickable(Forgot_password_form_locators.SIGN_IN_LINK)).click()

wait.until(EC.presence_of_element_located(Login_form_locators.EMAIL_FIELD)).send_keys(email)
driver.find_element(*Login_form_locators.PASSWORD_FIELD).send_keys(password)
driver.find_element(*Login_form_locators.SUBMIT_BUTTON).click()

wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/header/nav/a/p'))).click()
email_field = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/main/div/div/div/ul/li[2]/div/div/input'))).get_attribute('value')

assert email_field == 'account_for_sign_in_testing@yaya.ru'

driver.quit()