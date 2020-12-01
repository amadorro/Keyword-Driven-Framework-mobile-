'''Fixtures are functions, which will run before each test
function to which it is applied. Fixtures are used to feed
some data to the tests such as database connections,
URLs to test and some sort of input data. '''

from appium import webdriver
import pytest

@pytest.fixture()
def setup():
    desired_cap = {
        "platformName": "Android",
        "deviceName": "Android Emulator",
        "appPackage": "com.flipkart.android",
        "appWaitActivity": "com.flipkart.android.activity.FirstLaunchActivity",
        "app": "C:\\Users\\Amador\\com.flipkart.android_7.12.apk"
    }
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
    return driver