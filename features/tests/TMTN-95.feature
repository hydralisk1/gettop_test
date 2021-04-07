# Created by Joonil at 4/7/21
Feature: Test Scenarios for no match in GetTop shop page

  Scenario Outline: The price filters work even when no products match found
    Given Open the shop page
    When User sets the price filter to <minimum_price> dollars and <maximum_price> dollars using the slide bar
    Then Click on the filter button
    Then "<no_products_message>" message shown if no products match selected filters
    When Click on X from the <which> price filter to remove it
    Then Verify the Price filter worked
    When Click on X from the <the_other_one> price filter to remove it
    Then Verify the Price filter worked

    # Set minimum price and maximum price to the range of no products found

    Examples:
      | minimum_price | maximum_price | which   | the_other_one | no_products_message                              |
      |          1200 |          2000 | minimum | maximum       | No products were found matching your selection. |
      |          1200 |          1500 | maximum | minimum       | No products were found matching your selection. |


#  Scenario: The price filters work even when no products match found
#    Given Open the shop page
#    When User sets the price filter to 1200 dollars and 2000 dollars using the slide bar
#    Then Click on the filter button
#    Then "No products were found matching your selection." message shown if no products match selected filters
#    When Click on X from the maximum price filter to remove it
#    Then Verify the Price filter worked
#    When Click on X from the minimum price filter to remove it
#    Then Verify the Price filter worked
