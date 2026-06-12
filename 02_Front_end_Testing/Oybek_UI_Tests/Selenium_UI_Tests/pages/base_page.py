from utils.helper import (
    wait_for_element_visible,
    wait_for_element_clickable,
)


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        element = wait_for_element_clickable(self.driver, locator)
        element.click()

    def get_element(self, locator):
        return wait_for_element_visible(self.driver, locator)

    def is_displayed(self, locator):
        return self.get_element(locator).is_displayed()

    def get_text(self, locator):
        return self.get_element(locator).text