import urls
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from pages.recipes_page import RecipesPage


class LoginPage(BasePage):
    def open(self):
        self.go_to_url(urls.BASE_URL)

    def fill_username_field(self, username):
        self.fill_input(LoginPageLocators.USERNAME_INPUT, username)

    def fill_password_field(self, password):
        self.fill_input(LoginPageLocators.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)
        return self.navigate_to(RecipesPage)

    def fill_login_form(self, user_data):
        self.fill_username_field(user_data['user_name'])
        self.fill_password_field(user_data['password'])

    def is_login_form_visible(self):
        self.wait_until_visible(LoginPageLocators.LOGIN_FORM)

        return (
                urls.BASE_URL == self.get_current_url() and
                self.is_element_visible(LoginPageLocators.LOGIN_FORM) and
                self.is_element_visible(LoginPageLocators.USERNAME_INPUT)
        )
