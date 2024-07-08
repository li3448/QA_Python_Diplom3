from selenium.webdriver.common.by import By


class BasePageLocators:

    LINK_PERSONAL_ACCOUNT = By.XPATH, "//header/nav/a"
    LINK_CONSTRUCTOR = By.XPATH, "//*[text()='Конструктор']/parent::a"
    LINK_ORDERS_FEED = By.XPATH, "//*[text()='Лента Заказов']/parent::a"
