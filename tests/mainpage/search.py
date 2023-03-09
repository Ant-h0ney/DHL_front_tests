from selene import be, have
from selene.support.shared import browser


def test_search_line():
    browser.config.hold_browser_open = True

    # WHEN
    browser.open('')
    browser.element('#regular-search-input-desktop').type('167905').press_enter()

    # THEN
    browser.element('.email-signup-body').wait_until(be.visible)
    browser.element('.occ-sku').should(have.text('SKU: 167905'))

