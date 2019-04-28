from appium import webdriver
import unittest


class ClockTest(unittest.TestCase):

    def setUp(self):
        """ set up app on virtual device """
        desired_cap = {
            'platformName': 'Android',
            'platformVersion': '9',
            'deviceName': 'Android Emulator',
            'app': "C:\\Users\\User\\Documents\\code\\appium\\apk\\Clock_v6.1.1(238466778)_apkpure.com.apk"
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

    def test_clock_alarm(self):
        """ test alarm page """
        self.driver.find_element_by_accessibility_id('Alarm').click()
        self.driver.find_element_by_accessibility_id('Add alarm').click()
        self.driver.find_element_by_accessibility_id('4').click()
        self.driver.find_element_by_accessibility_id('30').click()
        self.driver.find_element_by_id("android:id/pm_label").click()
        self.driver.find_element_by_id('android:id/button1').click()

        # Check that Alarm was added
        self.assertTrue(self.driver.find_element_by_accessibility_id('4:30 PM'))
        self.driver.implicitly_wait()
        # remove Alarm
        self.driver.find_element_by_id('com.google.android.deskclock:id/delete').click()

    def test_clock_main(self):
        """ test main click page """
        self.driver.find_element_by_accessibility_id('Clock').click()
        self.assertTrue(self.driver.find_element_by_id('com.google.android.deskclock:id/digital_clock'))
        self.assertTrue(self.driver.find_element_by_id('com.google.android.deskclock:id/date'))

    def test_clock_timer(self):
        """ test click timer page """
        self.driver.find_element_by_accessibility_id('Timer').click()
        self.assertEqual(self.driver.find_element_by_id('com.google.android.deskclock:id/timer_setup_time').text,
                         "00h 00m 00s")
        self.driver.find_element_by_id("com.google.android.deskclock:id/timer_setup_digit_1").click()
        self.assertEqual(self.driver.find_element_by_id("com.google.android.deskclock:id/timer_setup_time").text,
                         "00h 00m 01s")
        self.driver.find_element_by_id("com.google.android.deskclock:id/timer_setup_delete").click()
        self.assertEqual(self.driver.find_element_by_id("com.google.android.deskclock:id/timer_setup_time").text,
                         "00h 00m 00s")

    def test_clock_stopwatch(self):
        """ test stopwatch """
        self.driver.find_element_by_accessibility_id('Stopwatch').click()
        self.assertEqual(self.driver.find_element_by_id('com.google.android.deskclock:id/stopwatch_time_text').text,
                         "0")
        self.assertEqual(
            self.driver.find_element_by_id('com.google.android.deskclock:id/stopwatch_hundredths_text').text,
            "00")
        self.driver.implicitly_wait(1)

        self.driver.find_element_by_id("com.google.android.deskclock:id/fab").click()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_id("com.google.android.deskclock:id/fab").click()
        assert int(self.driver.find_element_by_id("com.google.android.deskclock:id/stopwatch_time_text").text) > 1


if __name__ == "__main__":
    unittest.main()
