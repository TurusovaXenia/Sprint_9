from selenium.webdriver.common.by import By


class CreateAccountPageLocators:
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[name='first_name']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[name='last_name']")
    USERNAME_INPUT = (By.CSS_SELECTOR, "input[name='username']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Создать аккаунт']")
