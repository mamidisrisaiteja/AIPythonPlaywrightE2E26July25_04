from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.sort_icon = page.locator('.product_sort_container')
        self.add_to_cart_button = page.locator('button[data-test="add-to-cart-sauce-labs-backpack"]')
        self.cart_icon = page.locator('.shopping_cart_link')

    def sort_products_az(self):
        self.sort_icon.select_option('az')

    def add_to_cart(self):
        self.add_to_cart_button.click()

    def go_to_cart(self):
        self.cart_icon.click()
