from behave import *


@given("I open Login page")
def open_login_page(context):
    context.login_page.to_page('https://apparel-uk.local:9002/ucstorefront/en/login')


@when("created new user")
def crete_account(context):
    context.login_page.create_account()


@then("I see welcome text")
def welcome_text(context):
    text = context.login_page.driver.find_element_by_css_selector('.alert.alert-info.alert-dismissable.getAccAlert').is_displayed()
    assert text


@step("I see main banner")
def mail_banner(context):
    banner = context.login_page.driver.find_element_by_css_selector("img[title='Start Your Season']").is_displayed()
    assert banner
