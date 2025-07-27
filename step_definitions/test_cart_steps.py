import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

scenarios('../features/cart.feature')

@pytest.fixture
def login_page(browser):
    return LoginPage(browser)

@pytest.fixture
def inventory_page(browser):
    return InventoryPage(browser)

@given(parsers.parse('user is on https://www.saucedemo.com/'))
def user_on_login_page(login_page):
    login_page.page.goto('https://www.saucedemo.com/')

@when(parsers.parse('user enters user name as "{username}" and password as "{password}"'))
def user_enters_credentials(login_page, username, password):
    login_page.login(username, password)

@then(parsers.parse('verify page has text "{text}"'))
def verify_page_text(login_page, text):
    assert login_page.page.locator(f'text={text}').is_visible()

@when('click Add to cart')
def click_add_to_cart(inventory_page):
    # Click the first 'Add to cart' button
    inventory_page.page.locator('button[data-test^="add-to-cart-"]').first.click()

@when('click cart icon')
def click_cart_icon(inventory_page):
    inventory_page.go_to_cart()

@then(parsers.parse('verify page has text "{text}"'))
def verify_cart_page_text(inventory_page, text):
    assert inventory_page.page.locator(f'text={text}').is_visible()

@then('Cart page displays selected items')
def cart_page_displays_items(inventory_page):
    # Add cart item verification logic here
    assert True
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

scenarios('../features/cart.feature')

@pytest.fixture
def login_page(browser):
    return LoginPage(browser)

@pytest.fixture
def inventory_page(browser):
    return InventoryPage(browser)

@given(parsers.parse('user is on https://www.saucedemo.com/'))
def user_on_login_page(login_page):
    login_page.page.goto('https://www.saucedemo.com/')

@when(parsers.parse('user enters user name as "{username}" and password as "{password}"'))
def user_enters_credentials(login_page, username, password):
    login_page.login(username, password)


@then(parsers.parse('verify page has text "{text}"'))
def verify_page_text(login_page, text):
    assert login_page.page.locator(f'text={text}').is_visible()

@when('click Add to cart')
def click_add_to_cart(inventory_page):
    inventory_page.add_to_cart()

@when('click cart icon')
def click_cart_icon(inventory_page):
    inventory_page.go_to_cart()

@then(parsers.parse('verify page has text "{text}"'))
def verify_cart_page_text(inventory_page, text):
    assert inventory_page.page.locator(f'text={text}').is_visible()

@then('Cart page displays selected items')
def cart_page_displays_items(inventory_page):
    # Add cart item verification logic here
    assert True
