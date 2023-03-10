from selene import be, have
from selene.support.shared import browser

from front.elements import search_line, product_sku, wrapper


def test_search_by_sku():
    browser.config.hold_browser_open = True
    sku = '167905'
    # PREP
    browser.open('').wait.until(wrapper.focus('image').should(be.present))

    # WHEN
    search_line.input(sku)
    search_line.submit()
    browser.element('.email-signup-body').wait.until(be.present)

    # THEN
    product_sku.check_for_value(sku)
    # browser.element('.occ-sku').should(have.text(f'SKU: {sku}'))

