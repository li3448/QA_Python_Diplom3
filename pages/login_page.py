import allure

from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from config import URL


class LoginPage(BasePage):
    def __init__(self, web_drv):
        super().__init__(web_drv)
        self.URL = f'{URL}/login'

    def open_login_page(self):
        with allure.step(f'Открываем страницу {self.URL}'):
            self.open_page(self.URL)

    @allure.step('Ожидание загрузки страницы')
    def wait_loading_page(self):
        self.wait_visible_element(LoginPageLocators.BUTTON_ENTER)

    @allure.step("Клик на ссылку 'Восстановить пароль'")
    def click_link_recovery_password(self):
        self.click_by_element(LoginPageLocators.LINK_RECOVERY_PASSWORD)

    @allure.step("Заполнение поле 'E-mail'")
    def fill_email_field(self, email):
        self.fill_field(LoginPageLocators.INPUT_FIELD_EMAIL, email)

    @allure.step("Заполнение поле 'Password'")
    def fill_password_field(self, password):
        self.fill_field(LoginPageLocators.INPUT_FIELD_PASSWORD, password)

    @allure.step("Клик на кнопку 'Войти'")
    def click_button_enter(self):
        self.click_by_element(LoginPageLocators.BUTTON_ENTER)

    @allure.step("Вход в систему")
    def logining(self, login_details):
        self.fill_email_field(login_details['email'])
        self.fill_password_field(login_details['password'])
        self.click_button_enter()
