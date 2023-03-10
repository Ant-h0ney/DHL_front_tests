from selene.support.shared import browser

from front.elements import search_line, product_sku


def test_search_by_sku():
    browser.config.hold_browser_open = True
    sku = '167905'
    # PREP
    browser.open('')

    # WHEN
    search_line.search_for(sku)

    # THEN
    product_sku.check_for_value(sku)

