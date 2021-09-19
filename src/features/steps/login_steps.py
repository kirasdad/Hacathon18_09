from behave import *
from src.Locators.LoginPage import LoginPage


@given("I have account")
def created_user(context):
    context.user_email = 'team38@gmail.com'
    context.user_password = 'Team38'


@when("I open Login page")
def login_page(context):
    context.login_page.to_page('https://apparel-uk.local:9002/ucstorefront/en/login')


@step("enter my email and password")
def input_email_password(context):
    context.login_page.input(LoginPage.Login.email, context.user_email)
    context.login_page.input(LoginPage.Login.password, context.user_password)


@step('press a button "Log in"')
def press_login(context):
    context.login_page.click(LoginPage.Login.login_button)


@then("I see main page")
def see_mail_page(context):
    assert context.login_page.driver.current_url == "https://apparel-uk.local:9002/ucstorefront/en/"
