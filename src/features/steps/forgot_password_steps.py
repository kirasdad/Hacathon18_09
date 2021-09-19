from behave import *
from src.Pages.LoginPage import Login
from src.Locators.LoginPage import LoginPage


@when('I click link "Forgot your password"')
def step_impl(context):
    context.login_page.click(LoginPage.Login.forgot_link)


@step("input my email in window")
def step_impl(context):
    context.login_page.input(LoginPage.Login.forgot_email, context.user.email)


@step('click button "Reset password"')
def step_impl(context):
    context.login_page.click(LoginPage.Login.forgot_button)


@then('I see "Password reset instructions have been sent to your"')
def step_impl(context):
    context.login_page.driver.find_element_by_css_selector(LoginPage.Login.forgot_description).is_displayed()
