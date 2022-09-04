from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
# import utility.custom_logger as cl
import logging

"""""
def elementfound(locator, locatortype):
    locatortype = locatortype.lower()

    print("Element found with locator: " + locator +" and  locatorType: " + locatortype)

def elementnotfound(self,locator,locatortype):

    locatortype = locatortype.lower()

    print("Element not found with locator: " + locator +
          " and  locatorType: " + locatortype)
"""


class SeleniumDriver():
    def __init__(self, driver):
        self.driver = driver

    def getbytype(self, locator_type):
        locator_type = locator_type.lower()

        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "logintext":
            return By.LINK_TEXT
        else:
            print("Locator type is not valid" + locator + "locator Type" + locator_type)
        return False

    def getElement(self, locator,locator_type="id"):
        element = None

        try:
            locatortype = locator_type.lower()
            bytype = self.getbytype(locator_type)
            element = self.driver.find_element(bytype, locator)
            print("Element found with : " + locator + " and  locatorType: " + locator_type)
        except:
            print("Element not found with locator: " + locator + " and  locatorType: " + locator_type)
        return element

    def get_elementclick(self, locator_type):
        try:
            element = self.getElement( locatorType,locator)
            element.click()
            print("Element found with locator: " + locator + " and  locatorType: " + locator_type)
        except:
            print("Element not found with locator: " + locator +
                  " and  locatorType: " + locator_type)
            print_stack()

    def sendkeys(self,data,locator,locator_type="id" ):
        try:
            element = self.getelement(locator, locator_type)
            element.send_keys(data)
            print("Element found with locator: " + locator + " and  locatorType: " + locator_type)
        except:
            print("Element not found with sendkeys: " + locator +
                  " and  locatorType: " + locator_type)
            print_stack()

    def is_elementpresent(self, locator, locator_type):
        try:
            element = self.driver.find_element(locator, locator_type)
            if element is not None:
                print("Element found with locator: " + locator + " and  locatorType: " + locator_type)
        except:
            print("Element not found with locator: " + locator +
                  " and  locatorType: " + locator_type)

    def element_presence_check(self, locator, locator_type):
        try:
            element = self.driver.find_element(locator, locator_type)
            if len(element) > 0:
                print("Element found with locator: " + locator + " and  locatorType: " + locator_type)
            else:
                print("Element not found with locator: " + locator +
                      " and  locatorType: " + locator_type)
        except:
            print("Element not found with locator: " + locator +
                  " and  locatorType: " + locator_type)

    def waitForElement(self, locator, locator_type="id",
                       timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getbytype(locator_type)
            print("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType,
                                                             "stopFilter_stops-0")))
            print("Element appeared on the web page")
        except:
            print("Element not appeared on the web page")
            print_stack()
        return element
    def logindetails(self):
        baseURL = "https://lendperfect.janabank.com/lendperfect/login"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
