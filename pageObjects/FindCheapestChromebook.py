
class Chromebook:
    # locators
    click_chrombook_First_choice_id = "com.flipkart.android:id/root_titles"
    price_chrombook1_xpath = "//android.widget.TextView[@text = '₹20,990']"
    click_chromebook_xpath = "//android.widget.TextView[@bounds= '[311,504][468,561]']"
    price_chrombook2_xpath = "//android.widget.TextView[@text= '₹20,990']"


    def __init__(self, driver):
        self.driver = driver

    def clickChrmFirstChoice(self):
        self.driver.find_element_by_id(self.click_chrombook_First_choice_id).click()

    def setFindChromebook(self):
        self.driver.find_element_by_xpath(self.price_chrombook1_xpath).get_attribute('text')


    def clickFirstChrbook(self):
        self.driver.find_element_by_xpath(self.click_chromebook_xpath).click()

    def setPrice_chrombook1(self):
        self.driver.find_element_by_xpath(self.price_chrombook2_xpath).get_attribute('text')






