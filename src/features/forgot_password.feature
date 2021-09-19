@fixture.login_page
Feature: Forgot your password
As a user, I want to login my account without remembering the password

Scenario: Login to account without remembering the password
Given I have account
When I click link "Forgot your password"
And input my email in window
And click button "Reset password"
Then I see "Password reset instructions have been sent to your"
