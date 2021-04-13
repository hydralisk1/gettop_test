# Created by Joonil at 4/1/21
Feature: Test Scenarios for footer links in GetTop

  Scenario: Footer shows Best Selling, Latest, Top Rated categories
    Given Open GetTop page
    Then Verify Best Selling, Latest, Top Rated categories are shown in the footer

  Scenario: All products in the footer have price, name, star-rating
    Given Open GetTop page
    Then Verify all products in the footer have price, name, star-rating

  Scenario: "Copyright 2021" shown in the footer
    Given Open GetTop page
    Then Verify "Copyright 2021" is shown in the footer

  Scenario: Footer has button to go back to top
    Given Open GetTop page
    Then Verify the footer has a button to go back to top

  Scenario: Footer has working links to all product categories
    Given Open GetTop page
    Then Verify the footer has working links to all product categories