import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from generators.email_and_password_generators import generate_email
from generators.email_and_password_generators import generate_password
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.locators import Constructor_locators


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get('https://stellarburgers.nomoreparties.site/')


wait.until(EC.element_to_be_clickable(Constructor_locators.MENU_FILLINGS)).click()
clicked_menu_element = driver.find_element(*Constructor_locators.MENU_FILLINGS).get_attribute('class')
assert clicked_menu_element == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'


wait.until(EC.element_to_be_clickable(Constructor_locators.MENU_SAUCE)).click()
clicked_menu_element = driver.find_element(*Constructor_locators.MENU_SAUCE).get_attribute('class')
assert clicked_menu_element == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'


wait.until(EC.element_to_be_clickable(Constructor_locators.MENU_BUNS)).click()
clicked_menu_element = driver.find_element(*Constructor_locators.MENU_BUNS).get_attribute('class')
assert clicked_menu_element == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'


driver.quit()