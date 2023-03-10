from selene.support.shared import browser


def input(text: str):  # NOQA
    browser.element('#regular-search-input-desktop').set(text)


def submit():
    browser.element('.search-box .input-group-btn').click()
