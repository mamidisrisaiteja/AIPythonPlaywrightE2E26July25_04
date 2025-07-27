import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope='session')
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope='function')
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()
    browser.close()
