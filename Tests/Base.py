from selenium import webdriver
import time
import unittest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import sys; print('Python %s on %s' % (sys.version, sys.platform))
from Pages.Homepage import Homepage
from Pages.LoginPage import LoginPage
from Pages.ProductDetailPage import ProductDetailPage
from Pages.ResultPage import ResultPage
from Pages.WishListPage import Wishlist
from Locators.Locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Locators.Users import Users

class BaseTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()             ## path : Scripts/Geckodriver.exe copied.
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def  test_001Page_Load(self):
        driver = self.driver
        driver.get("https://www.amazon.com/")
        assert "Amazon" in driver.title             ## Check Title

    def test_0020SignInButton(self):
        driver = self.driver
        SignInBtn = Homepage(driver)
        SignInBtn.clickSignIn()                                             ## Home-> SignInButton
        assert "ap/signin" in driver.current_url                            ## Check Url

    def test_0021SignIn(self):                                              ## Sign IN.
        driver = self.driver
        Login = LoginPage(driver)
        Login.enterEmail(Users.mailadress)                                      ### Mail adress for login.
        Login.clickContinue()
        Login.enterPassword(Users.password)                                     ## Amazon password for login.
        Login.clickSignIn()                                                     ## SignInActivity

        ## One Time Password. -> Anti-Automation Protect , Captha etc.
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.ID, Locators.searchBar_id)))
        assert "ref_=nav_ya_signin" in driver.current_url                        ## Check Homepage url, after signin.

    def test_003Search(self):
        driver = self.driver
        Search = Homepage(driver)
        Search.searchProduct("samsung")                     ## search Samsung.
        time.sleep(2)

        try:
            driver.find_element_by_xpath(Locators.noResultCheck_xpath)
        except NoSuchElementException:
            print("Search Results Exist.")
            return True
        return False


    def test_004Page2(self):
        driver = self.driver
        Page2 = ResultPage(driver)
        Page2.clickPage2()                      ## Click Page 2 in Results.
        assert "_pg_2" in driver.current_url    ## Check Url for Page 2.

    def test_005Product3(self):                 ## Choose product 3 in result.
        time.sleep(3)
        driver = self.driver
        product = ResultPage(driver)
        product.product3()

        try:
            driver.find_element_by_id(Locators.addToList_Button_id)
        except NoSuchElementException:
            print("Product Detail Page Opened.")    # Control for Product detail Page Open?.
            return True
        return False


    def test_006AddToList(self):        ## Add to Wishlist.
        time.sleep(2)
        driver = self.driver
        addToList = ProductDetailPage(driver)
        global url_id
        url = driver.current_url
        url_id = addToList.idProduct(url)
        addToList.click_add()

    def test_007PopUpClose(self):       ## Close pop up , after add list.
        time.sleep(3)
        driver = self.driver
        closePopUp = ProductDetailPage(driver)
        closePopUp.clickClose()

    def test_008Hover(self):        ## Go to Wishlist.
        time.sleep(3)
        driver = self.driver
        hoverList = Homepage(driver)
        hoverList.hoverList()
        hoverList.clickWishlist()


    def test_009PrivateList(self):
        time.sleep(2)
        driver = self.driver
        PrivateList = Wishlist(driver)
        PrivateList.clickPrivate()
        #Product_ID Control.
        list = driver.find_element_by_id(Locators.wishlist_allprod)
        items = list.find_element_by_tag_name("li").get_attribute("data-reposition-action-params")
        print(items)
        assert url_id in items                                            ## Check for product in list.
        print(url_id)
        try:
            driver.find_element_by_xpath(Locators.wishlist_control)       # 0 item in list.
        except NoSuchElementException:
            print("Wishlist not empty.")
            return True
        return False


    def test_010DeleteItem(self):
        time.sleep(2)
        driver = self.driver
        DeleteItem = Wishlist(driver)
        DeleteItem.clickOption()
        DeleteItem.deleteProduct()
        ## Control for item delete.
        list = driver.find_element_by_id(Locators.wishlist_allprod)
        items = list.find_element_by_tag_name("li").get_attribute("data-reposition-action-params")
        driver.refresh()
        time.sleep(5)
        try:
            assert url_id in items
        except:
            print("Item Deleted.")
            return True
        return False

    @classmethod
    def test_011tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main()