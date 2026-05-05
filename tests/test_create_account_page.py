import allure


@allure.suite("Страница 'Создание аккаунта'")
class TestCreateAccountPage:
    @allure.title("Проверка перехода на страницу авторизации при успешном создании аккаунта")
    def test_create_account_success(self, login_page, header, new_user_data):
        login_page.open()
        create_account_page = header.click_create_account_button()
        create_account_page.fill_registration_form(new_user_data)
        login_page_after_reg = create_account_page.click_create_account_button()

        assert login_page_after_reg.is_login_form_visible(), \
            "Форма авторизации не отображается на странице"
