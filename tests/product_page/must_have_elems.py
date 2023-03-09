from selene import be, have
from selene.support.shared import browser


def test_search_line():
    browser.config.hold_browser_open = True

    # WHEN
    browser.open('product/281486')

    # THEN
    browser.element('.email-signup-body').wait_until(be.visible)
    browser.element('.occ-sku').should(have.text('SKU: 281486'))
    browser.element('.list-sale-price').should(be.visible)
    browser.element('#cc-image-viewer .img-responsive').should(be.visible)
    browser.element('.quantity-value').should(be.visible.and_(be.clickable))
    browser.element('#Q-bopis-delivery-option').should(be.visible.and_(be.clickable))
    browser.element('#C-bopis-delivery-option').should(be.visible.and_(be.clickable))
    browser.element('#cc-prodDetails-addToCart').should(have.text('ADD TO CART'))
