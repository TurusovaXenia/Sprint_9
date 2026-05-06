from selenium.webdriver.common.by import By


class RecipeDataPageLocators:
    RECIPE_CARDS = (By.CSS_SELECTOR, "div[class*='style_container'] > div[class*='styles_single-card']")
    RECIPE_TITLE = (By.CSS_SELECTOR, "h1[class*='styles_single-card__title']")
