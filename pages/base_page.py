from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def go_to_url(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def navigate_to(self, page_class):
        return page_class(self.driver)

    def wait_until_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_element_with_wait(self, locator):
        self.wait_until_visible(locator)
        return self.driver.find_element(*locator)

    def find_elements_with_wait(self, locator):
        self.wait.until(EC.visibility_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def fill_input(self, locator, text):
        self.wait_until_visible(locator)
        self.driver.find_element(*locator).send_keys(text)

    def get_text(self, locator):
        return self.find_element_with_wait(locator).text

    def upload_file_to_element(self, locator, file_path):
        self.driver.find_element(*locator).send_keys(file_path)

    def is_element_visible(self, locator):
        return self.driver.find_element(*locator).is_displayed()
