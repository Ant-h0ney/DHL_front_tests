import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_preparation():
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 1200
    browser.config.window_height = 1000
    browser.config.base_url = 'https://www.dollartree.com/'
    yield
