import allure
import pytest


class TestPersonalAccount:

    @allure.title("Проверка перехода в личный кабинет по ссылке 'Личный кабинет' в шапке")
    def test_go_to_personal_account_by_link_header(self, logged, header, account_profile_page):
        header.click_by_link_personal_account()
        account_profile_page.wait_loading_page()
        with allure.step(f'Проверяем текущий url (URL = {header.current_url})'):
            assert header.current_url == account_profile_page.URL

    @allure.title("Проверка переход в раздел личного кабинета 'История заказов'")
    def test_go_to_order_history_section_by_click_link_order_history(self, logged, header, account_profile_page,
                                                                     account_order_history_page):
        header.click_by_link_personal_account()
        account_profile_page.click_link_order_history()
        with allure.step(f'Проверяем текущий url (URL = {account_profile_page.current_url})'):
            assert account_profile_page.current_url == account_order_history_page.URL

    @allure.title("Проверка выхода из аккаунта")
        with allure.step(f'Проверка текущего url (URL = {header.current_url})'):
            assert header.current_url == account_profile_page.URL

    @allure.title("Проверка перехода в раздел личного кабинета 'История заказов'")
    def test_go_to_order_history_section_by_click_link_order_history(self, logged, header, account_profile_page ):
        header.click_by_link_personal_account()
        account_profile_page.click_link_order_history()
        with allure.step(f'Проверяем текущий url (URL = {account_profile_page.current_url})'):
            assert account_profile_page.current_url == account_profile_page.URL

    @allure.title("Выход из аккаунта")
    def test_exit_from_personal_account(self, logged, login_page, header, account_profile_page):
        header.click_by_link_personal_account()
        account_profile_page.click_button_exit()
        login_page.wait_loading_page()
        
        with allure.step(f'Проверяем текущий url (URL = {account_profile_page.current_url})'):
            assert account_profile_page.current_url == login_page.URL

    @allure.title("Переход на страницу восстановления пароля по ссылке 'Восстановить пароль'")
    def test_go_to_password_recovery_page_by_clicking_recover_password_link(self, login_page, forgot_password_page):
        login_page.open_login_page()
        login_page.click_link_recovery_password()
        with allure.step(f'Проверяем текущий url (URL = {login_page.current_url})'):
            assert login_page.current_url == forgot_password_page.URL

    @allure.title("Проверка ввода почты и клика по кнопке 'Восстановить'")
    def test_enter_email_and_click_restore_button(self, forgot_password_page, reset_password_page, user):
        forgot_password_page.open_forgot_password_page()
        forgot_password_page.fill_email_field(user['email'])
        forgot_password_page.click_button_recovery()
        reset_password_page.wait_load_page()
        with allure.step(f'Проверяем текущий url (URL = {forgot_password_page.current_url})'):
            assert forgot_password_page.current_url == reset_password_page.URL

    @allure.title("Проверка клика по кнопке показать/скрыть пароль.")
    def test_click_show_hide_password_button_makes_field_active(self, forgot_password_page,
                                                                reset_password_page, user):
        forgot_password_page.open_forgot_password_page()
        forgot_password_page.fill_email_field(user['email'])
        forgot_password_page.click_button_recovery()
        border = reset_password_page.inactive_border_of_field_password
        reset_password_page.click_icon_in_field_password()
        with allure.step(
                f"Проверка, что класс объекта содержит 'input_status_active' "
                f"(class = {border.get_attribute('class')})"):
            assert 'input_status_active' in border.get_attribute('class')

