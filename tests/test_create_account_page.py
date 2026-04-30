class TestCreateAccountPage:
    def test_create_account_success(self, login_page, header, new_user_data):
        login_page.open()
        create_account_page = header.go_to_create_account_page()
        create_account_page.fill_registration_form(new_user_data)
        success_page = create_account_page.click_create_account_button()

        assert success_page.is_login_form_visible(), \
            "Форма авторизации не отображается на странице"
