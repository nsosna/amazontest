from selenium import webdriver


def browser_chrome(context, timeout=30, **kwargs):
    driver = webdriver.Chrome("/opt/chromedriver")
    context.driver = driver
    yield context.driver
    driver.quit()
