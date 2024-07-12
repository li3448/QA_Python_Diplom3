import pytest
import requests
import allure

from selenium import webdriver
from faker import Faker

from pages.index_page import IndexPage
from pages.login_page import LoginPage
from pages.orders_feed_page import OrdersFeedPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
from pages.account_profile_page import AccountProfilePage
from pages.account_order_history_page import AccountOrderHistoryPage
from pages.header import Header
from config import URL
from config import Browsers
from helpers import create_order


@pytest.fixture()
def user():
    fake = Faker()
    payload = {
        "email": f'ake2014{fake.email()}',
        "password": fake.password(),
        "name": fake.user_name()
    }
    yield payload


@pytest.fixture()
def create_user(user):
    try:
        with allure.step('Отправляем запрос на создание пользователя'):
            response = requests.post(f'https://stellarburgers.nomoreparties.site/api/auth/register', json=user)
            response.raise_for_status()
    except requests.RequestException as e:
        raise e
    else:
        access_token = response.json()['accessToken']
        del user['name']

        yield user, access_token


@pytest.fixture()
def delete_user(create_user):
    user, access_token = create_user
    headers = {"Authorization": access_token}
    try:
        with allure.step('Отправляем запрос на удаление пользователя'):
            requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user", headers=headers)
    except requests.RequestException as e:
        raise e

@pytest.fixture(params=[Browsers.CHROME, Browsers.FIREFOX])
def web_drv(request):
    with allure.step(f'Инициализируем драйвер браузера {request.param}'):
        if request.param == Browsers.CHROME:
            driver = webdriver.Chrome()
        elif request.param == Browsers.FIREFOX:
            driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(URL)

    yield driver

    with allure.step(f'Зарываем браузер - {request.param}'):
        driver.quit()


@pytest.fixture()
def index_page(web_drv):
    return IndexPage(web_drv)


@pytest.fixture()
def login_page(web_drv):
    return LoginPage(web_drv)


@pytest.fixture()
def order_feed_page(web_drv):
    return OrdersFeedPage(web_drv)


@pytest.fixture()
def forgot_password_page(web_drv):
    return ForgotPasswordPage(web_drv)


@pytest.fixture()
def reset_password_page(web_drv):
    return ResetPasswordPage(web_drv)


@pytest.fixture()
def account_profile_page(web_drv):
    return AccountProfilePage(web_drv)


@pytest.fixture()
def account_order_history_page(web_drv):
    return AccountOrderHistoryPage(web_drv)


@pytest.fixture()
def header(web_drv):
    return Header(web_drv)


@pytest.fixture()
def logged(login_page, user):
    login_page.open_login_page()
    login_page.logining(user)


@pytest.fixture()
def order(request, user, logged, index_page):
    orders_count = request.node.get_closest_marker('orders_count').args[0]
    for _ in range(orders_count):
        create_order(index_page)
