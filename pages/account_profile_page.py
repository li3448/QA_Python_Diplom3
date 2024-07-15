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

from config import URL



class AccountProfilePage(BasePage):
    def __init__(self, web_drv):
        super().__init__(web_drv)
        self.URL = f'{URL}/account/order-history'

    def open_order_history_page(self):
        with allure.step(f'Открытие страницы {self.URL}'):
            self.open_page(self.URL)

    @allure.step("Получение номеров заказов из Истории Заказов'")
    def get_order_numbers(self):
        order_numbers = list(order_number.text for order_number in self.get_visible_elements(
            AccountOrderHistoryPageLocators.LIST_ORDER_NUMBERS))
        with allure.step(f"Номера заказов из раздела 'История заказов'{order_numbers}"):
            return order_numbers

    def __init__(self, web_drv):
        super().__init__(web_drv)
        self.URL = f'{URL}/account/profile'

    @allure.step("Ожидание загрузки страницы")
    def wait_loading_page(self):
        self.wait_visible_element(AccountProfilePageLocators.LINK_ORDERS_HISTORY)

    @allure.step("Клик на  'Историю заказов'")
    def click_link_order_history(self):
        self.click_by_element(AccountProfilePageLocators.LINK_ORDERS_HISTORY)

    @allure.step("Клик на  'Выход'")

    def click_button_exit(self):
        self.click_by_element(AccountProfilePageLocators.BUTTON_EXIT_FROM_ACCOUNT)
