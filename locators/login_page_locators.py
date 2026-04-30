from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME_INPUT = (By.CSS_SELECTOR, "input[type='text']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    LOGIN_FORM = (By.XPATH, ".//h1[text()='Войти на сайт']")

