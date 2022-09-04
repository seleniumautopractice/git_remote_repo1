
from selenium.webdriver.common.by import By

#from base.selenium_driver.Seleniumdriver import SeleniumDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage():

    def __init__(self, driver):
        #super().__init__(driver)
        self.driver = driver
    # Locators
    # _login_link = "Login"
    _email_field = "email"
    _password_field = "password"
    _login_button = "//div[4]/div[1]/input"

    #def getLoginLink(self):
     #   return self.driver.find_element(By.LINK_TEXT, self._login_link)

    def getEmailField(self):
        return self.driver.find_element(By.ID, self._email_field)

    def getPasswordField(self):
        return self.driver.find_element(By.ID, self._password_field)

    def getLoginButton(self):
        return self.driver.find_element(By.XPATH, self._login_button)

    #def clickLoginLink(self):
      #  self.getLoginLink().click()

    def enterEmail(self, email):
        self.getEmailField().send_keys(email)

    def enterPassword(self, password):
        self.getPasswordField().send_keys(password)

    def clickLoginButton(self):
        self.getLoginButton().click()

    def verify_login(self):
        homeicon = self.driver.find_element(By.ID,"//div/div[1]/a/img")

        if homeicon is not None:
            print("Element is visible and Login Successful")
            #self.driver.save_screenshots()
        else:
            print("Login Failed")

    def invalid_login(self):
        homepageicon1 = self.driver.find_element(By.XPATH,"//div/form/div[1]/span")

        print("Login Failed")
    """""
    def clearFields(self):
        emailField = self.getEmailField()
        emailField.clear()
        passwordField = self.enterPassword()
        passwordField.clear()
    """


    def login(self, email, password):
        #self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        self.driver.implicitly_wait(3)
        self.driver.quit()

    """""
    def enter_email(self ,email):
        self.sendkeys(email ,self._email_field)

    def enterpassword(self, password):
        self.sendkeys(password, self._password_field)
    def clickLoginButton(self,locator,locator_type="id"):
        self.get_elementclick()

    def login(self,email, password):
        self.enter_email(email)
        self.enterpassword(password)
        self.clickLoginButton()
        
        
        
        --------------------------
        
        def verifyLoginSuccessful(self):
        result = self.isElementPresent("//*[@id='navbar']//span[text()='User Settings']",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[contains(text(),'Invalid email or password')]",
                                       locatorType="xpath")
        return result
    """

