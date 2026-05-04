import allure

import data


@allure.suite("Страница 'Создание рецепта'")
class TestCreateRecipePage:
    @allure.title("Проверка отображения карточки рецепта при успешном создании рецепта")
    def test_create_recipe_success(self, authorized_user_on_recipes_page, header):
        create_recipe_page = header.go_to_create_recipe_page()
        create_recipe_page.fill_recipe_form()
        recipe_data_page = create_recipe_page.click_create_recipe_button()

        with allure.step("Проверка созданного рецепта"):
            assert recipe_data_page.get_created_recipe_details() == {
                "is_correct_url": True,
                "title": data.recipe_data["name"],
                "cards_count": 1
            }
