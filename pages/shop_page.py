from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains


class ShopPage(Page):
    SELECT_BOX = (By.CSS_SELECTOR, "select.orderby")
    PRICES = (By.CSS_SELECTOR, "div.col.large-9 span.price")
    NORMAL_PRICES = (By.CSS_SELECTOR, "span")
    INS_PRICES = (By.CSS_SELECTOR, "ins > span")
    PAGE_NUMBERS = (By.CSS_SELECTOR, "a.page-number")
    SELECTED_OPTION = (By.CSS_SELECTOR, "option[selected='selected']")
    SLIDER_POINTERS = (By.CSS_SELECTOR, "span.ui-slider-handle")
    MIN_PRICE = (By.CSS_SELECTOR, "span.from")
    MAX_PRICE = (By.CSS_SELECTOR, "span.to")
    FILTER_BUTTON = (By.CSS_SELECTOR, "div.price_slider_wrapper button")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "div#shop-sidebar a.tooltipstered")
    PRICE_ON_FILTER = (By.CSS_SELECTOR, "span.amount")

    product_order = ""
    ASC_OPTION = "Sort by price: low to high"
    DESC_OPTION = "Sort by price: high to low"
    url = "https://gettop.us/shop"
    min_price = 190
    max_price = 2400

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

    def set_filter(self, min_price, max_price):
        try:
            min_price = int(min_price)
            max_price = int(max_price)
            if min_price < 190 or max_price < 240 or min_price > 2400 or max_price > 2400:
                raise ValueError
        except ValueError:
            assert False, "Prices have to be int type (190 <= min_value <= 2400, 240 <= max_value <= 2400"

        if max_price < min_price:
            min_price, max_price = max_price, min_price

        min_price -= min_price % 10
        max_price -= max_price % 10

        self.min_price = min_price
        self.max_price = max_price

        filter_min_price = int(self.find_element(*self.MIN_PRICE).text.replace("$", "").replace(",", ""))
        filter_max_price = int(self.find_element(*self.MAX_PRICE).text.replace("$", "").replace(",", ""))

        slide_pointers = self.find_elements(*self.SLIDER_POINTERS)
        start = slide_pointers[0].location['x'] - slide_pointers[1].location['x']
        offset_x = start + (-1 * start) * (min_price - filter_min_price) / (filter_max_price - filter_min_price)

        ActionChains(self.driver)\
            .click_and_hold(slide_pointers[0])\
            .move_to_element_with_offset(slide_pointers[1], offset_x, 0)\
            .perform()

        while self.find_element(*self.MIN_PRICE).text != f"${min_price:,}":
            offset_x += 1
            ActionChains(self.driver)\
                .click_and_hold(slide_pointers[0])\
                .move_to_element_with_offset(slide_pointers[1], offset_x, 0)\
                .perform()

        slide_pointers = self.find_elements(*self.SLIDER_POINTERS)

        start = slide_pointers[1].location['x'] - slide_pointers[0].location['x'] + 20
        offset_x = start - (start * (filter_max_price - max_price) / (filter_max_price - filter_min_price))

        ActionChains(self.driver) \
            .click_and_hold(slide_pointers[1]) \
            .move_to_element_with_offset(slide_pointers[0], offset_x, 0) \
            .perform()

        while self.find_element(*self.MAX_PRICE).text != f"${max_price:,}":
            offset_x -= 1
            ActionChains(self.driver)\
                .click_and_hold(slide_pointers[1])\
                .move_to_element_with_offset(slide_pointers[0], offset_x, 0)\
                .perform()

    def click_filter_button(self):
        self.click(*self.FILTER_BUTTON)

    def verify_price_filter(self):
        self.verify_remove_button()
        # Find how many pages in the shop page
        pages = self.find_elements(*self.PAGE_NUMBERS)

        # Loop for pages
        for i in range(len(pages)):
            # Loop for prices
            for span in self.find_elements(*self.PRICES):
                price = span.find_elements(*self.INS_PRICES)
                # If a price in ins tag, store it to price variable
                # and transform it to float type in order to compare
                product_price = float(price[0].text.replace(",", "").replace("$", ""))\
                    if price\
                    else float(span.find_element(*self.NORMAL_PRICES).text.replace(",", "").replace("$", ""))

                assert self.min_price <= product_price <= self.max_price, "The price filter doesn't work"

            # if there's another page, click it to move to the next page
            if i+1 < len(pages):
                pages[i+1].click()

    def verify_remove_button(self):
        buttons = self.find_elements(*self.REMOVE_BUTTON)

        if len(buttons) == 2:
            min_price = buttons[0].find_element(*self.PRICE_ON_FILTER).text.split(".")[0]
            max_price = buttons[1].find_element(*self.PRICE_ON_FILTER).text.split(".")[0]
        elif len(buttons) == 1:
            if buttons[0].text == "Min":
                min_price = buttons[0].find_element(*self.PRICE_ON_FILTER).text.split(".")[0]
                max_price = "$2,400"
            else:
                max_price = buttons[0].find_element(*self.PRICE_ON_FILTER).text.split(".")[0]
                min_price = "$190"
        else:
            min_price = "$190"
            max_price = "$2,400"

        assert min_price == f"${self.min_price:,}", f"Expected minimum price on the remove button is ${self.min_price:,}, but actual price is {min_price}"
        assert max_price == f"${self.max_price:,}", f"Expected maximum price on the remove button is ${self.max_price:,}, but actual price is {max_price}"

    def click_x_button(self, which):
        buttons = self.find_elements(*self.REMOVE_BUTTON)
        if which == "minimum":
            self.min_price = 190
            buttons[0].click()
        else:
            self.max_price = 2400
            buttons[-1].click()

    def verify_price_filter_handle(self, which):
        handle = self.find_elements(*self.SLIDER_POINTERS)
        error_msg = " price filter slider handle wasn't back"
        # if minimum filter has been removed
        if which == "minimum":
            # the handle's style would be left: 0%;
            assert handle[0].get_attribute("style") == "left: 0%;", which + error_msg
        else:
            # if maximum filter has been removed
            # the handle's style would be left: 100%;
            assert handle[1].get_attribute("style") == "left: 100%;", which + error_msg
