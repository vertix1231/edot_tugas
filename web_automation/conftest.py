import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def browser():
    service = Service(ChromeDriverManager().install())
    driver = Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()