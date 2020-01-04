from behave import given, when, then
from selenium.webdriver.common.keys import Keys


@given("Open http://www.amazon.com")
def user_on_amazon_page(context):
    context.driver.get("http://www.amazon.com")


@given("enter term \"Software Development\"")
def user_enters_term(context):
    context.driver.find_element_by_id("twotabsearchtextbox").send_keys("Software Development")


@when("the customer submits the search")
def user_submits_search(context):
    context.driver.find_element_by_name("site-search").submit()


@then("the results of that search are displayed")
def results_are_displayed(context):
    elements = context.driver.find_elements_by_class_name("s-result-item")
    assert len(elements) > 0


@then("the number of results is displayed as a positive integer")
def number_results_is_positive(context):
    element = context.driver.find_element_by_xpath("//*[@id=\"search\"]/span[2]/h1/div/div[1]/div/div/span[1]")
    words = element.text[:element.text.index("results for") - 1].split()
    number = int(words[(len(words) - 1)].replace(',', ''))
    assert number > 0


@when("the customer doesn't enter the search term")
def no_search_term_submitted(context):
    context.driver.find_element_by_id("twotabsearchtextbox").clear()
    context.driver.find_element_by_name("site-search").submit()


@then("the related items get displayed")
def related_items_get_displayed(context):
    elements = context.driver.find_elements_by_class_name("aok-relative")
    assert len(elements) > 0