import allure

from locators.create_account_page_locators import CreateAccountPageLocators
from pages.base_page import BasePage
from pages.login_page import LoginPage


class CreateAccountPage(BasePage):
    @allure.step("Заполнить поле 'Имя'")
    def fill_first_name_field(self, first_name):
        self.fill_input(CreateAccountPageLocators.FIRST_NAME, first_name)

    @allure.step("Заполнить поле 'Фамилия'")
    def fill_last_name_field(self, last_name):
        self.fill_input(CreateAccountPageLocators.LAST_NAME, last_name)

    @allure.step("Заполнить поле 'Имя пользователя'")
    def fill_username_field(self, username):
        self.fill_input(CreateAccountPageLocators.USERNAME, username)

    @allure.step("Заполнить поле 'Адрес электронной почты'")
    def fill_email_field(self, email):
        self.fill_input(CreateAccountPageLocators.EMAIL, email)

    @allure.step("Заполнить поле 'Пароль'")
    def fill_password_field(self, password):
        self.fill_input(CreateAccountPageLocators.PASSWORD, password)

    @allure.step("Клик кнопки 'Создать аккаунт'")
    def click_create_account_button(self):
        self.click_element(CreateAccountPageLocators.CREATE_ACCOUNT_BUTTON)
        return self.navigate_to(LoginPage)

    @allure.step("Заполнение формы регистрации")
    def fill_registration_form(self, user_data):
        self.fill_first_name_field(user_data['first_name'])
        self.fill_last_name_field(user_data['last_name'])
        self.fill_username_field(user_data['user_name'])
        self.fill_email_field(user_data['email'])
        self.fill_password_field(user_data['password'])
