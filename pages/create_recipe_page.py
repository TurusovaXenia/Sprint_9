import data
from locators.create_recipe_page_locators import CreateRecipePageLocators
from pages.base_page import BasePage
from utils import helpers


class CreateRecipePage(BasePage):
    def fill_recipe_name(self, recipe_name):
        self.fill_input(CreateRecipePageLocators.RECIPE_NAME, recipe_name)

    def select_ingredient(self, ingredient_name):
        self.fill_input(CreateRecipePageLocators.INGREDIENT_DROPDOWN, ingredient_name)
        self.click_element(CreateRecipePageLocators.SELECTED_INGREDIENT)

    def click_add_ingredient_button(self):
        self.click_element(CreateRecipePageLocators.ADD_INGREDIENT_BUTTON)

    def fill_ingredient_grams(self, grams):
        self.fill_input(CreateRecipePageLocators.GRAMS_INPUT, grams)

    def fill_time_of_cooking(self, time):
        self.fill_input(CreateRecipePageLocators.TIME_INPUT, time)

    def fill_recipe_description(self, recipe_description):
        self.fill_input(CreateRecipePageLocators.RECIPE_DESCRIPTION, recipe_description)

    def upload_recipe_foto(self, file_path):
        self.upload_file_to_element(CreateRecipePageLocators.UPLOAD_FILE_BUTTON, file_path)

    def click_create_recipe_button(self):
        self.click_element(CreateRecipePageLocators.CREATE_RECIPE)

    def fill_recipe_form(self):
        self.fill_recipe_name(data.recipe_data["name"])
        self.select_ingredient(data.recipe_data["ingredient_name"])
        self.fill_ingredient_grams(data.recipe_data["ingredient_gram"])
        self.click_add_ingredient_button()
        self.fill_time_of_cooking(data.recipe_data["time"])
        self.fill_recipe_description(data.recipe_data["description"])
        self.upload_recipe_foto(helpers.get_upload_file_path("bee.png"))
