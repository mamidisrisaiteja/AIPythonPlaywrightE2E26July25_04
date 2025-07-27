@auth @smoke
Feature: Authentication Module

  Scenario: Login with valid credentials
    Given user is on https://www.saucedemo.com/
    When user enters user name as "standard_user" and password as "secret_sauce"
    Then verify page has text "Products"
    Then Redirect to Products page

  Scenario: Login with invalid credentials
    Given user is on https://www.saucedemo.com/
    When user enters user name as "standard_use" and password as "secret_sauce"
    Then verify page has text "Login"
    Then Login Button should be still displayed
