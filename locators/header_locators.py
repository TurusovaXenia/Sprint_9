from selenium.webdriver.common.by import By


class HeaderLocators:
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "a[class*='menuButton']")
    LOGOUT_BUTTON = (By.XPATH, ".//a[text()='Выход']")
    CREATE_RECIPE_BUTTON = (By.XPATH, ".//a[text()='Создать рецепт']")
