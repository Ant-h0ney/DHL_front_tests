from selene.support.shared import browser

from front.pages import mainpage, product_page


def test_search_by_sku():
    browser.config.hold_browser_open = True
    sku = '167905'
    # PREP
    mainpage.open()

    # WHEN
    mainpage.search(sku)
    # search_line.search_for(sku)

    # THEN
    product_page.check_sku(sku)
    # product_sku.check_value(sku)

