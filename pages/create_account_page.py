from locators.create_account_page_locators import CreateAccountPageLocators
from pages.base_page import BasePage
from pages.login_page import LoginPage


class CreateAccountPage(BasePage):
    def fill_first_name_field(self, first_name):
        self.fill_input(CreateAccountPageLocators.FIRST_NAME, first_name)

    def fill_last_name_field(self, last_name):
        self.fill_input(CreateAccountPageLocators.LAST_NAME, last_name)

    def fill_username_field(self, username):
        self.fill_input(CreateAccountPageLocators.USERNAME, username)

    def fill_email_field(self, email):
        self.fill_input(CreateAccountPageLocators.EMAIL, email)

    def fill_password_field(self, password):
        self.fill_input(CreateAccountPageLocators.PASSWORD, password)

    def click_create_account_button(self):
        self.click_element(CreateAccountPageLocators.CREATE_ACCOUNT_BUTTON)
        return self.navigate_to(LoginPage)

    def fill_registration_form(self, user_data):
        self.fill_first_name_field(user_data['first_name'])
        self.fill_last_name_field(user_data['last_name'])
        self.fill_username_field(user_data['user_name'])
        self.fill_email_field(user_data['email'])
        self.fill_password_field(user_data['password'])
