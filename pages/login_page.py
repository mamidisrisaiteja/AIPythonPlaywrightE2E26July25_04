from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator('input[data-test="username"]')
        self.password_input = page.locator('input[data-test="password"]')
        self.login_button = page.locator('input[data-test="login-button"]')

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
