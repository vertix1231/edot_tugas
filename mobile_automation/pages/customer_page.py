from appium.webdriver.common.appiumby import AppiumBy
from utilities.base_page import BasePage
from faker import Faker

class CustomerPage(BasePage):
    CUSTOMER_MENU = (AppiumBy.XPATH, "//android.widget.TextView[@text='Customers']")
    CREATE_BUTTON = (AppiumBy.ID, "com.edot.ework:id/fabAdd")
    NAME_INPUT = (AppiumBy.ID, "com.edot.ework:id/etCustomerName")
    SAVE_BUTTON = (AppiumBy.ID, "com.edot.ework:id/btnSave")
    SUCCESS_MESSAGE = (AppiumBy.ID, "com.edot.ework:id/tvSuccessMessage")
    
    def navigate_to_customers(self):
        self.tap(self.CUSTOMER_MENU)
    
    def create_customer(self):
        self.tap(self.CREATE_BUTTON)
        customer_name = Faker().name()
        self.input_text(self.NAME_INPUT, customer_name)
        self.tap(self.SAVE_BUTTON)
        return customer_name
    
    def is_success_displayed(self):
        return self.driver.find_element(*self.SUCCESS_MESSAGE).is_displayed()