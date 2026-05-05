import allure

import urls
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from pages.recipes_page import RecipesPage


class LoginPage(BasePage):
    @allure.step("Открыть страницу 'Логин'")
    def open(self):
        self.go_to_url(urls.BASE_URL)

    @allure.step("Заполнить поле 'Имя пользователя'")
    def fill_username_field(self, username):
        self.fill_input(LoginPageLocators.USERNAME_INPUT, username)

    @allure.step("Заполнить поле 'Пароль'")
    def fill_password_field(self, password):
        self.fill_input(LoginPageLocators.PASSWORD_INPUT, password)

    @allure.step("Клик кнопки 'Войти'")
    def click_login_button(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)
        return self.navigate_to(RecipesPage)

    @allure.step("Заполнить форму авторизации")
    def fill_login_form(self, user_data):
        self.fill_username_field(user_data['user_name'])
        self.fill_password_field(user_data['password'])

    @allure.step("Проверить отображение формы авторизации")
    def is_login_form_visible(self):
        self.wait_until_visible(LoginPageLocators.LOGIN_FORM)

        return (
                urls.BASE_URL == self.get_current_url() and
                self.is_element_visible(LoginPageLocators.LOGIN_FORM) and
                self.is_element_visible(LoginPageLocators.USERNAME_INPUT)
        )
