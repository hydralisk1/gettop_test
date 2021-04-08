from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.shop_page import ShopPage
from pages.account_page import AccountPage
from pages.category_page import CategoryPage


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.shop_page = ShopPage(self.driver)
        self.account_page = AccountPage(self.driver)
        self.category_page = CategoryPage(self.driver)
