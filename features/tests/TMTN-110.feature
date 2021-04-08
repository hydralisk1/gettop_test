# Created by Joonil at 4/8/21
Feature: Test Scenarios for Category pages in GetTop
  Scenario Outline: Category pages show only correct items, number of results, and user can open Quick view in the page
    Given Open <category> Category page
    Then Only items of correct category are shown
    Then "Showing all N results" is present and reflects correct amount of items
    Then Verify all items have Category, Name and Price
    Then User can click on Quick View for all items and close it by clicking on closing X
    Then User can click on Quick View for all items and add product to cart

    Examples:
      | category |
      | Macbook  |
      | iPhone   |
      | iPad     |
      | Watch    |
      | Airpods  |


#  Scenario: Category pages show only correct items, number of results, and user can open Quick view in the page
#    Given Open Macbook Category page
#    Then Only items of correct category are shown
#    Then "Showing all N results" is present and reflects correct amount of items
#    Then Verify all items have Category, Name and Price
#    Then User can click on Quick View for all items and close it by clicking on closing X
#    Then User can click on Quick View for all items and add product to cart
