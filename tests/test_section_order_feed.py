import allure
import pytest

from helpers import create_order


class TestSectionOrderFeed:

    @allure.title('Проверка открытия всплывающее окна с деталями по клику на заказ в ленте заказов')
    def test_opening_popup_window_by_click_on_order(self, order_feed_page):
        order_index = 0
        order_feed_page.open_order_feed_page()
        number_order = order_feed_page.get_order_number_by_index(order_index)
        order_feed_page.click_orders_by_index_(order_index)
        with allure.step('проверяем, что окно заказа открылось'):
            assert order_feed_page.get_order_number_in_popup_window() == number_order

    @allure.title("Проверка отображения заказов пользователя из раздела 'История заказов' на странице 'Лента заказов'")
    @pytest.mark.orders_count(2)
    def test_displaying_user_orders_from_order_history_section_on_order_feed_page(self, user, logged,
                                                                                  order, header, create_user, order_feed_page,
                                                                                  account_profile_page,
                                                                                  account_order_history_page):
        header.click_by_link_personal_account()
        account_profile_page.click_link_order_history()
        order_numbers_from_order_history = account_order_history_page.get_order_numbers()
        order_feed_page.open_order_feed_page()
        order_numbers_from_order_feed = order_feed_page.get_orders_number()
        for order_number in order_numbers_from_order_history:
            with allure.step(f"Проверяем есть ли заказ {order_number} в 'Ленте заказов'"):
                assert order_number in order_numbers_from_order_feed

    @allure.title("Проверка увеличения счётчика 'Выполнено за всё время' при создании нового заказа")
    def test_increases_completed_for_all_time_counter_after_creating_order(self, user, create_user, logged, header, index_page,
                                                                           order_feed_page):
        header.click_by_link_orders_feed()
        counter_before = order_feed_page.get_count_completed_orders_for_all_time()
        header.click_by_link_constructor()
        create_order(index_page)
        header.click_by_link_orders_feed()
        with allure.step('Проверяем увеличение счетчика'):
            assert order_feed_page.get_count_completed_orders_for_all_time() == counter_before + 1

    @allure.title("Проверка увеличения счётчика 'Выполнено за сегодня' при создании нового заказа")
    def test_increases_completed_for_today_counter_after_creating_order(self, user,create_user, logged, header, index_page,
                                                                        order_feed_page):
        header.click_by_link_orders_feed()
        counter_before = order_feed_page.get_count_completed_orders_for_today()
        header.click_by_link_constructor()
        create_order(index_page)
        header.click_by_link_orders_feed()
        with allure.step('Проверяем увеличение счетчика'):
            assert order_feed_page.get_count_completed_orders_for_today() == counter_before + 1

    @allure.title("Проверка появления номера заказа в разделе 'В работе' после его оформления")
    def test_order_number_appears_in_section_in_progress_after_place_order(self, user, create_user, logged, header,
                                                                           index_page, order_feed_page):
        index_page.add_ingredient_to_order_by_index(0)
        index_page.add_ingredient_to_order_by_index(3)
        index_page.click_button_place_order()
        index_page.click_cross_button_in_popup_window()
        order_number = index_page.get_order_number_fom_order_confirm_window()
        header.click_by_link_orders_feed()
        order_numbers_in_progress = order_feed_page.get_orders_number_in_progress()

        with allure.step(f"Проверяем номер нового заказа - {order_number}"
                         f" в разделе 'В работе' {order_numbers_in_progress}"):
            assert order_number in order_numbers_in_progress
