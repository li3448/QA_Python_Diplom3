from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    LIST_ORDERS = By.XPATH, "//*[contains(@class, 'OrderHistory_listItem')]"
    LIST_ORDER_NUMBERS = By.XPATH, "//*[contains(text(), '#')]"
    LIST_ORDER_IN_PROGRESS = By.XPATH, "//*[contains(@class, '_orderListReady')]/li[contains(@class, 'digits')]"

    ORDER_NUMBER_IN_POPUP_WINDOW = By.XPATH, "//*[contains(@class, 'Modal_orderBox')]/p[1]"

    COUNTER_COMPLETED_FOR_ALL_TIME = By.XPATH, "//*[text()='Выполнено за все время:']/parent::div/p[2]"
    COUNTER_COMPLETED_FOR_TODAY = By.XPATH, "//*[text()='Выполнено за сегодня:']/parent::div/p[2]"
