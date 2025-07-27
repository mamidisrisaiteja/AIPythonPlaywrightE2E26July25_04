import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture(scope='session')
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope='function')
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=True)  # Changed to headless for CI
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()
    browser.close()

@pytest.fixture
def login_page(browser):
    return LoginPage(browser)

@pytest.fixture
def inventory_page(browser):
    return InventoryPage(browser)
