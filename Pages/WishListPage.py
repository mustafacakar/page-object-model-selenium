
from Locators.Locators import Locators
import time
from Pages.ProductDetailPage import ProductDetailPage

class Wishlist():

    # Constructor
    def __init__(self, driver):
        self.driver = driver

        self.privateWishlist_xpath         = Locators.privateWishList_xpath
        self.productOptionsButton_xpath    = Locators.productOptionsButton_xpath
        self.deleteButton_xpath            = Locators.deleteButton_xpath
        self.shoppingList            = Locators.shopping_list

    def clickPrivate(self):
        time.sleep(2)
        # self.driver.find_element_by_xpath(self.privateWishlist_xpath).click()
        self.driver.find_element_by_xpath(self.privateWishlist_xpath).click()

    def clickOption(self):
        time.sleep(1)
        self.driver.find_element_by_xpath(self.productOptionsButton_xpath).click()

    def deleteProduct(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.deleteButton_xpath).click()
