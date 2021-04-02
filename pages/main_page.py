from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import requests


class MainPage(Page):
    CATEGORIES = (By.CSS_SELECTOR, "span.widget-title")
    PRODUCTS = (By.CSS_SELECTOR, "ul.product_list_widget > li")
    PRODUCT_NAME = (By.CSS_SELECTOR, "span.product-title")
    PRICE = (By.CSS_SELECTOR, "span.woocommerce-Price-amount")
    PRICE_INS = (By.CSS_SELECTOR, "ins > span.woocommerce-Price-amount")
    STAR_RATING = (By.CSS_SELECTOR, "div.star-rating")
    COPYRIGHT = (By.CSS_SELECTOR, "div.copyright-footer")
    LINK_TO_TOP = (By.CSS_SELECTOR, "a[href='#top']")
    CATEGORY_LINKS = (By.CSS_SELECTOR, "ul#menu-main-1 a")

    def open_main_page(self):
        self.open_page("https://gettop.us")

    def verify_categories(self, *categories):
        categories_in_footer = [category.text.lower() for category in self.find_elements(*self.CATEGORIES)]

        for category in categories:
            assert category.lower() in categories_in_footer, f"There's no {category} in the footer"

    def verify_products(self):
        products = self.find_elements(*self.PRODUCTS)

        for i in range(len(products)):
            # Check product name
            product_name = products[i].find_elements(*self.PRODUCT_NAME)
            assert product_name, f"{i}th product doesn't have a product name"

            # Check price
            price = products[i].find_elements(*self.PRICE_INS)
            if not price:
                price = products[i].find_elements(*self.PRICE)
            assert price, f"{product_name[0].text} doesn't have a price"

            # Check star rating
            star_rating = products[i].find_elements(*self.STAR_RATING)
            assert star_rating, f"{product_name[0].text} doesn't have a star rating"

    def verify_string(self, text):
        try:
            copyright_string = self.find_element(*self.COPYRIGHT).text
            # This test will fail because the string in the footer is "Copyright 2021"
            # If input string is "Copyright 2021", this test will pass
            assert text in copyright_string, f"{text} isn't shown in the footer"
        except NoSuchElementException:
            assert False, "You should check the footer element"

    def verify_button_to_top(self):
        button_to_top = self.find_elements(*self.LINK_TO_TOP)
        assert button_to_top, "There's no button to go back to the top"

    def verify_all_links_working(self):
        links = self.find_elements(*self.CATEGORY_LINKS)
        for link in links:
            r = requests.head(link.get_attribute("href"))
            assert r.status_code, f"Link to {link.text} category doesn't work"