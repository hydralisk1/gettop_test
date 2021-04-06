# Created by Joonil at 4/6/21
Feature: Test Scenarios for recently viewed items in GetTop

  Scenario Outline: User can see recently viewed items, open them and is taken to correct page
    Given Open the shop page
    When Click on the <number> product on the page
    Then Open the shop page again
    Then Verify the recently viewed item is on top in the item list
    When Click on the recently viewed item on top
    Then Verify the correct page is open

    Examples:
      | number |
      | 1st    |
      | 4th    |
      | 11th   |

  Scenario: User can see recently viewed items, open them and is taken to correct page
    Given Open the shop page
    When Click on the 2nd product on the page
    Then Open the shop page again
    Then Verify the recently viewed item is on top in the item list
    When Click on the recently viewed item on top
    Then Verify the correct page is open
