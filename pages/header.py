import allure

from pages.base_page import BasePage
from locators.header_locators import HeaderLocators


class Header(BasePage):

    @allure.step("Клик на 'Личный кабинет' в шапке")
    def click_by_link_personal_account(self):
        self.click_by_element(HeaderLocators.LINK_PERSONAL_ACCOUNT)

    @allure.step("Клик на 'Конструктор' в шапке сайта")
    def click_by_link_constructor(self):
        self.click_by_element(HeaderLocators.LINK_CONSTRUCTOR)

    @allure.step("Клик на 'Ленту Заказов' в шапке сайта")
    def click_by_link_orders_feed(self):
        self.click_by_element(HeaderLocators.LINK_ORDERS_FEED)
