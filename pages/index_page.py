import allure

from pages.base_page import BasePage
from locators.index_page_locators import IndexPageLocators
from config import URL


class IndexPage(BasePage):
    def __init__(self, web_drv):
        super().__init__(web_drv)
        self.URL = f'{URL}/'

    def open_index_page(self):
        with allure.step(f'Открытие страницы {self.URL}'):
            self.open_page(self.URL)

    @allure.step('Клик на ингредиент')
    def click_on_ingredient_by_index_(self, index):
        ingredients = self.get_visible_elements(IndexPageLocators.LIST_OF_INGREDIENTS)
        ingredients[index].click()


    @allure.step('Клик на крестик во всплывающем окне')

    @allure.step('Клик на крестик')

    def click_cross_button_in_popup_window(self):
        self.click_by_element(IndexPageLocators.BUTTON_CROSS_IN_POPUP_WINDOW)

    @allure.step("Клик на кнопку 'Оформить заказ'")
    def click_button_place_order(self):
        self.click_by_element(IndexPageLocators.BUTTON_PLACE_ORDER)


    @allure.step('Добавление ингредиента в заказ')
    def add_ingredient_to_order_by_index(self, index):
        ingredients = self.get_visible_elements(IndexPageLocators.LIST_OF_INGREDIENTS)
        basket = self.get_visible_element(IndexPageLocators.SECTION_CONSTRUCTOR_BASKET)
        self.drag_and_drop(ingredients[index], basket)

    @allure.step('Получение название ингредиента')
    def get_name_ingredient_by_index_(self, index):
        ingredients = self.get_visible_elements(IndexPageLocators.LIST_OF_INGREDIENTS)
        return ingredients[index].text.split('\n')[2]


    @allure.step('Получение названия ингредиента в окне деталей')

    def get_ingredient_name_in_details_window(self):
        return self.get_visible_element(IndexPageLocators.TEXT_NAME_INGREDIENT_IN_DETAILS_WINDOW).text

    @allure.step('Получение текста из окна подтверждения заказа')
    def get_text_fom_order_confirm_window(self):
        return self.get_visible_element(IndexPageLocators.TEXT_ORDER_START_TO_PREPARE).text

    @allure.step('Получение номера заказа из окна подтверждения заказа')
    def get_order_number_fom_order_confirm_window(self):
        return f'0{self.get_element(IndexPageLocators.ORDER_NUMBER_IN_POPUP_WINDOW).text}'

    @allure.step("Получение web-элемента 'Детали ингредиента'")
    def get_popup_details_window(self):
        return self.get_visible_element(IndexPageLocators.MODAL_POPUP_WINDOW)



    @allure.step('Получение значения счетчика ингредиентов')
    def get_counter_ingredient_by_index_(self, index):
        counters = self.get_visible_elements(IndexPageLocators.LIST_COUNTERS_OF_INGREDIENTS)
        return int(counters[index].text)
