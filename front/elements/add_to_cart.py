from selene import have, be

from front.elements import wrapper


def check_having():
    wrapper.focus_presented("add-to-cart").element("#cc-prodDetails-addToCart").should(
        be.present.and_(have.text("ADD TO CART"))
    )
