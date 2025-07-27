@auth @smoke
Feature: User Login
  As a registered user
  I want to log in to the portal
  So that I can access my account

  Scenario: Validate user login flow
    Given the user is on the login page
    When the user logs in with valid credentials
    Then the user should see the dashboard
