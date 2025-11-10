import pytest
from selene import browser
from selenium.webdriver import ChromeOptions


@pytest.fixture(scope="session", autouse=True)
def configure_browser():
    options = ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    browser.config.driver_options = options
    browser.config.timeout = 6.0

    yield
    browser.quit()
