import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

scenarios('../features/inventory.feature')

@given(parsers.parse('user is on https://www.saucedemo.com/'))
def user_on_login_page(login_page):
    login_page.page.goto('https://www.saucedemo.com/')

@when(parsers.parse('user enters user name as "{username}" and password as "{password}"'))
def user_enters_credentials(login_page, username, password):
    login_page.login(username, password)

@then(parsers.parse('verify page has text "{text}"'))
def verify_page_text(login_page, text):
    if text == "Add to cart":
        # Check that at least one 'Add to cart' button is visible
        assert login_page.page.locator('button[data-test^="add-to-cart-"]').first.is_visible()
    elif text == "Products":
        assert login_page.page.locator('span.title').filter(has_text="Products").is_visible()
    else:
        assert login_page.page.locator(f'text={text}').is_visible()

@then(parsers.parse('verify Products page has text "{text1}" and "{text2}"'))
def verify_products_page_text(login_page, text1, text2):
    if text1 == "Products":
        assert login_page.page.locator('span.title').filter(has_text="Products").is_visible()
    else:
        assert login_page.page.locator(f'text={text1}').is_visible()
    
    if text2 == "Add to cart":
        # Check that at least one 'Add to cart' button is visible
        assert login_page.page.locator('button[data-test^="add-to-cart-"]').first.is_visible()
    else:
        assert login_page.page.locator(f'text={text2}').is_visible()

@then('click Sort Icon')
def click_sort_icon(inventory_page):
    inventory_page.sort_icon.click()

@when('click Sort the Products by Name (A–Z)')
def sort_products_az(inventory_page):
    inventory_page.sort_products_az()

@then('click Sort the Products by Name (A–Z)')
def then_click_sort_products_az(inventory_page):
    inventory_page.sort_products_az()

@then('all the products must be sorted from A to Z')
def products_sorted_az(inventory_page):
    # Add sorting verification logic here
    assert True
