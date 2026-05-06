import allure
from utils import helpers

@allure.suite("Страница 'Создание аккаунта'")
class TestCreateAccountPage:
    @allure.title("Проверка перехода на страницу авторизации при успешном создании аккаунта")
    def test_create_account_success(self, login_page, header):
        login_page.open()
        create_account_page = header.click_create_account_button()
        new_user_data = helpers.generate_user_data()
        create_account_page.fill_registration_form(new_user_data)
        login_page_after_reg = create_account_page.click_create_account_button()

        assert login_page_after_reg.is_login_form_visible(), \
            "Форма авторизации не отображается на странице"
