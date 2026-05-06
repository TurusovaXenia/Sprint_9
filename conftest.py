import os

import allure
import pytest
from selenium import webdriver

from pages.header import Header
from pages.login_page import LoginPage
from utils import helpers


@pytest.fixture
def driver():
    selenoid_url = os.getenv("SELENOID_URL", "http://localhost:4444/wd/hub")

    options = webdriver.ChromeOptions()
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "128.0")
    options.set_capability("selenoid:options", {
        "enableVNC": True,  # Чтобы видеть экран в Selenoid UI
        "enableVideo": False
    })
    driver = webdriver.Remote(
        command_executor=selenoid_url,
        options=options
    )

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
def registered_user(header, login_page):
    with allure.step("Подготовить пользователя"):
        login_page.open()
        create_account_page = header.click_create_account_button()
        new_user_data = helpers.generate_user_data()
        create_account_page.fill_registration_form(new_user_data)
        create_account_page.click_create_account_button()

    return new_user_data


@pytest.fixture
def authorized_user_on_recipes_page(registered_user, login_page):
    with allure.step("Авторизировать только что созданного пользователя"):
        login_page.open()
        login_page.fill_login_form(registered_user)
        recipe_page = login_page.click_login_button()

    return recipe_page
