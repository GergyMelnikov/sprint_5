import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from generators.email_and_password_generators import generate_email
from generators.email_and_password_generators import generate_password
# без таких манипуляций VS Code не ест импорт из каталогов на разных уровнях

import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import by





driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get('https://stellarburgers.nomoreparties.site/')

print(generate_email())
print(generate_password(6))


time.sleep(10)
driver.quit()