from appium import webdriver

desired_cap = {
    'platformName': 'Android',
    'platformVersion': '9',
    'deviceName': 'Android Emulator',
    'app': "C:\\Users\\User\\Documents\\code\\appium\\apk\\Clock_v6.1.1(238466778)_apkpure.com.apk"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

elemAlarm = driver.find_elements_by_accessibility_id('Alarm')
elemAlarm[0].click()
driver.implicitly_wait(1)

elemClock = driver.find_elements_by_accessibility_id('Clock')
elemClock[0].click()
driver.implicitly_wait(1)

elemTimer = driver.find_elements_by_accessibility_id('Timer')
elemTimer[0].click()
driver.implicitly_wait(1)

elemStopwatch = driver.find_elements_by_accessibility_id('Stopwatch')
elemStopwatch[0].click()
driver.implicitly_wait(1)
