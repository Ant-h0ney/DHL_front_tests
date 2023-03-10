from selene import Element
from selene.support.shared import browser


def focus(elem) -> Element:
    wrapper = browser.element(f'[class$={elem}-wrapper]')
    return wrapper
