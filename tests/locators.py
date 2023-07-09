from selenium.webdriver.common.by import By


class TestLocators:
    SEARCH_LOGIN_ACCOUNT = By.XPATH, './/button[text() = "Войти в аккаунт"]' # кнопка "Войти в аккаунт" на главной странице сайта
    SEARCH_NAME = By.XPATH, '//input[@name="name"]' # поле ввода логина для входа
    SEARCH_PASS = By.XPATH, '//input[@name="Пароль"]' #поле ввода пароля для входа и на форме регистрации
    SEARCH_LOGIN = By.XPATH, './/button[text() = "Войти"]' #кнопка "Войти" для авторизации в ЛК
    SEARCH_ACCOUNT_PROFILE = By.XPATH, './/p[text() = "Личный Кабинет"]' #ссылка для перехода в Личный Кабинет
    SEARCH_CHECKOUT = By.XPATH,'.//button[text() = "Оформить заказ"]' # кнопка "Оформить заказ" на главной странице сайта
    SEARCH_REGISTER = By.XPATH, './/a[text() = "Зарегистрироваться"]' # кнопка для регистрации на сайте
    SEARCH_REGISTER_LOGIN = By.XPATH, './/a[@href = "/login"]' # ссылка "Войти" на форме регистрации на сайте
    SEARCH_RESTORE = By.XPATH, './/a[text() = "Восстановить пароль"]' # ссылка восстановления пароля
    SEARCH_RESTORE_LOGIN = By.XPATH, './/a[text() = "Войти"]' # кнопка входа на экране восстановления пароля
    SEARCH_LOGOUT = By.XPATH, './/button[text() = "Выход"]' # кнопка выхода в личном кабинете
    SEARCH_CONSTRUCTOR = By.XPATH, './/p[text() = "Конструктор"]' # ссылка на конструткор
    SEARCH_LOGO = By.XPATH, './/a[@class ="active"]' #ссылка на логотип
    SEARCH_ROLLS = By.XPATH, './/span[text() = "Булки"]' # переход к просмотру булок
    SEARCH_SAUCES = By.XPATH, './/span[text() = "Соусы"]' #переход к просмотру соусов
    SEARCH_FILLINGS = By.XPATH, './/span[text() = "Начинки"]' #переход к просмотру начинок
    SEARCH_NAME_REGISTRATION = By.XPATH, './/label[text()="Имя"]/following-sibling::input' # имя при регистрации
    SEARCH_EMAIL_REGISTRATION = By.XPATH, './/label[text()="Email"]/following-sibling::input'  # емейл при регистрации
    SEARCH_BUTTON_REGISTRATION = By.XPATH, '.// button[text() = "Зарегистрироваться"]' # кнопка зарегистрироваться для регистрации
    PASSWORD = '12345678'
    NAME_REGISTRATION = 'Светлана'