# Created by Joonil at 4/7/21
Feature: Test Scenarios for Account Login Error Handling in GetTop

  Scenario Outline: User cannot login with invalid ids and passwords
    Given Open the my account page
    When User tries log in with <email> and <password>
    Then Verify login was failed
    Then Verify correct error message was displayed

    # 'blank email' to clear the email field
    # 'blank password' to clear the password field
    Examples:
    |email         | password       |
    |test@test.com | blank password |
    |blank email   | test           |
    |test@test.com | test           |

  Scenario: User cannot login with invalid ids and passwords
    Given Open the my account page
    When User tries log in with test@test.com and blank password
    Then Verify login was failed
    Then Verify correct error message was displayed
    When User tries log in with blank email and test
    Then Verify login was failed
    Then Verify correct error message was displayed
    When User tries log in with test@test.com and test
    Then Verify login was failed
    Then Verify correct error message was displayed
