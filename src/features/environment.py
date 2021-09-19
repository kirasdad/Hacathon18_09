from behave import use_fixture
from src.fixtures import login_page


def before_tag(context, tag):
    if tag == "fixture.login_page":
        use_fixture(login_page, context)
