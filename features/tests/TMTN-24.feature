# Created by Joonil at 4/5/21
Feature: Test Scenarios for Sorting by price in GetTop

  Scenario Outline: Sort by price select box is working properly in the shop page
    Given Open the shop page
    When Choose <sort-order> from the select box
    Then Verify products are displayed in correct order

    Examples:
      | sort-order                 |
      | Sort by price: high to low |
      | Sort by price: low to high |


  Scenario: Sort by price select box is working properly in the shop page
    Given Open the shop page
    When Choose Sort by price: high to low from the select box
    Then Verify products are displayed in correct order
    When Choose Sort by price: low to high from the select box
    Then Verify products are displayed in correct order


  Scenario Outline: When user open sorted pages via a direct link, the Select box and sort order are properly working
    Given Open the shop page via https://gettop.us/shop/<direct_link>
    Then Verify the Select box displays correct option
    Then Verify products are displayed in correct order

    Examples:
      | direct_link         |
      | ?orderby=price-desc |
      | ?orderby=price      |


  Scenario: When user open sorted pages via a direct link, the Select box and sort order are properly working
    Given Open the shop page via https://gettop.us/shop/?orderby=price-desc
    Then Verify the Select box displays correct option
    Then Verify products are displayed in correct order


  Scenario: When user open sorted pages via a direct link, the Select box and sort order are properly working
    Given Open the shop page via https://gettop.us/shop/?orderby=price
    Then Verify the Select box displays correct option
    Then Verify products are displayed in correct order
