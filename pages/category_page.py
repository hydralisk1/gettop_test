from pages.base_page import Page
from selenium.webdriver.common.by import By


class CategoryPage(Page):
    CATEGORY_ON_ITEMS = (By.CSS_SELECTOR, "p.category")
    NAME_ON_ITEMS = (By.CSS_SELECTOR, "p.name > a")
    PRICE_ON_ITEMS = (By.CSS_SELECTOR, "span.price > span.amount")
    PRICE_INS_ON_ITEMS = (By.CSS_SELECTOR, "span.price > ins > span.amount")
    RESULT_MESSAGE = (By.CSS_SELECTOR, "p.woocommerce-result-count")
    RESULT_ITEMS = (By.CSS_SELECTOR, "div.product-small.box")
    QUICK_VIEWS = (By.CSS_SELECTOR, "a.quick-view")
    BUTTON_CLOSING_QUICK_VIEW = (By.CSS_SELECTOR, "button[title='Close (Esc)']")
    QUICK_VIEW_CONTAINER = (By.CSS_SELECTOR, "div.product-quick-view-container")
    ADD_TO_CART_FROM_QV = (By.CSS_SELECTOR, "button[name='add-to-cart']")
    PRODUCT_NAME_ON_QV = (By.CSS_SELECTOR, "h1")
    MESSAGE_ADD_TO_CART = (By.CSS_SELECTOR, "div.message-container")
    CART_ICON = (By.CSS_SELECTOR, "li.has-dropdown span.cart-icon")
    OUT_OF_STOCK = (By.CSS_SELECTOR, "p.out-of-stock")

    category = ""

    def open_category_page(self, category):
        if category.lower() == "watch" or category.lower() == "airpods":
            category = f"accessories/{category}"
            self.category = "accessories"
        else:
            self.category = category

        url = f"https://gettop.us/product-category/{category}"

        self.open_page(url)

    def verify_items_have_correct_category(self):
        categories_items_have = self.find_elements(*self.CATEGORY_ON_ITEMS)
        for category in categories_items_have:
            assert self.category.lower() == category.text.lower(), f"Expected category is {self.category}, but {category.text}"

    def verify_result_message(self):
        num_of_items = len(self.find_elements(*self.RESULT_ITEMS))
        expected_msg = f"Showing all {num_of_items} results"

        self.verify_text(expected_msg, *self.RESULT_MESSAGE)

    def verify_items_have(self):
        items = self.find_elements(*self.RESULT_ITEMS)

        for item in items:
            assert item.find_elements(*self.CATEGORY_ON_ITEMS), "An item doesn't have the category"
            assert item.find_elements(*self.NAME_ON_ITEMS), "An item doesn't have a name"
            if not item.find_elements(*self.PRICE_ON_ITEMS):
                assert item.find_elements(*self.PRICE_INS_ON_ITEMS), "An item doesn't have a price"

    def open_and_close_quick_view(self):
        quick_views = self.find_elements(*self.QUICK_VIEWS)

        for qv in quick_views:
            self.open_quick_view(qv)
            self.close_quick_view()

    def open_quick_view(self, qv):
        self.hover_over_element(qv)
        qv.click()
        self.wait_for_element_appear(*self.QUICK_VIEW_CONTAINER)
        assert self.find_elements(*self.QUICK_VIEW_CONTAINER), "Quick view didn't open"

    def close_quick_view(self):
        self.find_element(*self.BUTTON_CLOSING_QUICK_VIEW).click()
        self.wait_for_element_disappear(*self.QUICK_VIEW_CONTAINER)

    def add_product_from_quick_view_to_cart(self):
        quick_view_size = len(self.find_elements(*self.QUICK_VIEWS))

        for i in range(quick_view_size):
            qv = self.find_elements(*self.QUICK_VIEWS)[i]
            self.open_quick_view(qv)
            self.add_to_cart_from_qv()

    def add_to_cart_from_qv(self):
        # If this item isn't out of stock, add it to cart
        if not self.find_elements(*self.OUT_OF_STOCK):
            product = self.find_element(*self.PRODUCT_NAME_ON_QV).text

            expected_message = f'“{product}” has been added to your cart.'

            self.find_element(*self.ADD_TO_CART_FROM_QV).click()
            self.wait_for_element_disappear(*self.QUICK_VIEW_CONTAINER)
            self.verify_text(expected_message, *self.MESSAGE_ADD_TO_CART)
        # If this item is out of stock, just close this quick view
        else:
            self.close_quick_view()
