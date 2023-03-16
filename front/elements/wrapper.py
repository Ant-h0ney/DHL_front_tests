import allure
from selene import Element, be
from selene.support.shared import browser


@allure.step('Focus on elements in wrapper "{elem}"')
def focus_presented(elem) -> Element:
    object_wrapper = browser.element(f'[class$={elem}-wrapper]')
    browser.all(f'[class$={elem}-wrapper]').with_(timeout=6).wait.until(be.visible)
    return object_wrapper
