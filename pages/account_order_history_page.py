import allure

from pages.base_page import BasePage
from locators.account_order_history_page_locators import AccountOrderHistoryPageLocators
from config import URL


class AccountOrderHistoryPage(BasePage):
    def __init__(self, web_drv):
        super().__init__(web_drv)
        self.URL = f'{URL}/account/order-history'

    def open_order_history_page(self):
        with allure.step(f'Открываем страницу {self.URL}'):
            self.open_page(self.URL)

    @allure.step("Получаем номера заказов из раздела 'История заказов'")
    def get_order_numbers(self):
        order_numbers = list(order_number.text for order_number in self.get_visible_elements(
            AccountOrderHistoryPageLocators.LIST_ORDER_NUMBERS))
        with allure.step(f"Номера заказов из раздела 'История заказов'{order_numbers}"):
            return order_numbers
