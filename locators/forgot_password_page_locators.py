from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:

    INPUT_FIELD_EMAIL = By.NAME, 'name'
    BUTTON_RECOVERY = By.XPATH, "//*[text()='Восстановить']"
