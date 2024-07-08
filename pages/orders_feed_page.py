import allure

from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
from config import URL


class OrdersFeedPage(BasePage):
    def __init__(self, web_drv):
        super().__init__(web_drv)
        self.URL = f'{URL}/feed'

    def open_order_feed_page(self):
        with allure.step(f'Открытие страницы {self.URL}'):
            self.open_page(self.URL)

    @allure.step('Клик на заказ')
    def click_orders_by_index_(self, index):
        orders = self.get_visible_elements(OrderFeedPageLocators.LIST_ORDERS)
        orders[index].click()

    @allure.step('Получение номера заказа')
    def get_order_number_by_index(self, index):
        order_numbers = self.get_visible_elements(OrderFeedPageLocators.LIST_ORDER_NUMBERS)
        return order_numbers[index].text

    @allure.step("Получение списка номеров заказов")
    def get_orders_number(self):
        orders_number = list(order_number.text for order_number in self.get_visible_elements(
            OrderFeedPageLocators.LIST_ORDER_NUMBERS))
        return orders_number

   # @allure.step('Получение  номер заказа из всплывающего окна')
    #def get_order_number_in_popup_window(self):
        #return self.get_visible_element(OrderFeedPageLocators.ORDER_NUMBER_IN_POPUP_WINDOW).text

    @allure.step('Получение количества выполненных заказов')
    def get_count_completed_orders_for_all_time(self):
        return int(self.get_visible_element(OrderFeedPageLocators.COUNTER_COMPLETED_FOR_ALL_TIME).text)

    @allure.step('Получение количества выполненных заказов за сегодня')
    def get_count_completed_orders_for_today(self):
        return int(self.get_visible_element(OrderFeedPageLocators.COUNTER_COMPLETED_FOR_TODAY).text)

    @allure.step('Получение заказов в работе')
    def get_orders_number_in_progress(self):
        return list(order_number.text for order_number in self.get_visible_elements(
            OrderFeedPageLocators.LIST_ORDER_IN_PROGRESS))
