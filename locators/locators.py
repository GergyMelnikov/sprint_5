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


class Constructor_locators():
    MENU_SAUCE = (By.XPATH, '/html/body/div/div/main/section[1]/div[1]/div[2]') # Кнопка "Соусы" в меню
    MENU_BUNS = (By.XPATH, '/html/body/div/div/main/section[1]/div[1]/div[1]') # Кнопка "Булки" в меню
    MENU_FILLINGS = (By.XPATH, '/html/body/div/div/main/section[1]/div[1]/div[3]') # Кнопка "Начинки" в меню

    BUN_FLUORISCENT = (By.XPATH, '//img[@alt="Флюоресцентная булка R2-D3"]') # Булка "Флюоресцентная булка R2-D3"
    BUN_CRATER = (By.XPATH, '//img[@alt="Краторная булка N-200i"]') # Булка "Краторная булка N-200i"

    SAUCE_SPICE = (By.XPATH, '//img[@alt="Соус Spicy-X"]') # Соус "Соус Spicy-X"
    SAUCE_SPACE = (By.XPATH, '//img[@alt="Соус фирменный Space Sauce"]') # Соус "Соус фирменный Space Sauce"
    SAUCE_HETERO = (By.XPATH, '//img[@alt="Соус традиционный галактический"]') # Соус "Соус традиционный галактический"
    SAUCE_SPIKES = (By.XPATH, '//img[@alt="Соус с шипами Антарианского плоскоходца"]') # Соус "Соус с шипами Антарианского плоскоходца"

    FILLING_UNDEAD_MEAT = (By.XPATH, '//img[@alt="Мясо бессмертных моллюсков Protostomia"]') # Начинка "Мясо бессмертных моллюсков Protostomia"
    FILLING_CHOP = (By.XPATH, '//img[@alt="Говяжий метеорит (отбивная)"]') # Начинка "Говяжий метеорит (отбивная)"
    FILLING_MAGNOLIA = (By.XPATH, '//img[@alt="Биокотлета из марсианской Магнолии"]') # Начинка "Биокотлета из марсианской Магнолии"
    FILLING_TETRAMORPH = (By.XPATH, '//img[@alt="Филе Люминесцентного тетраодонтимформа"]') # Начинка "Филе Люминесцентного тетраодонтимформа"


