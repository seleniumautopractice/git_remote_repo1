from selenium import webdriver
# from selenium.webdriver.common.by import By
# import logging

# from selenium.webdriver.support import wait
#from webdriver_manager.core import driver

# from base.selenium_driver.Seleniumdriver import SeleniumDriver
from page.home_page.login_page import LoginPage
import unittest
import pytest


class LoginTests(unittest.TestCase):
    base_url = "https://courses.letskodeit.com/login"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(base_url)

    lp = LoginPage(driver)
    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.driver.get(self.base_url)
        self.lp.login("santhoshgnupdates@gmail.com", "Letskodeit#10l")
        result = self.lp.verify_login()
        assert result == True
        self.driver.implicitly_wait(3)
        self.driver.quit()


    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.driver.get(self.base_url)
        self.lp.login("santhosh.gn.cog", "rttyy#2j")
        result = self.lp.invalid_login()
        assert result==True

