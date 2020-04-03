from selenium.webdriver import ActionChains

from Locators.Locators import Locators
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Homepage():

    # Constructor
    def __init__(self,driver):
        self.driver = driver

        self.accLoginButton_id      = Locators.accLoginButton_id
        self.searchBar_id           = Locators.searchBar_id
        self.searchButton_xpath     = Locators.searchButton_xpath
        self.listButton_xpath       = Locators.listButton_xpath
        self.wishList_xpath         = Locators.wishList_xpath


    def clickSignIn(self):
        self.driver.find_element_by_id(self.accLoginButton_id).click()

    def searchProduct(self,searchText):
        self.driver.find_element_by_id(self.searchBar_id).clear()
        self.driver.find_element_by_id(self.searchBar_id).send_keys(searchText)
        self.driver.find_element_by_xpath(self.searchButton_xpath).click()

    def hoverList(self):
        time.sleep(2)
        WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.listButton_xpath)))
        hover_element = self.driver.find_element_by_xpath(self.listButton_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", hover_element)
        hover = ActionChains(self.driver).move_to_element(hover_element)
        hover.perform()

    def clickWishlist(self):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.wishList_xpath)))
        self.driver.find_element_by_xpath(self.wishList_xpath).click()
