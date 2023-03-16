from selene.support.shared import browser

from front.pages import product_page


def test_elems_on_page():
    browser.config.hold_browser_open = True
    sku = '281486'
    # WHEN
    product_page.open(sku)

    # THEN
    product_page.check_sku(sku)
    product_page.have_product_image()
    product_page.have_each_price()
    product_page.have_quantity_selector()
    product_page.have_total_price()
    product_page.have_ship_to_store()
    product_page.have_ship_to_home()
    product_page.have_add_to_cart()
