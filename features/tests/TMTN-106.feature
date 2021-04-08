# Created by Joonil at 4/8/21
Feature: Test Scenarios for Product Categories on the top menu in GetTop
  Scenario Outline: Product Categories work well
    Given Open GetTop page
    When Hover over <category> Category Menu
    Then User can see all items under the category
    Then Verify correct pages open when clicking on each product

    Examples:
      | category    |
      | Mac         |
      | iPhone      |
      | iPad        |
      | Watch       |
      | Accessories |

  Scenario: Product Category iPad works well
    Given Open GetTop page
    When Hover over iPad Category Menu
    Then User can see all items under the category
    Then Verify correct pages open when clicking on each product
