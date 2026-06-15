from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):

    ADD_BUTTON_TEXT = (
        By.CSS_SELECTOR,
        'button[name="add"] span'
    )

    def get_add_button_text(self):
        return self.get_text(self.ADD_BUTTON_TEXT)

    def verify_sold_out_product(self):
        button_text = self.get_add_button_text()

        assert "Sold out" in button_text
        assert "Add to cart" not in button_text