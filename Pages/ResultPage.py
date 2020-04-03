from Locators.Locators import Locators
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class ResultPage():


    # Constructor
    def __init__(self, driver):
        self.driver = driver

        self.resultPage2_xpath = Locators.resultPage2_xpath
        self.product_xpath     = Locators.product_xpath
        self.page2button_xpath = Locators.page2button_xpath

    def product3(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locators.product_xpath)))
        product3 = self.driver.find_element_by_xpath(self.product_xpath)
        product3.click()

    def clickPage2(self):
        page2 = self.driver.find_element_by_xpath(self.page2button_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", page2)     ## Scroll down to Page 2 Button.
        page2.click()