import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Login_form_locators
from locators.locators import Header_locators
from locators.locators import Personal_account_locators
import pytest
import time

class Test_exit_from_account():
    def test_exit_from_profile_true(self, browser, auth_data):
        driver, wait = browser
        driver.get('https://stellarburgers.nomoreparties.site/login')

        wait.until(EC.presence_of_element_located(Login_form_locators.EMAIL_FIELD)).send_keys(auth_data['email'])
        driver.find_element(*Login_form_locators.PASSWORD_FIELD).send_keys(auth_data['password'])
        driver.find_element(*Login_form_locators.SUBMIT_BUTTON).click()

        wait.until(EC.presence_of_element_located(Header_locators.PERSONAL_ACCOUNT_LINK)).click()
        wait.until(EC.presence_of_element_located(Personal_account_locators.EXIT_BUTTON)).click()

        wait.until(EC.presence_of_element_located(Login_form_locators.SUBMIT_BUTTON))
        try:
            assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        except Exception:
            time.sleep(0.5)
            assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'