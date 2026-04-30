from selenium.webdriver.common.by import By


class CreateRecipePageLocators:
    RECIPE_NAME = (By.XPATH, ".//div[text()='Название рецепта']/following-sibling::input[1]")
    INGREDIENT_DROPDOWN = (By.XPATH, ".//div[text()='Ингредиенты']/following-sibling::input[1]")
    SELECTED_INGREDIENT = (By.XPATH, ".//div[contains(@class, 'ingredientsInputs')]/div[contains(@class, 'styles_container')]")
    GRAMS_INPUT = (By.CSS_SELECTOR, "input[class*='Amount']")
    ADD_INGREDIENT_BUTTON = (By.CSS_SELECTOR, "div[class*='styles_ingredientAdd']")
    TIME_INPUT = (By.XPATH, "//div[text()='Время приготовления']/following-sibling::input[1]")
    RECIPE_DESCRIPTION = (By.CSS_SELECTOR, "textarea[class*= 'textareaField']")
    UPLOAD_FILE_BUTTON = (By.CSS_SELECTOR, "input[class*='styles_fileInput']")
    CREATE_RECIPE = (By.XPATH, ".//button[text()='Создать рецепт']")
