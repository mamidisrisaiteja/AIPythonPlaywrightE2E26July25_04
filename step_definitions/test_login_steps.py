import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage

scenarios('../features/login.feature')

@pytest.fixture
def login_page(browser):
    return LoginPage(browser)

@given('the user is on the login page')
def user_on_login_page(login_page):
    login_page.page.goto('https://www.saucedemo.com/')

@when(parsers.parse('the user logs in with valid credentials'))
def user_logs_in(login_page):
    # Replace with Excel MCP integration for credentials
    login_page.login('standard_user', 'secret_sauce')

@then('the user should see the dashboard')
def user_sees_dashboard(login_page):
    login_page.page.wait_for_selector('text=Products', timeout=15000)
    assert login_page.page.locator('text=Products').is_visible()
