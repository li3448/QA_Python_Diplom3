import allure
import pytest


class TestBasicFunctionality:

    @allure.title('Проверка перехода по клику на ссылку «Конструктор» в шапке сайта')
    def test_goto_by_click_link_constructor(self, header, index_page):
        index_page.open_index_page()
        header.click_by_link_orders_feed()
        header.click_by_link_constructor()

        with allure.step(f'Проверяем текущий url (URL = {header.current_url})'):
            assert header.current_url == index_page.URL

    @allure.title('Проверка перехода по клику на ссылку «Лента заказов» в шапке сайта')
    def test_goto_by_click_link_orders_feed(self, header, index_page, order_feed_page):
        index_page.open_index_page()
        header.click_by_link_orders_feed()

        with allure.step(f'Проверяем текущий url (URL = {header.current_url})'):
            assert header.current_url == order_feed_page.URL

    @allure.title('Проверка появления всплывающего окно с деталями при кликнуть на ингредиент')
    def test_pop_up_details_window_by_click_on_ingredient(self, index_page):
        index_page.open_index_page()
        ingredient_name = index_page.get_name_ingredient_by_index_(0)
        index_page.click_on_ingredient_by_index_(0)

        with allure.step(f'Проверяем открылось ли окно с деталями об ингредиенте ({ingredient_name})'):
            assert index_page.get_ingredient_name_in_details_window() == ingredient_name

    @allure.title('Проверка закрытия всплывающего окна с деталями о ингредиенте кликом по крестику')
    def test_close_pop_up_details_window_by_click_on_cross_button(self, index_page):
        index_page.open_index_page()
        index_page.click_on_ingredient_by_index_(1)
        popup_window = index_page.get_popup_details_window()
        index_page.click_cross_button_in_popup_window()

        with allure.step(f'Проверяем что окно с деталями об ингредиенте закрылось'):
            assert 'Modal_modal_opened' not in popup_window.get_attribute('class')

    @allure.title('Проверка увеличения счетчика ингредиента при добавлении его в заказ')
    @pytest.mark.parametrize(
        'ingredient_index, counter_inc',
        (
                (0, 2), (3, 1)
        )
    )
    def test_increment_ingredient_counter_when_adding_it_to_order(self, index_page, ingredient_index, counter_inc):
        index_page.open_index_page()
        counter_before = index_page.get_counter_ingredient_by_index_(ingredient_index)
        index_page.add_ingredient_to_order_by_index(ingredient_index)
        counter_past = index_page.get_counter_ingredient_by_index_(ingredient_index)

        with allure.step(f'Проверяем что счетчик увеличился на {counter_inc}'):
            assert counter_past == counter_before + counter_inc

    @allure.title('Проверка авторизированный пользователь может оформить заказ')
    def test_logged_user_can_place_order(self, user,create_user, logged, index_page):
        index_page.add_ingredient_to_order_by_index(1)
        index_page.add_ingredient_to_order_by_index(4)
        index_page.click_button_place_order()

        with allure.step(f'Проверяем, что заказ оформлен'):
            assert index_page.get_text_fom_order_confirm_window() == 'Ваш заказ начали готовить'
