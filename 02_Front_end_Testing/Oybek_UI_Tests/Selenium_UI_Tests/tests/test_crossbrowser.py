import unittest

from selenium.webdriver.common.by import By

from pages.home_page import HomePage
from pages.collection_page import CollectionPage
from pages.product_page import ProductPage
from utils.helper import create_driver, close_driver


class NYCBShopTestsMixin:

    def open_collection_page(self):
        home_page = HomePage(self.driver)
        collection_page = CollectionPage(self.driver)

        home_page.open_homepage()
        home_page.verify_homepage_title()
        home_page.click_view_all()

        collection_page.wait_for_product_grid()

        return collection_page

    # ============================================================
    # POSITIVE TEST CASES
    # ============================================================

    def test_TC_P_01_view_all_button(self):
        print("\n========== TC_P_01 | View All Button ==========")

        collection_page = self.open_collection_page()

        self.assertTrue(
            collection_page.is_displayed(collection_page.PRODUCT_GRID)
        )

        print("View All button is visible and collection page opened")

    def test_TC_P_02_sort_by_best_selling(self):
        print("\n========== TC_P_02 | Sort By Best Selling ==========")

        collection_page = self.open_collection_page()
        collection_page.select_best_selling()

        self.assertTrue(
            collection_page.is_displayed(collection_page.SORT_BY_DROPDOWN)
        )

        print("Best Selling option selected")

    def test_TC_P_03_availability_filter(self):
        print("\n========== TC_P_03 | Availability Filter ==========")

        collection_page = self.open_collection_page()
        collection_page.select_best_selling()
        collection_page.open_availability_filter()
        collection_page.select_in_stock()

        self.assertTrue(
            collection_page.is_displayed(collection_page.PRODUCT_GRID)
        )

        print("Availability filter and In Stock checkbox work")

    def test_TC_P_04_add_to_cart_visibility(self):
        print("\n========== TC_P_04 | Add To Cart Visibility ==========")

        collection_page = self.open_collection_page()
        collection_page.select_best_selling()
        collection_page.open_availability_filter()
        collection_page.select_in_stock()

        self.assertTrue(collection_page.is_add_to_cart_visible())

        print("Add to Cart button is visible")

    def test_TC_P_05_product_count_displayed(self):
        print("\n========== TC_P_05 | Product Count Display ==========")

        collection_page = self.open_collection_page()
        collection_page.select_best_selling()
        collection_page.open_availability_filter()
        collection_page.select_in_stock()

        self.assertTrue(collection_page.is_product_count_visible())

        print("Product count is visible")

    # ============================================================
    # NEGATIVE TEST CASES
    # ============================================================

    def test_TC_N_01_product_without_name(self):
        print("\n========== TC_N_01 | Product Without Name ==========")

        collection_page = self.open_collection_page()

        product_cards = collection_page.get_product_cards()
        self.assertGreaterEqual(len(product_cards), 4)

        for i in range(4):
            product_name = product_cards[i].find_element(By.CSS_SELECTOR, "h3")

            self.assertTrue(product_name.is_displayed())
            self.assertRegex(product_name.text, r"\S+")

        print("First 4 product names are visible and not empty")

    def test_TC_N_02_product_without_img(self):
        print("\n========== TC_N_02 | Product Without Image ==========")

        collection_page = self.open_collection_page()

        product_cards = collection_page.get_product_cards()
        self.assertGreaterEqual(len(product_cards), 4)

        for i in range(4):
            product_img = product_cards[i].find_element(
                By.CSS_SELECTOR,
                "img.motion-reduce"
            )

            self.assertTrue(product_img.is_displayed())
            self.assertRegex(product_img.get_attribute("src"), r"\S+")

        print("First 4 product images are visible")

    def test_TC_N_03_unavailable_product_cannot_be_added_to_cart(self):
        print("\n========== TC_N_03 | Unavailable Product Cannot Be Added To Cart ==========")

        collection_page = self.open_collection_page()
        product_page = ProductPage(self.driver)

        collection_page.open_availability_filter()
        collection_page.select_out_of_stock()
        collection_page.open_sold_out_product()

        product_page.verify_sold_out_product()

        print("Unavailable product cannot be added to cart")

    def test_TC_N_04_incorrect_currency_symbols(self):
        print("\n========== TC_N_04 | Incorrect Currency Symbols ==========")

        collection_page = self.open_collection_page()

        price_text = collection_page.get_price_text()

        self.assertNotIn("€", price_text)
        self.assertNotIn("£", price_text)
        self.assertNotIn("¥", price_text)
        self.assertTrue(price_text.startswith("$"))

        print("Price is displayed with correct US currency symbol")

    def test_TC_N_05_duplicate_products_not_displayed(self):
        print("\n========== TC_N_05 | Duplicate Products Not Displayed ==========")

        collection_page = self.open_collection_page()

        product_names = collection_page.get_product_names()

        self.assertGreater(len(product_names), 0)
        self.assertEqual(len(product_names), len(set(product_names)))

        print("Duplicate products are not displayed")


class ChromeNYCBShopTest(NYCBShopTestsMixin, unittest.TestCase):
    browser_name = "Chrome"

    def setUp(self):
        print(f"\n\n===== RUNNING TEST ON: {self.browser_name} =====")
        self.driver = create_driver("chrome")

    def tearDown(self):
        close_driver(self.driver)


class FireFoxNYCBShopTest(NYCBShopTestsMixin, unittest.TestCase):
    browser_name = "Firefox"

    def setUp(self):
        print(f"\n\n===== RUNNING TEST ON: {self.browser_name} =====")
        self.driver = create_driver("firefox")

    def tearDown(self):
        close_driver(self.driver)


class EdgeNYCBShopTest(NYCBShopTestsMixin, unittest.TestCase):
    browser_name = "Edge"

    def setUp(self):
        print(f"\n\n===== RUNNING TEST ON: {self.browser_name} =====")
        self.driver = create_driver("edge")

    def tearDown(self):
        close_driver(self.driver)


if __name__ == "__main__":
    unittest.main()