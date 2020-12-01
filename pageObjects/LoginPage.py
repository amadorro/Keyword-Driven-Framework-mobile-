# note: turn on the server: adb start-server on cmd

class LoginPage:
    # locator variables
    select_language_id = "com.flipkart.android:id/locale_icon_layout"
    select_continue_id = "com.flipkart.android:id/select_btn"
    select_X_id = "com.flipkart.android:id/custom_back_icon"


    def __init__(self, driver):
        self.driver = driver

    def clickButtonLanguage(self):
        self.driver.find_element_by_id(self.select_language_id).click()

    def clickButtonContinue(self):
        self.driver.find_element_by_id(self.select_continue_id).click()

    def clickX(self):
        self.driver.find_element_by_id(self.select_X_id).click()


