import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from generators.email_and_password_generators import generate_email
from generators.email_and_password_generators import generate_password
# без таких манипуляций VS Code не ест импорт из каталогов на разных уровнях вложенности, точнее есть но наполовину, типа код работает, а подсветка и помощь в написании - нет
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.locators import Login_form_locators
from locators.locators import Header_locators
from locators.locators import Registration_form_locators
from locators.locators import Personal_account_locators
import pytest


class Test_registration():
    def test_success_registration_true(self, browser):
        driver, wait = browser
        driver.get(Registration_form_locators.URL)

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
            time.sleep(0.5) # жду редирект на страницу авторизации. Сори за костыль:)
            assert '/login' in driver.current_url


        wait.until(EC.presence_of_element_located(Login_form_locators.EMAIL_FIELD)).send_keys(email)
        driver.find_element(*Login_form_locators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*Login_form_locators.SUBMIT_BUTTON).click()

        wait.until(EC.element_to_be_clickable(Header_locators.PERSONAL_ACCOUNT_LINK)).click()

        received_name = wait.until(EC.presence_of_element_located(Personal_account_locators.NAME_FIELD)).get_attribute('value')
        assert name == received_name


    def test_short_password_error_visible_true(self, browser):
        driver, wait = browser
        driver.get(Registration_form_locators.URL)

        password = generate_password(5)

        wait.until(EC.presence_of_element_located(Registration_form_locators.PASSWORD_FIELD)).send_keys(password)
        driver.find_element(*Registration_form_locators.SUBMIT_BUTTON).click()

        recieved_error_text = wait.until(EC.visibility_of_element_located(Registration_form_locators.PASSWORD_ERROR)).text

        assert driver.current_url == Registration_form_locators.URL
        assert recieved_error_text == 'Некорректный пароль'
