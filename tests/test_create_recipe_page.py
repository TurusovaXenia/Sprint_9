class TestCreateRecipePage:
    def test_create_recipe_success(self, authorized_user_on_recipes_page, header):
        create_recipe_page = header.go_to_create_recipe_page()
        create_recipe_page.fill_recipe_form()
        create_recipe_page.click_create_recipe_button()