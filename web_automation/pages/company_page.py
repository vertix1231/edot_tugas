from selenium.webdriver.common.by import By
from utilities.base_page import BasePage
import time
from faker import Faker

class CompanyPage(BasePage):
    # Element Locators
    TAB_COMPANY = (By.XPATH, '/html/body/div/header/div/nav/div/div/a[2]')
    CREATE_BUTTON = (By.XPATH, "//button[contains(text(),'Create')]")
    COMPANY_NAME_INPUT = (By.ID, "company-name")
    SAVE_BUTTON = (By.ID, "save-company")
    
    def create_company(self):
        self.click(self.TAB_COMPANY)
        time.sleep(10)
        # fake = Faker()
        # self.click(self.CREATE_BUTTON)
        # company_name = fake.company()
        # self.input_text(self.COMPANY_NAME_INPUT, company_name)
        # self.click(self.SAVE_BUTTON)
        # return company_name