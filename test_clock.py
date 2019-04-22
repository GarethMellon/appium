from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import unittest


class ClockTest(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            'platformName': 'Android',
            'platformVersion': '9',
            'deviceName': 'Android Emulator',
            'app': "C:\\Users\\User\\Documents\\code\\appium\\apk\\Clock_v6.1.1(238466778)_apkpure.com.apk"
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

    def test_clock_alarm(self):
        self.driver.find_element_by_accessibility_id('Alarm').click()
        self.driver.find_element_by_accessibility_id('Add alarm').click()
        self.driver.find_element_by_accessibility_id('4').click()
        self.driver.find_element_by_accessibility_id('30').click()
        self.driver.find_element_by_id('android:id/button1').click()

        # Check that Alarm was added
        self.assertTrue(self.driver.find_element_by_accessibility_id('4:30 PM'))

        self.driver.implicitly_wait(2)

        self.driver.find_element_by_id('com.google.android.deskclock:id/delete').click()
        # self.assertEqual(self.driver.find_element_by_id('com.google.android.deskclock:id/snackbar_text').text, "Alarm deleted")
        self.driver.implicitly_wait(2)

    def test_clock_main(self):
        self.driver.find_element_by_accessibility_id('Clock').click()

        self.driver.implicitly_wait(2)

    def test_clock_timer(self):
        self.driver.find_element_by_accessibility_id('Timer').click()
        self.assertEqual(self.driver.find_element_by_id('com.google.android.deskclock:id/timer_setup_time').text,
                         "00h 00m 00s")
        self.driver.implicitly_wait(2)

    def test_clock_stopwatch(self):
        self.driver.find_element_by_accessibility_id('Stopwatch').click()
        self.assertEqual(self.driver.find_element_by_id('com.google.android.deskclock:id/stopwatch_time_text').text, "0")
        self.assertEqual(self.driver.find_element_by_id('com.google.android.deskclock:id/stopwatch_hundredths_text').text,
                         "00")
        self.driver.implicitly_wait(2)


if __name__ == "__main__":
    unittest.main()
