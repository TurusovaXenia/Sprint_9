import allure

from locators.header_locators import HeaderLocators
from locators.recipes_page_locators import RecipesPageLocators
from pages.base_page import BasePage


class RecipesPage(BasePage):
    @allure.step("Проверить переход на главную страницу и отображение кнопки 'Выход'")
    def is_recipes_page_visible(self):
        self.wait_until_visible(RecipesPageLocators.RECIPES_FORM)

        return (
                "/recipes" in self.get_current_url() and
                self.is_element_visible(HeaderLocators.LOGOUT_BUTTON)
        )
