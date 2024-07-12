import allure


class TestPasswordRecovery:

    @allure.title("Проверка перехода на страницу восстановления пароля по ссылке 'Восстановить пароль'")
    def test_go_to_password_recovery_page_by_clicking_recover_password_link(self, login_page, forgot_password_page):
        login_page.open_login_page()
        login_page.click_link_recovery_password()
        with allure.step(f'Проверяем текущий url (URL = {login_page.current_url})'):
            assert login_page.current_url == forgot_password_page.URL

    @allure.title("Проверка ввод почты и клик по кнопке 'Восстановить'")
    def test_enter_email_and_click_restore_button(self, forgot_password_page, reset_password_page, user):
        forgot_password_page.open_forgot_password_page()
        forgot_password_page.fill_email_field(user['email'])
        forgot_password_page.click_button_recovery()
        reset_password_page.wait_load_page()
        with allure.step(f'Проверяем текущий url (URL = {forgot_password_page.current_url})'):
            assert forgot_password_page.current_url == reset_password_page.URL

    @allure.title("Проверка клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.")
    def test_click_show_hide_password_button_makes_field_active(self, forgot_password_page,
                                                                reset_password_page, create_user, user):
        forgot_password_page.open_forgot_password_page()
        forgot_password_page.fill_email_field(user_payload['email'])
        forgot_password_page.click_button_recovery()
        border = reset_password_page.inactive_border_of_field_password
        reset_password_page.click_icon_in_field_password()
        with allure.step(
                f"Проверяем, что класс объекта содержит 'input_status_active' "
                f"(class = {border.get_attribute('class')})"):
            assert 'input_status_active' in border.get_attribute('class')
