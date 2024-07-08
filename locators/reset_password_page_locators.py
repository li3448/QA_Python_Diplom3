from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:

    ICON_IN_FIELD_PASSWORD = By.XPATH, "//*[contains(@class, 'input__icon')]"
    BORDER_FIELD_PASSWORD = By.XPATH, "//*[contains(@class, 'Auth_form')]/fieldset[1]/div/div"
    INACTIVE_BORDER_FIELD_PASSWORD = By.XPATH, "//*[contains(@class , 'input_type_password')]"
