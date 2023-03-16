import allure
from selene import be, have
from selene.support.shared import browser

from front.elements import wrapper


@allure.step('Open product "{sku}" page')
def open(sku: str):  # NOQA
    browser.open(f'product/{sku}')


@allure.step('"SKU: {sku}" text and visibility validation')
def check_sku(sku: str):
    wrapper.focus_presented('product-sku').element('.occ-sku').should(have.text(f'SKU: {sku}'))


@allure.step('Price for each validation')
def have_each_price():
    browser.element('.list-sale-price').should(be.present)


@allure.step('Total price validation')
def have_total_price():
    wrapper.focus_presented('total').element('.total-value').should(be.present)


@allure.step('Product image validation')
def have_product_image():
    browser.element('#cc-image-viewer .img-responsive').should(be.present)


@allure.step('Quantity selector validation')
def have_quantity_selector():
    browser.element('.quantity-value').should(be.present.and_(be.clickable))


@allure.step('Ship to store option validation')
def have_ship_to_store():
    browser.element('#Q-bopis-delivery-option').should(be.present.and_(be.clickable))


@allure.step('Ship to home option validation')
def have_ship_to_home():
    browser.element('#C-bopis-delivery-option').should(be.present.and_(be.clickable))


@allure.step('Add to cart button validation')
def have_add_to_cart():
    wrapper.focus_presented("add-to-cart").element("#cc-prodDetails-addToCart").should(
        be.present.and_(have.text("ADD TO CART"))
    )
