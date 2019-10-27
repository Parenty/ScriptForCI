import pytest
from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--headless', action='store', default='true', help='Is headless driver?')


@pytest.fixture(scope="function")
def get_url():
    """
    Return url
    """
    url = os.environ.get('URL')
    yield url


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        headless = request.config.getoption("--headless")
        chrome_options = webdriver.ChromeOptions()
        if headless == "true":
            # Set headless flag to true
            chrome_options.add_argument("headless")
        print("\nstart browser for test..")
        browser = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        print("\nstart browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
