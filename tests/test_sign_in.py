import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.locators import Main_page_locators, Login_form_locators, Personal_account_locators, Header_locators, Forgot_password_form_locators


class Test_sign_in():
    def test_sign_in_from_forgot_password_form_true(self, browser, auth_data):
        driver, wait = browser
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password')

        wait.until(EC.element_to_be_clickable(Forgot_password_form_locators.SIGN_IN_LINK)).click()

        wait.until(EC.presence_of_element_located(Login_form_locators.EMAIL_FIELD)).send_keys(auth_data['email'])
        driver.find_element(*Login_form_locators.PASSWORD_FIELD).send_keys(auth_data['password'])
        driver.find_element(*Login_form_locators.SUBMIT_BUTTON).click()

        wait.until(EC.presence_of_element_located(Header_locators.PERSONAL_ACCOUNT_LINK)).click()
        email_field = wait.until(EC.presence_of_element_located(Personal_account_locators.EMAIL_FIELD)).get_attribute('value')

        assert email_field == 'account_for_sign_in_testing@yaya.ru'


    def test_sign_in_from_registration_form_true(self, browser, auth_data):
        driver, wait = browser
        driver.get('https://stellarburgers.nomoreparties.site/register')

        wait.until(EC.element_to_be_clickable(Forgot_password_form_locators.SIGN_IN_LINK)).click()

        wait.until(EC.presence_of_element_located(Login_form_locators.EMAIL_FIELD)).send_keys(auth_data['email'])
        driver.find_element(*Login_form_locators.PASSWORD_FIELD).send_keys(auth_data['password'])
        driver.find_element(*Login_form_locators.SUBMIT_BUTTON).click()

        wait.until(EC.presence_of_element_located(Header_locators.PERSONAL_ACCOUNT_LINK)).click()
        email_field = wait.until(EC.presence_of_element_located(Personal_account_locators.EMAIL_FIELD)).get_attribute('value')

        assert email_field == 'account_for_sign_in_testing@yaya.ru'


    def test_sign_in_from_main_page_true(self, browser, auth_data):
        driver, wait = browser
        driver.get('https://stellarburgers.nomoreparties.site/')

        wait.until(EC.element_to_be_clickable(Main_page_locators.SIGN_IN_BUTTON)).click()

        wait.until(EC.presence_of_element_located(Login_form_locators.EMAIL_FIELD)).send_keys(auth_data['email'])
        driver.find_element(*Login_form_locators.PASSWORD_FIELD).send_keys(auth_data['password'])
        driver.find_element(*Login_form_locators.SUBMIT_BUTTON).click()

        wait.until(EC.presence_of_element_located(Header_locators.PERSONAL_ACCOUNT_LINK)).click()
        email_field = wait.until(EC.presence_of_element_located(Personal_account_locators.EMAIL_FIELD)).get_attribute('value')

        assert email_field == 'account_for_sign_in_testing@yaya.ru'


    def test_sign_in_from_personal_account_link_true(self, browser, auth_data):
        driver, wait = browser
        driver.get('https://stellarburgers.nomoreparties.site/')

        wait.until(EC.element_to_be_clickable(Header_locators.PERSONAL_ACCOUNT_LINK)).click()

        wait.until(EC.presence_of_element_located(Login_form_locators.EMAIL_FIELD)).send_keys(auth_data['email'])
        driver.find_element(*Login_form_locators.PASSWORD_FIELD).send_keys(auth_data['password'])
        driver.find_element(*Login_form_locators.SUBMIT_BUTTON).click()

        wait.until(EC.presence_of_element_located(Header_locators.PERSONAL_ACCOUNT_LINK)).click()
        email_field = wait.until(EC.presence_of_element_located(Personal_account_locators.EMAIL_FIELD)).get_attribute('value')

        assert email_field == 'account_for_sign_in_testing@yaya.ru'
