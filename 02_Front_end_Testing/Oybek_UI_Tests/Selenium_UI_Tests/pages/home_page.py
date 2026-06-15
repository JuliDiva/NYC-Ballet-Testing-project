from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils import helper


class HomePage(BasePage):

    URL = "https://nycballetshop.com/"

    VIEW_ALL_BUTTON = (
        By.CSS_SELECTOR,
        'a[aria-label="View all products in the Homepage collection"]'
    )

    def open_homepage(self):
        self.open(self.URL)

    def verify_homepage_title(self):
        assert "nycballetshop.com" in self.driver.current_url

    def click_view_all(self):
        helper.scroll_to_bottom(self.driver)

        view_all_btn = helper.wait_for_element_clickable(
            self.driver,
            self.VIEW_ALL_BUTTON
        )

        view_all_btn.click()