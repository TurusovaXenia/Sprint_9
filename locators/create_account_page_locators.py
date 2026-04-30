from selenium.webdriver.common.by import By


class CreateAccountPageLocators:
    FIRST_NAME = (By.CSS_SELECTOR, "input[name='first_name']")
    LAST_NAME = (By.CSS_SELECTOR, "input[name='last_name']")
    USERNAME = (By.CSS_SELECTOR, "input[name='username']")
    EMAIL = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD = (By.CSS_SELECTOR, "input[type='password']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Создать аккаунт']")
