from behave import use_fixture

from fixtures import browser_chrome


def before_all(context):
    if context.config.userdata['browser'] == "chrome":
        use_fixture(browser_chrome, context)