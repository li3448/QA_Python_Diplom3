from selenium.webdriver.common.by import By


class LoginPageLocators:

    LINK_RECOVERY_PASSWORD = By.LINK_TEXT, 'Восстановить пароль'
    INPUT_FIELD_EMAIL = By.NAME, "name"
    INPUT_FIELD_PASSWORD = By.NAME, "Пароль"
    BUTTON_ENTER = By.XPATH, "//*[text()='Войти']"
