import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Login_form_locators
from locators.locators import Header_locators, Constructor_locators
import pytest

class Test_jump_from_account_to_constructor():
    def test_jump_to_constructor_from_profile_on_logo_true(self, browser, auth_data):
        driver, wait = browser
        driver.get(Login_form_locators.URL)

        wait.until(EC.presence_of_element_located(Login_form_locators.EMAIL_FIELD)).send_keys(auth_data['email'])
        driver.find_element(*Login_form_locators.PASSWORD_FIELD).send_keys(auth_data['password'])
        driver.find_element(*Login_form_locators.SUBMIT_BUTTON).click()

        wait.until(EC.presence_of_element_located(Header_locators.PERSONAL_ACCOUNT_LINK)).click()

        wait.until(EC.element_to_be_clickable(Header_locators.LOGO_LINK)).click()

        assert driver.current_url == Constructor_locators.URL


    def test_jump_to_constructor_from_profile_on_constructor_link_true(self, browser, auth_data):
        driver, wait = browser
        driver.get(Login_form_locators.URL)

        wait.until(EC.presence_of_element_located(Login_form_locators.EMAIL_FIELD)).send_keys(auth_data['email'])
        driver.find_element(*Login_form_locators.PASSWORD_FIELD).send_keys(auth_data['password'])
        driver.find_element(*Login_form_locators.SUBMIT_BUTTON).click()

        wait.until(EC.presence_of_element_located(Header_locators.PERSONAL_ACCOUNT_LINK)).click()

        wait.until(EC.presence_of_element_located(Header_locators.CONSTRUCROR_LINK)).click()

        assert driver.current_url == Constructor_locators.URL

