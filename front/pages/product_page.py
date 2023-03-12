from selene import be, have
from selene.support.shared import browser

from front.elements import wrapper


def open(sku: str):  # NOQA
    browser.open(f'product/{sku}')


def check_sku(sku: str):
    wrapper.focus_presented('product-sku').element('.occ-sku').should(have.text(f'SKU: {sku}'))


def have_each_price():
    browser.element('.list-sale-price').should(be.present)


def have_total_price():
    wrapper.focus_presented('total').element('.total-value').should(be.present)


def have_product_image():
    browser.element('#cc-image-viewer .img-responsive').should(be.present)


def have_quantity_selector():
    browser.element('.quantity-value').should(be.present.and_(be.clickable))


def have_store_delivery():
    browser.element('#Q-bopis-delivery-option').should(be.present.and_(be.clickable))


def have_home_delivery():
    browser.element('#C-bopis-delivery-option').should(be.present.and_(be.clickable))


def have_add_to_cart():
    wrapper.focus_presented("add-to-cart").element("#cc-prodDetails-addToCart").should(
        be.present.and_(have.text("ADD TO CART"))
    )