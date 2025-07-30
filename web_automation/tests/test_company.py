import pytest
from pages.login_page import LoginPage
from pages.company_page import CompanyPage
import time
from utilities.config import BASE_URL, CREDENTIALS

@pytest.mark.usefixtures("browser")
class TestCompanyCreation:
    def test_create_and_verify_company(self, browser):
        # # Login
        # browser.get(BASE_URL)
        # login_page = LoginPage(browser)
        # login_page.login(CREDENTIALS["email"], CREDENTIALS["password"])
        browser.get(BASE_URL)
        login_page = LoginPage(browser)
        login_page.login(CREDENTIALS["email"],CREDENTIALS["password"])
        # Tambahkan delay untuk memastikan halaman loading
        time.sleep(3)
        
        # Create Company
        company_page = CompanyPage(browser)
        company_page.create_company()
        time.sleep(3)
        
        # Verification
        # assert company_name in browser.page_source