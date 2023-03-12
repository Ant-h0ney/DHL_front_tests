from selene import be
from selene.support.shared import browser

from front.elements import product_sku, add_to_cart


def open(sku: str):  # NOQA
    browser.open(f'product/{sku}')


def check_sku(sku: str):
    product_sku.check_having(sku)


def have_sale_price():
    browser.element('.list-sale-price').should(be.present)


def have_product_image():
    browser.element('#cc-image-viewer .img-responsive').should(be.present)


def have_quantity_selector():
    browser.element('.quantity-value').should(be.present.and_(be.clickable))


def have_store_delivery():
    browser.element('#Q-bopis-delivery-option').should(be.present.and_(be.clickable))


def have_home_delivery():
    browser.element('#C-bopis-delivery-option').should(be.present.and_(be.clickable))


def have_add_to_cart():
    add_to_cart.check_having()
