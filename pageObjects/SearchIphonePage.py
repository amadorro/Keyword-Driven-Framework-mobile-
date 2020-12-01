import pytest
from appium import webdriver
from pageObjects.LoginPage import LoginPage
from selenium.webdriver.common.keys import Keys
import time
# note id = class + :id/ content-desc

class SearchIphone:
    # class variables
    txtSearchBox_id = "com.flipkart.android:id/search_widget_textbox"
    acSearch_id = "com.flipkart.android:id/search_autoCompleteTextView"
    selectIcon_xpath = "(//android.widget.ImageView[@content-desc='Product Image'])[1]"
    alertMessage_id = "com.flipkart.android:id/not_now_button"

    def __init__(self, driver):
        self.driver = driver

    def iphoneSearchBox(self, iphone):
        self.driver.find_element_by_id(self.txtSearchBox_id).click()
        time.sleep(8)
        self.driver.find_element_by_id(self.acSearch_id).send_keys(iphone)

    def clickIcon(self):
        self.driver.find_element_by_xpath(self.selectIcon_xpath).click()

    def clickAlert(self):
        self.driver.find_element_by_id(self.alertMessage_id).click()

