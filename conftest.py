import allure
import pytest
from selenium import webdriver

from pages.header import Header
from pages.login_page import LoginPage
from utils import helpers


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def header(driver):
    header = Header(driver)
    return header


@pytest.fixture
def login_page(driver):
    page = LoginPage(driver)
    return page


@pytest.fixture
def new_user_data():
    return helpers.generate_user_data()


@pytest.fixture
def registered_user(new_user_data, header, login_page):
    with allure.step("Подготовка пользователя"):
        login_page.open()
        create_account_page = header.go_to_create_account_page()
        create_account_page.fill_registration_form(new_user_data)
        create_account_page.click_create_account_button()

    return new_user_data


@pytest.fixture
def authorized_user_on_recipes_page(registered_user, login_page):
    with allure.step("Авторизация только что созданного пользователя"):
        login_page.open()
        login_page.fill_login_form(registered_user)
        recipe_page = login_page.click_login_button()

    return recipe_page
