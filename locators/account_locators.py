from selenium.webdriver.common.by import By


class AccountPageLocators:
    LINK_ORDERS_HISTORY = By.LINK_TEXT, "История заказов"
    BUTTON_EXIT_FROM_ACCOUNT = By.XPATH, "//*[text()='Выход']"
    LIST_ORDER_NUMBERS = By.XPATH, "//*[contains(text(), '#')]"