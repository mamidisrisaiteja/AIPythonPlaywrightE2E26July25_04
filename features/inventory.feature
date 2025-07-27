@inventory
Feature: Inventory Module

  Scenario: Verify product listing
    Given user is on https://www.saucedemo.com/
    When user enters user name as "standard_user" and password as "secret_sauce"
    Then verify page has text "Products"
    And verify page has text "Add to cart"
    Then verify Products page has text "Products" and "Add to cart"

  Scenario: Sort products by Name (A–Z)
    Given user is on https://www.saucedemo.com/
    When user enters user name as "standard_user" and password as "secret_sauce"
    Then verify page has text "Products"
    And click Sort Icon
    And click Sort the Products by Name (A–Z)
    Then all the products must be sorted from A to Z
