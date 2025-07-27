@cart
Feature: Cart Module

  Scenario: View cart contents
    Given user is on https://www.saucedemo.com/
    When user enters user name as "standard_user" and password as "secret_sauce"
    Then verify page has text "Products"
   When click Add to cart
    And click cart icon
    Then verify page has text "Your Cart"
    Then Cart page displays selected items
