from pages.main_page import MainPage
from pages.product_page import ProductPage


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.product_page = ProductPage(self.driver)
