
from Locators.Locators import Locators

class LoginPage():

    # Constructor
    def __init__(self,driver):
        self.driver = driver

        self.emailTextbox_id     = Locators.emailTextbox_id
        self.continueButton_id   = Locators.continueButton_id
        self.passwordTextbox_id  = Locators.passwordTextbox_id
        self.signInButton_id     = Locators.signInButton_id

    def enterEmail(self,email):
        self.driver.find_element_by_id(self.emailTextbox_id).clear()
        self.driver.find_element_by_id(self.emailTextbox_id).send_keys(email)


    def clickContinue(self):
        self.driver.find_element_by_id(self.continueButton_id).click()

    def enterPassword(self,password):
        self.driver.find_element_by_id(self.passwordTextbox_id).clear()
        self.driver.find_element_by_id(self.passwordTextbox_id).send_keys(password)

    def clickSignIn(self):
        self.driver.find_element_by_id(self.signInButton_id).click()