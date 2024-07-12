from selenium.webdriver.common.by import By


class AccountProfilePageLocators:
    LINK_ORDERS_HISTORY = By.LINK_TEXT, "История заказов"
    BUTTON_EXIT_FROM_ACCOUNT = By.XPATH, "//*[text()='Выход']"
