from Locators.Locators import Locators
import time
class ProductDetailPage():

    # Constructor

    def __init__(self, driver):
        self.driver = driver

        self.addToList_Button_id = Locators.addToList_Button_id
        self.closeButton_xpath   = Locators.closeButton_xpath
        self.productTitle        = Locators.productTitle_id


    def click_add(self):
        time.sleep(2)
        self.driver.find_element_by_id(self.addToList_Button_id).click()

    def clickClose(self):
        time.sleep(1)
        self.driver.find_element_by_css_selector(self.closeButton_xpath).click()

    def idProduct(self,url):
        product_idlist = url.split("/")         ## amazon.com/2323/product_id/23232
        product_id = product_idlist[5]          ## get product_id from url.
        print(product_idlist[5])
        return product_id


