from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ShopPage(Page):
    SELECT_BOX = (By.CSS_SELECTOR, "select.orderby")
    PRICES = (By.CSS_SELECTOR, "div.col.large-9 span.price")
    NORMAL_PRICES = (By.CSS_SELECTOR, "span")
    INS_PRICES = (By.CSS_SELECTOR, "ins > span")
    PAGE_NUMBERS = (By.CSS_SELECTOR, "a.page-number")
    SELECTED_OPTION = (By.CSS_SELECTOR, "option[selected='selected']")
    product_order = ""
    ASC_OPTION = "Sort by price: low to high"
    DESC_OPTION = "Sort by price: high to low"
    url = "https://gettop.us/shop"

    def open_shop_page(self):
        self.open_page(self.url)

    def open_shop_page_directly(self, direct_link):
        self.product_order = self.DESC_OPTION\
            if direct_link == "?orderby=price-desc"\
            else self.ASC_OPTION
        self.open_page(f"{self.url}/{direct_link}")

    def choose_one_from_select_box(self, option):
        select_box = Select(self.find_element(*self.SELECT_BOX))
        select_box.select_by_visible_text(option)
        self.product_order = option

    def verify_products_in_correct_order(self):
        # Check the sort order
        # Currently, sort by price only supported
        order = self.product_order
        # Find how many pages in the shop page
        pages = self.find_elements(*self.PAGE_NUMBERS)
        pre_price = 0
        # Test fail massage
        fail_message = "Product prices are not in correct order"

        # Loop for pages
        for i in range(len(pages)):
            # Loop for prices
            for span in self.find_elements(*self.PRICES):
                price = span.find_elements(*self.INS_PRICES)
                # If a price in ins tag, store it to price variable
                # and transform it to float type in order to compare
                this_price = float(price[0].text.replace(",", "").replace("$", ""))\
                    if price\
                    else float(span.find_element(*self.NORMAL_PRICES).text.replace(",", "").replace("$", ""))

                # If previous price doesn't exist, don't compare it
                # because it's the first price
                if pre_price != 0:
                    # Depending on sort order, compare previous price to current price
                    # in order to verify they're in correct order
                    if order == self.DESC_OPTION:
                        assert pre_price >= this_price, fail_message
                    elif order == self.ASC_OPTION:
                        assert pre_price <= this_price, fail_message

                # Set the current price to previous price
                pre_price, this_price = this_price, 0

            # if there's another page, click it to move to the next page
            if i+1 < len(pages):
                pages[i+1].click()

    def verify_option(self):
        order = self.product_order
        self.verify_text(order, *self.SELECTED_OPTION)
