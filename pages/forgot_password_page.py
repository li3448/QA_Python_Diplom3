import allure

from pages.base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from config import URL


class ForgotPasswordPage(BasePage):
    def __init__(self, web_drv):
        super().__init__(web_drv)
        self.URL = f'{URL}/forgot-password'

    def open_forgot_password_page(self):

        with allure.step(f'Открываем страницу {self.URL}'):
            self.open_page(self.URL)

    @allure.step("Заполнение полей 'E-mail'")
    def fill_email_field(self, email):
        self.fill_field(ForgotPasswordPageLocators.INPUT_FIELD_EMAIL, email)

    @allure.step("Клик на  кнопку 'Восстановить'")

        with allure.step(f'Открытие страницы {self.URL}'):
            self.open_page(self.URL)

    @allure.step("Заполнение поля 'E-mail'")
    def fill_email_field(self, email):
        self.fill_field(ForgotPasswordPageLocators.INPUT_FIELD_EMAIL, email)

    @allure.step("Нажатие кнопки 'Восстановить'")
    
    def click_button_recovery(self):
        self.click_by_element(ForgotPasswordPageLocators.BUTTON_RECOVERY)
