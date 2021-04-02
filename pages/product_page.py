from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class ProductPage(Page):
    PRODUCT_PAGE_BASE_URL = "https://gettop.us/product/"
    BLOCK_TITLE = (By.CSS_SELECTOR, "h3.shop-sidebar")
    PRODUCTS_UNDER_BLOCK = (By.CSS_SELECTOR, "aside.widget span.product-title")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1.product-title")
    LINKS_UNDER_BLOCK = (By.CSS_SELECTOR, "aside.widget a")

    def open_product_page(self, product):
        self.open_page(self.PRODUCT_PAGE_BASE_URL + product)

    def verify_block(self, block_title):
        self.verify_text(block_title, *self.BLOCK_TITLE)

    def verify_products(self):
        products = self.find_elements(*self.PRODUCTS_UNDER_BLOCK)
        assert products, "There's nothing under the block"

    def verify_links(self):
        links = self.find_elements(*self.LINKS_UNDER_BLOCK)
        assert links, "There's no link under the block"

        for i in range(len(links)):
            current_link_selector = (By.CSS_SELECTOR, f"aside.widget li:nth-child({i+1}) > a")
            current_link = self.find_element(*current_link_selector)
            product_name = current_link.find_element(*(By.CSS_SELECTOR, "span.product-title")).text

            try:
                e = self.wait.until(EC.element_to_be_clickable(current_link_selector))
                e.click()
                self.verify_text(product_name, *self.PRODUCT_NAME)
                self.driver.back()

            except TimeoutException:
                assert False, f'''{product_name} link doesn't work'''
