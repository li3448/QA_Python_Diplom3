import allure

from pages.base_page import BasePage
from locators.account_profile_page_locators import AccountProfilePageLocators
from config import URL


class AccountProfilePage(BasePage):
    def __init__(self, web_drv):
        super().__init__(web_drv)
        self.URL = f'{URL}/account/profile'

    @allure.step("Ожидаем загрузки страницы")
    def wait_loading_page(self):
        self.wait_visible_element(AccountProfilePageLocators.LINK_ORDERS_HISTORY)

    @allure.step("Нажимаем на ссылку 'История заказов'")
    def click_link_order_history(self):
        self.click_by_element(AccountProfilePageLocators.LINK_ORDERS_HISTORY)

    @allure.step("Нажимаем на кнопку 'Выход'")
    def click_button_exit(self):
        self.click_by_element(AccountProfilePageLocators.BUTTON_EXIT_FROM_ACCOUNT)
