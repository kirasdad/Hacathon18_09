from behave import fixture
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from src.Pages.LoginPage import Login


@fixture(name='fixture.login_page')
def login_page(context):
    options = webdriver.ChromeOptions()
    options.add_argument('ignore-certificate-errors')
    browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    context.login_page = Login(browser)
    yield context.login_page
    context.login_page.driver.close()
