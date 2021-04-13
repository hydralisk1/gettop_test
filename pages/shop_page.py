from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains


class ShopPage(Page):
    SELECT_BOX = (By.CSS_SELECTOR, "select.orderby")
    PRICES = (By.CSS_SELECTOR, "div.col.large-9 span.price")
    NORMAL_PRICES = (By.CSS_SELECTOR, "span")
    INS_PRICES = (By.CSS_SELECTOR, "ins > span")
    CATEGORIES = (By.CSS_SELECTOR, "p.category")
    PAGE_NUMBERS = (By.CSS_SELECTOR, "a.page-number")
    SELECTED_OPTION = (By.CSS_SELECTOR, "option[selected='selected']")
    SLIDER_POINTERS = (By.CSS_SELECTOR, "span.ui-slider-handle")
    MIN_PRICE = (By.CSS_SELECTOR, "span.from")
    MAX_PRICE = (By.CSS_SELECTOR, "span.to")
    FILTER_BUTTON = (By.CSS_SELECTOR, "div.price_slider_wrapper button")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "div#shop-sidebar a.tooltipstered")
    PRICE_ON_FILTER = (By.CSS_SELECTOR, "span.amount")
    PRODUCT_LINKS = (By.CSS_SELECTOR, "div.image-fade_in_back > a")
    PRODUCT_NAMES = (By.CSS_SELECTOR, "p.product-title > a")
    VIEWED_ITEMS = (By.CSS_SELECTOR, "aside span.product-title")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "h1.product-title")
    NO_PRODUCT_MSG = (By.CSS_SELECTOR, "p.woocommerce-info")
    CATEGORIES_UNDER_BROWSE = (By.CSS_SELECTOR, "li.cat-item > a")
    ACC_CAT_TOGGLE_BTN = (By.CSS_SELECTOR, "li.cat-item > button.toggle")

    product_order = ""
    ASC_OPTION = "Sort by price: low to high"
    DESC_OPTION = "Sort by price: high to low"
    url = "https://gettop.us/shop"
    min_price = 190
    max_price = 2400
    recently_viewed_item = ""

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

        self.set_min_slider(min_price)
        self.set_max_slider(max_price)

    def set_min_slider(self, min_price):
        slide_pointers = self.find_elements(*self.SLIDER_POINTERS)

        filter_min_price = self.currency_to_int(self.find_element(*self.MIN_PRICE).text)
        filter_max_price = self.currency_to_int(self.find_element(*self.MAX_PRICE).text)

        start = slide_pointers[0].location['x'] - slide_pointers[1].location['x']
        offset_x = start * (1 - (min_price-filter_min_price)/(filter_max_price-filter_min_price))

        self.slide_to(slide_pointers[0], slide_pointers[1], offset_x)

        current_filter_min = self.currency_to_int(self.find_element(*self.MIN_PRICE).text.replace("$", ""))

        while min_price != current_filter_min:
            offset_x = offset_x - 1 if current_filter_min > min_price else offset_x + 1
            self.slide_to(slide_pointers[0], slide_pointers[1], offset_x)
            current_filter_min = self.currency_to_int(self.find_element(*self.MIN_PRICE).text.replace("$", ""))

    def set_max_slider(self, max_price):
        slide_pointers = self.find_elements(*self.SLIDER_POINTERS)

        filter_min_price = int(self.find_element(*self.MIN_PRICE).text.replace("$", "").replace(",", ""))
        filter_max_price = int(self.find_element(*self.MAX_PRICE).text.replace("$", "").replace(",", ""))

        start = slide_pointers[1].location['x'] - slide_pointers[0].location['x']
        offset_x = start * (1 - (filter_max_price - max_price) / (filter_max_price - filter_min_price))

        self.slide_to(slide_pointers[1], slide_pointers[0], offset_x)

        current_filter_max = self.currency_to_int(self.find_element(*self.MAX_PRICE).text.replace("$", ""))
        while max_price != current_filter_max:
            offset_x = offset_x - 1 if current_filter_max > max_price else offset_x + 1
            self.slide_to(slide_pointers[1], slide_pointers[0], offset_x)
            current_filter_max = self.currency_to_int(self.find_element(*self.MAX_PRICE).text.replace("$", ""))

    def slide_to(self, start, to, offset_x):
        ActionChains(self.driver)\
            .click_and_hold(start)\
            .move_to_element_with_offset(to, offset_x, 0)\
            .release()\
            .perform()

    def click_filter_button(self):
        self.click(*self.FILTER_BUTTON)

    def verify_price_filter(self):
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

                assert self.min_price <= product_price <= self.max_price, f"The price has to be between ${self.min_price} - ${self.max_price}, but {product_price}"

            # if there's another page, click it to move to the next page
            if i+1 < len(pages):
                pages[i+1].click()

    def click_x_button(self, which):
        buttons = self.find_elements(*self.REMOVE_BUTTON)
        button_text = {"minimum": "Min", "maximum": "Max"}

        if which == "minimum":
            self.min_price = 190
        else:
            self.max_price = 2400

        for button in buttons:
            if button.text.split()[0] == button_text[which]:
                button.click()
                break

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

    def click_product(self, number):
        num = int(number[:-2]) - 1
        self.recently_viewed_item = self.find_elements(*self.PRODUCT_NAMES)[num].text
        self.find_elements(*self.PRODUCT_LINKS)[num].click()

    def verify_recently_viewed_item(self):
        viewed_item = self.find_elements(*self.VIEWED_ITEMS)[0].text
        assert self.recently_viewed_item == viewed_item, f"{self.recently_viewed_item} is not on the top in the list"

    def click_viewed_item(self):
        self.find_elements(*self.VIEWED_ITEMS)[0].click()

    def verify_page(self):
        self.verify_text(self.recently_viewed_item, *self.PRODUCT_TITLE)

    def verify_no_product(self, message):
        products = self.find_elements(*self.PRODUCT_NAMES)
        if len(products) == 0:
            self.verify_text(message, *self.NO_PRODUCT_MSG)
        else:
            for product in products:
                print(product, end=" ")
            print("exist")

    def verify_correct_categories_under_browse(self):
        correct_categories = ["Accessories", "AirPods", "Watch", "iPad", "iPhone", "MacBook"]
        self.find_element(*self.ACC_CAT_TOGGLE_BTN).click()

        categories_under_browse = self.find_elements(*self.CATEGORIES_UNDER_BROWSE)

        for category in categories_under_browse:
            category_name = category.text
            assert category_name in correct_categories, f"{category_name} is not a correct category"

    def verify_correct_page_under_browse(self):
        num_of_cat = len(self.find_elements(*self.CATEGORIES_UNDER_BROWSE))

        for i in range(num_of_cat):
            current_category = self.find_elements(*self.CATEGORIES_UNDER_BROWSE)[i]
            category_name = current_category.text
            current_category.click()
            self.verify_category(category_name)

    def verify_category(self, category_name):
        categories = self.find_elements(*self.CATEGORIES)

        for i, category in enumerate(categories):
            # If current category is sub category of Accessories,
            # Check if current product name includes current sub category
            if category_name.lower() == "airpods" or category_name.lower() == "watch":
                product_name = self.find_elements(*self.PRODUCT_NAMES)[i].text
                assert category.text.lower() == "accessories", f"Expected category is Accessories, but actual is {category.text}"
                assert category_name in product_name, f"{category_name} is not included in {product_name}"
            else:
                assert category.text.lower() == category_name.lower(), f"Expected category is {category_name}, but actual is {category.text}"

    @staticmethod
    def currency_to_int(price):
        return int(price.replace("$", "").replace(",", ""))
