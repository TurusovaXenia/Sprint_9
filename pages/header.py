from locators.header_locators import HeaderLocators
from pages.base_page import BasePage
from pages.create_account_page import CreateAccountPage
from pages.create_recipe_page import CreateRecipePage


class Header(BasePage):
    def go_to_create_account_page(self):
        self.click_element(HeaderLocators.CREATE_ACCOUNT_BUTTON)
        return self.navigate_to(CreateAccountPage)

    def go_to_create_recipe_page(self):
        self.click_element(HeaderLocators.CREATE_RECIPE_BUTTON)
        return self.navigate_to(CreateRecipePage)
