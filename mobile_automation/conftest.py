# conftest.py
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from utilities.config import APPIUM_HOST, APPIUM_PORT, APP_PATH, APP_PACKAGE, APP_ACTIVITY

@pytest.fixture(scope="function")
def mobile_driver():
    # Buat objek Options
    options = UiAutomator2Options()
    
    # Set capabilities menggunakan atribut objek
    options.platform_name = "Android"
    options.device_name = "537848b2"
    options.automation_name = "UiAutomator2"
    options.app = APP_PATH
    options.app_package = APP_PACKAGE
    options.app_activity = APP_ACTIVITY
    
    # Jika perlu tambahan capabilities
    # options.auto_grant_permissions = True
    # options.no_reset = False
    
    driver = webdriver.Remote(
        command_executor=f"http://{APPIUM_HOST}:{APPIUM_PORT}",
        options=options
    )
    yield driver
    driver.quit()
# import pytest
# from appium import webdriver
# from utilities.config import APPIUM_HOST, APPIUM_PORT, APP_PATH, APP_PACKAGE, APP_ACTIVITY

# @pytest.fixture(scope="function")
# def mobile_driver():
#     capabilities = {
#         "platformName": "Android",
#         "appium:deviceName": "537848b2",
#         "appium:automationName": "UiAutomator2",
#         "appium:app": APP_PATH,
#         "appium:appPackage": APP_PACKAGE,
#         "appium:appActivity": APP_ACTIVITY,
#     }
    
#     driver = webdriver.Remote(f"http://{APPIUM_HOST}:{APPIUM_PORT}/wd/hub",capabilities)
#     yield driver
#     driver.quit()