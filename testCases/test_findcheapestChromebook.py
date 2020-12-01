# goal: verify if the item's price is the same when is selected

from pageObjects.FindCheapestChromebook import Chromebook
from pageObjects.SearchIphonePage import SearchIphone
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
import time

class Test_03_Chrbook:
    logger = LogGen.loggen()

    def test_findChromebook(self, setup):
        self.logger.info("**** Test_03_Chrbook Testing Started ****")
        self.driver = setup
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
        self.si.iphoneSearchBox('Chromebook')

        # click on item
        self.cb = Chromebook(self.driver)
        time.sleep(5)
        self.cb.clickChrmFirstChoice()
        time.sleep(10)
        # click on popup
        self.si.clickAlert()

        time.sleep(10)
        act_price1 = self.cb.setFindChromebook()
        self.cb.clickFirstChrbook()

        # validate item's price when selected
        time.sleep(9)
        act_price2 = self.cb.setPrice_chrombook1()
        if act_price1 == act_price2:
            self.logger.info("***** Price matched *****")
            assert True

        else:
            self.driver.save_screenshot("./Screenshots/" + "Test_03_Chrbook.png")
            self.logger.error("***** Price do not matched *****")
            assert False

        self.logger.info("**** Test_03_Chrbook Testing Completed ****")




