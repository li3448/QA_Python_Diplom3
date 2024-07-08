import allure

from pages.base_page import BasePage
from locators.reset_password_page_locators import ResetPasswordPageLocators
from config import URL


class ResetPasswordPage(BasePage):
    def __init__(self, web_drv):
        super().__init__(web_drv)
        self.URL = f'{URL}/reset-password'

    @property
    def inactive_border_of_field_password(self):
        return self.get_visible_element(ResetPasswordPageLocators.INACTIVE_BORDER_FIELD_PASSWORD)

    @allure.step('Ожидание загрузки страницы')
    def wait_load_page(self):
        self.wait_visible_element(ResetPasswordPageLocators.ICON_IN_FIELD_PASSWORD)

    @allure.step('Клик на кнопку скрыть/показать пароль')
    def click_icon_in_field_password(self):
        self.click_by_element(ResetPasswordPageLocators.ICON_IN_FIELD_PASSWORD)
