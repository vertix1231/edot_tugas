from appium.webdriver.common.appiumby import AppiumBy
from utilities.base_page import BasePage

class LoginPage(BasePage):
    COMPANY_ID_INPUT = (AppiumBy.ID, "com.edot.ework:id/etCompanyId")
    EMAIL_INPUT = (AppiumBy.ID, "com.edot.ework:id/etEmail")
    PASSWORD_INPUT = (AppiumBy.ID, "com.edot.ework:id/etPassword")
    LOGIN_BUTTON = (AppiumBy.ID, "com.edot.ework:id/btnLogin")
    DASHBOARD = (AppiumBy.ID, "com.edot.ework:id/dashboard_layout")
    
    def login(self, company_id, email, password):
        self.input_text(self.COMPANY_ID_INPUT, company_id)
        self.input_text(self.EMAIL_INPUT, email)
        self.input_text(self.PASSWORD_INPUT, password)
        self.tap(self.LOGIN_BUTTON)
    
    def is_dashboard_displayed(self):
        return self.driver.find_element(*self.DASHBOARD).is_displayed()