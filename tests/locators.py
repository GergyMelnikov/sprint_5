from selenium.webdriver.common.by import By

class Login_form_locators():
    EMAIL_FIELD = (By.XPATH, '/html/body/div/div/main/div/form/fieldset[1]/div/div/input') # Поле для ввода логина в форме авторизации
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[type="password"]') # Поле для ввода пароля в форме авторизации
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]') # Кнопка "Вход" в форме авторизации
    

class Header_locators():
    PERSONAL_ACCOUNT_LINK = (By.XPATH, '/html/body/div/div/header/nav/a/p') # Ссылка для перехода в личный кабинет, в хедере
    CONSTRUCROR_LINK = (By.XPATH, '/html/body/div/div/header/nav/ul/li[1]/a/p') # Кнопка для перехода в конструктор в хедере


class Personal_account_locators():
    EMAIL_FIELD = (By.XPATH, '/html/body/div/div/main/div/div/div/ul/li[2]/div/div/input') # Поле email в личном кабинете
    EXIT_BUTTON = (By.XPATH, '/html/body/div/div/main/div/nav/ul/li[3]/button') # Кнопка для выхода из личного кабинета
    NAME_FIELD = (By.XPATH, '/html/body/div/div/main/div/div/div/ul/li[1]/div/div/input')


class Forgot_password_form_locators():
    SIGN_IN_LINK = (By.CSS_SELECTOR, 'a[href="/login"]') # Ссыкла "Войти" в форме восстановления пароля и в форме регистрации

class Main_page_locators():
    SIGN_IN_BUTTON = (By.XPATH, '/html/body/div/div/main/section[2]/div/button') # Кнопка входа на главной

class Registration_form_locators():
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[type="password"]') # Поле для ввода пароял в форме регистрации
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]') # Кнопка сабмита в форме регистрации
    NAME_FIELD = (By.XPATH, '/html/body/div/div/main/div/form/fieldset[1]/div/div/input') # Поле для ввода имени в форме регистрации
    EMAIL_FIELD = (By.XPATH, '/html/body/div/div/main/div/form/fieldset[2]/div/div/input') # Поле для адреса электронной почты, в форме регистрации