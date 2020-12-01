import pytest
from appium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
import time

class Test_001_Login:

    logger = LogGen.loggen()
    def test_LoginPage(self, setup):
        self.logger.info("**** Test_001_Login Started ****")
        self.driver = setup
        # from constructor
        self.lp = LoginPage(self.driver)
        time.sleep(12)
        self.lp.clickButtonLanguage()
        time.sleep(12)
        self.lp.clickButtonContinue()
        time.sleep(12)
        self.lp.clickX()
        self.logger.info("**** Test_001_Login Completed ****")