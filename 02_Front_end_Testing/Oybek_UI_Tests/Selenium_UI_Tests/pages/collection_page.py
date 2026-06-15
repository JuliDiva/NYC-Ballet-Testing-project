from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

from pages.base_page import BasePage
from utils import helper


class CollectionPage(BasePage):

    PRODUCT_GRID = (By.CSS_SELECTOR, "#product-grid")

    SORT_BY_DROPDOWN = (
        By.CSS_SELECTOR,
        'div[class="select"] > select[id="SortBy"]'
    )

    AVAILABILITY_FILTER = (
        By.XPATH,
        '//*[@class="facets__summary caption-large focus-offset"]/descendant::*[text()="Availability"]'
    )

    IN_STOCK_CHECKBOX = (
        By.CSS_SELECTOR,
        'label[for="Filter-Availability-1"]'
    )

    OUT_OF_STOCK_CHECKBOX = (
        By.CSS_SELECTOR,
        'label[for="Filter-Availability-2"]'
    )

    ADD_TO_CART_BUTTON = (
        By.CSS_SELECTOR,
        '*[value="Add to cart  "]'
    )

    PRODUCT_COUNT = (
        By.CSS_SELECTOR,
        "#ProductCountDesktop"
    )

    PRODUCT_CARDS = (
        By.CSS_SELECTOR,
        ".grid__item"
    )

    PRODUCT_NAMES = (
        By.CSS_SELECTOR,
        "h3.card-information__text a"
    )

    PRICE = (
        By.CSS_SELECTOR,
        "div.price__regular span.price-item--regular"
    )

    SOLD_OUT_BADGE = (
        By.XPATH,
        '//*[contains(text(), "Sold out")]'
    )

    def wait_for_product_grid(self):
        return self.get_element(self.PRODUCT_GRID)

    def select_best_selling(self):
        dropdown = self.get_element(self.SORT_BY_DROPDOWN)

        dropdown.click()
        dropdown.send_keys("Best selling")
        dropdown.send_keys(Keys.ENTER)

    def open_availability_filter(self):
        self.click(self.AVAILABILITY_FILTER)

    def select_in_stock(self):
        self.click(self.IN_STOCK_CHECKBOX)
        self.driver.find_element(By.TAG_NAME, "body").click()

    def select_out_of_stock(self):
        self.click(self.OUT_OF_STOCK_CHECKBOX)
        self.driver.find_element(By.TAG_NAME, "body").click()

    def is_add_to_cart_visible(self):
        helper.scroll_to_bottom(self.driver)
        return self.is_displayed(self.ADD_TO_CART_BUTTON)

    def is_product_count_visible(self):
        return self.is_displayed(self.PRODUCT_COUNT)

    def get_product_cards(self):
        return self.driver.find_elements(*self.PRODUCT_CARDS)

    def get_product_names(self):
        product_name_elements = self.driver.find_elements(*self.PRODUCT_NAMES)

        names = []

        for product in product_name_elements:
            name = product.text.strip()

            if name:
                names.append(name)

        return names

    def get_price_text(self):
        return self.get_text(self.PRICE).strip()

    def open_sold_out_product(self):
        sold_out_badge = self.get_element(self.SOLD_OUT_BADGE)

        sold_out_product = sold_out_badge.find_element(
            By.XPATH,
            "./ancestor::li"
        )

        sold_out_product.click()