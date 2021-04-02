# Created by Joonil at 4/2/21
Feature: Test Scenarios for footer links in GetTop

  Scenario Outline: "You may also like…" block is shown and working properly
    Given Open the <product-title> product page
    Then "<block-title>" block is shown
    And It contains products
    And Verify all product links under the block are clickable and take to correct pages

    Examples:
      | product-title  | block-title        |
      | macbook-air    | You may also like… |
      | macbook-pro-13 | You may also like… |
      | iphone-11      | You may also like… |
      | iphone-11pro   | You may also like… |
      | ipad           | You may also like… |
      | ipad-pro       | You may also like… |


  Scenario: "You may also like…" block is shown and working properly
    Given Open the ipad product page
    Then "You may also like…" block is shown
    And It contains products
    And Verify all product links under the block are clickable and take to correct pages

