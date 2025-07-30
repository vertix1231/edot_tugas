from appium import webdriver
from appium.options.android import UiAutomator2Options
from utilities.config import APPIUM_HOST, APPIUM_PORT, APP_PATH, APP_PACKAGE, APP_ACTIVITY

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

print("App launched successfully!")
print("Current package:", driver.current_package)
print("Current activity:", driver.current_activity)
driver.quit()