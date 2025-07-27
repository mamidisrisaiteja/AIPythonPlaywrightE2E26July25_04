import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage

scenarios('../features/auth.feature')

@pytest.fixture
def login_page(browser):
    return LoginPage(browser)

@given(parsers.parse('user is on https://www.saucedemo.com/'))
def user_on_login_page(login_page):
    login_page.page.goto('https://www.saucedemo.com/')

@when(parsers.parse('user enters user name as "{username}" and password as "{password}"'))
def user_enters_credentials(login_page, username, password):
    login_page.login(username, password)


@then(parsers.parse('verify page has text "{text}"'))
def verify_page_text(login_page, text):
    assert login_page.page.locator(f'text={text}').is_visible()

@then('Redirect to Products page')
def redirect_to_products(login_page):
    assert login_page.page.url.endswith('/inventory.html')

@then('Login Button should be still displayed')
def login_button_displayed(login_page):
    assert login_page.login_button.is_visible()
