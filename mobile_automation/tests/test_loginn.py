# tests/test_login.py
from appium import webdriver
from appium.options.android import UiAutomator2Options
from utilities.config import APPIUM_HOST, APPIUM_PORT, APP_PATH, APP_PACKAGE, APP_ACTIVITY

def test_valid_login():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "537848b2"
    options.automation_name = "UiAutomator2"
    options.app = APP_PATH
    options.app_package = APP_PACKAGE
    options.app_activity = APP_ACTIVITY
    
    driver = webdriver.Remote(
        command_executor=f"http://{APPIUM_HOST}:{APPIUM_PORT}",
        options=options
    )
    
    try:
        print("Aplikasi berhasil dibuka!")
        print("Package:", driver.current_package)
        assert driver.current_package == APP_PACKAGE
    finally:
        driver.quit()