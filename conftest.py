import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import Login_form_locators, Header_locators, Personal_account_locators
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    yield driver, wait
    driver.quit()
