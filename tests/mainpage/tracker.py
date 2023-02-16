from selene import be, have
from selene.support.shared import browser


def test_one_track_number():
    browser.config.hold_browser_open = False
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 1200
    browser.config.window_height = 1000
    browser.config.base_url = 'https://www.logistics.dhl.ru/ru-en/home.html'

    browser.open('')
    browser.element('[class*=tracking-input] [name=tracking-id]').type('1234567890')
    browser.element('[class*=tracking-input] [type=submit]').click()

    # should
    browser.element('[class*=tracking-result][class*=status-code-200]').wait_until(be.existing)
