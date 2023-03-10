from selene import be
from selene.support.shared import browser


def wait(css: str):
    browser.wait_until(browser.element(css).should(be.present))
