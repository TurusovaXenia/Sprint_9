import allure


@allure.suite("Страница авторизации")
class TestLoginPage:
    @allure.title("Проверка успешной авторизации и перехода на страницу 'Рецепты'")
    def test_login_user_success(self, login_page, registered_user):
        login_page.open()
        login_page.fill_login_form(registered_user)
        recipes_page = login_page.click_login_button()

        assert recipes_page.is_recipes_page_visible(), \
            "Главная страница не открылась"
