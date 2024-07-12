import allure


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
    def test_exit_from_personal_account(self, logged, login_page, header, account_profile_page):
        header.click_by_link_personal_account()
        account_profile_page.click_button_exit()
        login_page.wait_loading_page()
        with allure.step(f'Проверяем текущий url (URL = {account_profile_page.current_url})'):
            assert account_profile_page.current_url == login_page.URL
