import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Login_form_locators
from locators.locators import Header_locators
from locators.locators import Personal_account_locators
import pytest


class Test_jump_to_account_from_main():
    def test_transition_to_account_profile_true(self, browser):
        driver, wait = browser
        driver.get(Login_form_locators.URL)
        email = 'Account_for_sign_in_testing@yaya.ru'
        password = '123123'

        wait.until(EC.element_to_be_clickable(Login_form_locators.EMAIL_FIELD)).send_keys(email)
        driver.find_element(*Login_form_locators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*Login_form_locators.SUBMIT_BUTTON).click()

        wait.until(EC.presence_of_element_located(Header_locators.PERSONAL_ACCOUNT_LINK)).click()

        wait.until(EC.presence_of_element_located(Personal_account_locators.EMAIL_FIELD))

        assert driver.current_url == Personal_account_locators.URL
