from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
    
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
    
    def input_text(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)
    
    def get_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    def __init__(self, driver: WebDriver):  # Tambah type hinting
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        
     # Fungsi untuk mengakses shadow root dan elemen di dalamnya
    def get_shadow_element(self, shadow_host_selector, inner_selector):
        """
        shadow_host_selector: CSS selector untuk shadow host
        inner_selector: CSS selector untuk elemen di dalam shadow DOM
        """
        # Script JavaScript untuk mengakses shadow element
        js_script = """
            return document.querySelector(arguments[0])
                .shadowRoot.querySelector(arguments[1])
        """
        return self.driver.execute_script(js_script, shadow_host_selector, inner_selector)
    
    # Fungsi untuk menunggu shadow element muncul
    def wait_for_shadow_element(self, shadow_host_selector, inner_selector, timeout=15):
        def _predicate(_):
            element = self.get_shadow_element(shadow_host_selector, inner_selector)
            return element if element else False
        return WebDriverWait(self.driver, timeout).until(_predicate)