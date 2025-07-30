from selenium.webdriver.common.by import By
from utilities.base_page import BasePage
import time

class LoginPage(BasePage):
    # Element Locators
    LOGIN_METODE_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/button[1]')
    SHADOW_HOST = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/div/div[2]/div/input')
    EMAIL_INPUT = (By.XPATH, '//input[@name="username"]')
    LOGIN_BUTTON_ONE = (By.XPATH, "//div[@id='root']/div/div[2]/div/div[3]/div/button")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON_TWO = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/div/button')
    
    
    def login(self,email,password):
        
        self.click(self.LOGIN_METODE_BUTTON)
        time.sleep(10)
        self.input_text(self.EMAIL_INPUT,email)
        time.sleep(10)
        self.click(self.LOGIN_BUTTON_ONE)
        time.sleep(10)
        self.input_text(self.PASSWORD_INPUT,password)
        time.sleep(10)
        self.click(self.LOGIN_BUTTON_TWO)
        time.sleep(10)
        
        # email_field = self.wait_for_shadow_element(
        #     self.SHADOW_HOST,
        #     self.EMAIL_INPUT
        # )
        # email_field.send_keys(email)
        
        # self.input_text(self.EMAIL_INPUT, email)
        # self.input_text(self.PASSWORD_INPUT, password)
        # self.click(self.LOGIN_BUTTON)
    
    # def test_shadow_dom_element(self,driver):

    #     # 1. Locate the HOST element of the Shadow DOM
    #     host_element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/div/div[2]/div/input')

    #     # 2. Use JavaScript to access the Shadow Root
    #     shadow_root = driver.execute_script("return arguments[0].shadowRoot", host_element)

    #     # 3. Find elements INSIDE the Shadow Root using XPath
    #     inner_element = shadow_root.find_element(self.EMAIL_INPUT)

    #     # Interact with the element
    #     inner_element.click()