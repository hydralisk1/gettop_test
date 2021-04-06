# Created by Joonil at 4/5/21
Feature: Test Scenarios for Price filter in GetTop

  Scenario Outline: User can use the Price filter in order to filter products with prices
    Given Open the shop page
    When User sets the price filter to <minimum_price> dollars and <maximum_price> dollars using the slide bar
    Then Click on the filter button
    When Click on X from the <which> price filter to remove it
    Then Verify <which> price filter slider handle position resents
    Then Verify the Price filter worked
    When Click on X from the <which> price filter to remove it
    Then Verify <which> price filter slider handle position resents
    Then Verify the Price filter worked

    # Don't set the same maximum and minimum prices
    # Filter slider would be overlay, and not work properly
    # 190 <= minimum_price <= 2400, step 10
    # 240 <= maximum_price <= 2400, step 10
    Examples:
      | minimum_price | maximum_price | which   | which   | which   | which   |
      |           500 |          1900 | minimum | minimum | maximum | maximum |
      |          1000 |          1500 | maximum | maximum | minimum | minimum |


  Scenario: User can use the Price filter in order to filter products with prices
    Given Open the shop page
    When User sets the price filter to 500 dollars and 1500 dollars using the slide bar
    Then Click on the filter button
    Then Verify the Price filter worked
    When Click on X from the minimum price filter to remove it
    Then Verify minimum price filter slider handle position resents
    Then Verify the Price filter worked
    When Click on X from the maximum price filter to remove it
    Then Verify maximum price filter slider handle position resents
    Then Verify the Price filter worked
