import allure

from locators.recipe_data_page_locators import RecipeDataPageLocators
from pages.base_page import BasePage


class RecipeDataPage(BasePage):
    @allure.step("Получить детали о созданном рецепте")
    def get_created_recipe_details(self):
        self.wait_until_visible(RecipeDataPageLocators.RECIPE_TITLE)

        return {
            "is_correct_url": '/recipes/' in self.get_current_url(),
            "title": self.get_text(RecipeDataPageLocators.RECIPE_TITLE),
            "cards_count": len(self.find_elements_with_wait(RecipeDataPageLocators.RECIPE_CARDS))
        }
