import pytest
from appium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchIphonePage import SearchIphone
from utilities.customLogger import LogGen
import time


class Test_002_SearchIphone5:
    logger = LogGen.loggen()

    def test_searchIphone(self, setup):
        self.logger.info("***** Test Test_002_SearchIphone11 Start *****")
        self.driver = setup
        time.sleep(9)
        self.logger.info("***** Login Begins *****")

        # Create a variable to access LoginPage.py
        self.lp = LoginPage(self.driver)
        time.sleep(9)
        self.lp.clickButtonLanguage()
        time.sleep(9)
        self.lp.clickButtonContinue()
        time.sleep(9)
        self.lp.clickX()
        time.sleep(9)

        # create variable to access SearchIphonePage.py
        self.logger.info("***** Iphone Search begins *****")
        self.si = SearchIphone(self.driver)
        time.sleep(13)
        self.si.iphoneSearchBox('iphone 11')
        time.sleep(13)
        self.logger.info("***** Search Iphone *****")
        self.si.clickIcon()
        time.sleep(13)
        self.si.clickAlert()
        time.sleep(13)
        self.logger.info("***** Click Alert Message *****")
        self.logger.info("***** Ending Search Iphone 11 *****")
        self.logger.info("***** Test Test_002_SearchIphone11 Completed *****")



